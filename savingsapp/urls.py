from django.urls import path
from savingsapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('MemberAccountRegister/', views.MemberAccountRegister, name='MemberAccountRegister'),
    path('Logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('Login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('Password-Reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('Done/Password-Reset/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('Complete/Password-Reset/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('Sacco-Account/', views.sacco_account, name='sacco-account'),
    path('Add-Member/', views.add_member, name='add-member'), 
    path('Edit-Member/<int:pk>/', views.edit_member, name='edit-member'),
    path('Member-Details/<int:pk>/', views.view_member, name='view-member'),
    path('Edit-Savings/<int:pk>/', views.edit_saving, name='edit-saving'),
    path('Savings-delete-member/<int:pk>/', views.delete_member, name='delete-member'),
    path('Member-Savings/<int:pk>/', views.view_savings, name='view-savings'),
    path('All-Members/', views.members_list, name='members-list'),
    path('Record-Attendance/', views.make_attendance, name='make-attendence'),
    path('Attendance-History/', views.attendence_history, name='attendence-history'),
    path('Record-Savings/', views.make_saving, name='make-saving'),
    path('All-Savings/', views.savings_list, name='savings-list'),
    
    path('Record-Social-Fund/', views.record_social_fund, name='record-social-fund'),
    path('Social-Fund-List/', views.social_fund_list, name='social-fund-list'),
    path('Social-Funds-Routine/<int:pk>/', views.social_fund_routine, name='social-fund-routine'),
    path('Manage-Cycles/', views.add_cycle, name='add-cycle'),
    path('Cycle-List/', views.cycle_list, name='cycle-list'),
    path('archiving-cycles/', views.archiving_cycle, name='archive-cycle'),
    path('Edit-Cycle/<int:pk>/', views.edit_cycle, name='edit-cycle'),
    # path('activate/<str:uidb64>/<str:token>/', views.activate_email, name='activate'), 
    path('Activate-Cycle/<int:pk>/', views.activate_cycle, name='activate-cycle'),
    path('Savings-delete-cycle/<int:pk>/', views.delete_cycle, name='delete-cycle'),

    path('Loan-Application/', views.give_loan, name='give-loan'),
    path('All-Loan-Repayments/', views.list_loan_repayment, name='loan-list'),
    path('All-Loans/', views.all_loans_given, name='all-loans'),
    path('Paying-Loan/<int:pk>/', views.pay_loan, name='pay-loan'),
    path('Edit-Loan-Repayment/<int:pk>/', views.edit_loan_repayment, name='edit-loan-repayment'),
    path('edit-loan/<int:pk>/', views.edit_loan, name='edit-loan'),
    path('delete-loan-details/<int:pk>/', views.delete_loan, name='delete-loan'),
    
    path('Add-Lookup/', views.add_lookup, name='add-lookup'),
    path('Lookup-Details/', views.add_lookup_details, name='add-lookup-details'),
    path('All-Look-Ups/', views.list_lookup_details, name='list-lookup-details'),
    path('stocks/', views.StockList.as_view()), 
    path('Loan-Repayment/<int:pk>/', views.view_loan_repaymnets, name='loan-repayments'),
]

from rest_framework.urlpatterns import format_suffix_patterns

