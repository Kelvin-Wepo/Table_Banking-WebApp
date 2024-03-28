from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, date, timedelta
# from dateutil.relativedelta import *
from dateutil.relativedelta import relativedelta
from django.db.models import Sum

#table for the custom user other than the default user.
class CustomUser(AbstractUser):
	roles = (('Admin', 'Admin'), ('Ordinary', 'Ordinary'))
	Role = models.CharField(max_length=250, choices=roles, blank=True, null=True, default='Admin')
	full_name = models.CharField(max_length=100, blank=True, null= True, default="Name")
	username = models.CharField(max_length=30, unique=True, blank=True, null=True)
	is_active = models.BooleanField(default=False)   # can login
	is_staff = models.BooleanField(default=False)  # staff user non superuser
	is_superuser = models.BooleanField(default=False)
	email = models.EmailField(max_length=255, blank=True, null=True, default='')
	# telephone = models.IntegerField(default=0, blank=True, null=True)
	USERNAME_FIELD = 'username'
	REQUIRED_FILEDS = []
	def __str__(self):
		return self.full_name

#table for members of the sacco.
class Member(models.Model):
	is_active = models.BooleanField(default=True)   # can login
	roles = (('Admin', 'Admin'), ('Ordinary', 'Ordinary'))
	atte = (('Present', 'Present'), ('Absent', 'Absent'))
	joining_date =models.DateTimeField(auto_now_add=True, blank=True)
	status = models.CharField(max_length=30,choices=atte,default='Absent', blank=True, null=True)
	email = models.EmailField(max_length=255, blank=True, null=True)
	telephone = models.CharField(max_length=30, null=False)
	first_name = models.CharField(max_length=30, blank=True, null=True)
	last_name = models.CharField(max_length=255, blank=True, null=True)
	username = models.CharField(max_length=30, unique=True, blank=True, null=True)
	application_fee = models.IntegerField(default=10000, blank=True, null=True)
	Role = models.CharField(max_length=250, choices=roles)
	
	def __str__(self):
		return str(self.last_name) + ' ' + str(self.first_name)

	#decoratiing the member model with a wtrapper.
	@property 
	def total_saving(self):
		cycles = Cycle.objects.filter(is_active=True)
		for i in cycles:
			startdate= i.cycle_period_start
			enddate= i.cycle_period_end
			results=Saving.objects.filter(date__range=(startdate, enddate),name=self.id).aggregate(totals=models.Sum("amount"))
			if (results['totals']):
				return results["totals"]
			else:
				return 0 

	@property
	def total_social_fund(self):
		cycles = Cycle.objects.filter(is_active=True)
		for i in cycles:
			if (self.first_name != None and self.last_name != None):
				name = (self.first_name + " " + self.last_name)
				startdate = i.cycle_period_start
				enddate = i.cycle_period_end
				results = SocialFund.objects.filter(date__range=(
						startdate, enddate), full_name=name).aggregate(totals=models.Sum("social_fund"))
				if (results['totals']):
					return results["totals"]
				else:
					return 0
	@property
	def maximum_loan_amount(self):
		cycles = Cycle.objects.filter(is_active=True)
		for i in cycles:
			startdate = i.cycle_period_start
			enddate = i.cycle_period_end
			results = Saving.objects.filter(date__range=(
					startdate, enddate), name=self.id).aggregate(totals=models.Sum("amount"))
			if (results['totals']):
				x=(results["totals"]*2)
				return x
			else:
				return 0

	@property
	def full_name(self):
		return '%s %s' % (self.last_name, self.first_name)
		# return (str(self.last_name )+ ' '+ str(self.first_name))

	@property
	def loan_status(self):
		get_loans=Loan.objects.all()
		for i in get_loans:
			filtering=PayingLoan.objects.filter(loan_id=i.id, name=self.full_name)
			for j in filtering:
				if j.loan_status == 'SETTLED':
					return 'No Running Loan'
				else:
					return 'Running Loan'	
				
				return j.loan_status


class SocialFund(models.Model):
	full_name = models.CharField(max_length=220, blank=True, null=True)
	date = models.DateField(max_length=100, blank=True, null=True)
	social_fund = models.IntegerField(default=0, blank=True, null=True)
	def __str__(self):
		return self.full_name

class Attendance(models.Model):
	today = datetime.now()
	years=today.year
	full_name = models.CharField(max_length=123, null=True, blank=True)
	date = models.DateField(blank=True, null=True)
	status = models.CharField(max_length=100, null=True, blank=True)
	attendance_year = models.CharField(max_length=255, blank=True, null=True, default=years)
	attendance_month = models.CharField(max_length=255, blank=True, null=True)
	attendance_day = models.CharField(max_length=255, blank=True, null=True)
	def __str__(self):
		return self.full_name
    
class Cycle(models.Model):
	cycle_name =  models.CharField( max_length=220, null=True, blank=True, unique=True)
	rate = models.IntegerField(default=15, null=True, blank=True)
	cycle_period_start = models.DateField(max_length=255, blank=False, null=False, unique=True)
	cycle_period_end = models.DateField(max_length=255, blank=False, null=False, unique=True)
	is_active = models.BooleanField(default=True) 
	def __str__(self):
		return str(self.cycle_period_start.year) + "/" + str(self.cycle_period_end.year)

class Saving(models.Model):
	date = models.DateField(max_length=100, blank=True, null=True)
	name = models.ForeignKey(
		Member, on_delete=models.CASCADE, max_length=100, null=True, blank=True)
	amount = models.IntegerField(default=0, null=True, blank=True)
	def __str__(self):
		return self.name
		
class Loan(models.Model):
	status = (("RUNNING", "RUNNING"), ("SETTLED", "SETTLED"))
	date = models.DateField(max_length=100, blank=True, null=True)
	name = models.ForeignKey(Member, on_delete=models.CASCADE,
	                     max_length=100, null=True, blank=True)
	amount = models.IntegerField(default=0, null=True, blank=True)
	interest_rate = models.IntegerField(default=0)
	loan_period = models.IntegerField(default=0, null=True, blank=True)
	loan_status = models.CharField(max_length=100,choices=status, default='RUNNING', null=True, blank=True)
	recorded_by =models.CharField(max_length=220, blank=True, null=True)
	def __str__(self):
		return str(self.name)

	@property
	def total_repayments(self):
		if PayingLoan.objects.filter(loan_id=self.id).exists():
			get_loan = PayingLoan.objects.filter(loan_id=self.id)
			for i in get_loan:
				return i.total_paid
		else:
			return 0
	@property
	def balance(self):
		if PayingLoan.objects.filter(loan_id=self.id).exists():
			get_loan = PayingLoan.objects.filter(loan_id=self.id)
			for i in get_loan:
				return i.balance
		else:
			return self.amount
	@property
	def status(self):
		if PayingLoan.objects.filter(loan_id=self.id).exists():
			get_loan = PayingLoan.objects.filter(loan_id=self.id)
			for i in get_loan:
				return i.loan_status
		else:
			return 'RUNNING'

	@property
	def deadline(self):
		end_date = (self.date)+relativedelta(months=+self.loan_period)
		return end_date
   
	@property
	def repayment(self):
		interest = ((self.interest_rate / 100) * self.loan_period * self.amount)
		loan_repayment = interest + self.amount
		return loan_repayment

	@property
	def grace_period(self):
		grace_date = (self.date)+relativedelta(months=+(self.loan_period + 1))
		return grace_date
	
	@property
	def penalties(self):
		pen_date=date.today()
		if pen_date >= self.grace_period and self.status == 'RUNNING':
			# penalted=(self.repay) + (self.interest)
			# self.amount=penalted
			# self.save() 
			return (self.repayment/2)
		elif pen_date >= self.grace_period and self.status == 'SETTLED':
			return 'Not Penalized'
		else:
			return 'No Penalty Yet'

	@property
	def loan_interest(self):
		interest = ((self.interest_rate / 100) * self.loan_period * self.amount)
		return interest
		
class PayingLoan(models.Model):
	status = (("RUNNING", "RUNNING"), ("SETTLED", "SETTLED"))
	loan_id = models.CharField(max_length=100, blank=True, null=True)
	date = models.DateField(max_length=100, blank=True, null=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	amount = models.IntegerField(null=True, blank=True, default=0)
	total_paid = models.IntegerField(blank=True, default=0)
	balance = models.IntegerField(blank=True, default=0)
	loan_status = models.CharField(max_length=100, choices=status, default='RUNNING', null=True, blank=True)
	@property
	def total_repayment(self):
		get_all_loans = Loan.objects.all()
		for j in get_all_loans:
			cycle = Cycle.objects.filter(is_active=True)
			for i in cycle:
				startdate = i.cycle_period_start
				enddate = i.cycle_period_end
			results = PayingLoan.objects.filter(date__range=(
				startdate, enddate), loan_id=j.id).aggregate(totals=models.Sum("total_paid"))
			if (results['totals']):
				x=(results["totals"])
				return x
			else:
				return 0
	def __str__(self):
		return str(self.name)

class Stock(models.Model):
	ticker = models.CharField(max_length=10)
	openn = models.FloatField()
	close = models.FloatField()
	volume = models.IntegerField()
	def __str__(self):
		return str(self.ticker)

class LookUp(models.Model):
	name = models.CharField(unique=True, max_length=220, blank=False, null=False)
	def __str__(self):
		return self.name

class LookupDetail(models.Model):
	Lookup_Name = models.ForeignKey(LookUp, on_delete=models.CASCADE, max_length=220, blank=False, null=False)
	Details = models.CharField(max_length=220, blank=False, null=False)
	def __str__(self):
		return self.Lookup_Name
