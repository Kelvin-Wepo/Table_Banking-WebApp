# Table Banking Web App

This Table Banking Web App is designed to help organizations manage their member records, savings, loans, and social fund contributions efficiently. It provides a user-friendly interface for both administrators and members, ensuring smooth operations and transparency within the organization.

## Features

1. **Custom User Model**: The app includes a custom user model that extends Django's AbstractUser model to accommodate additional fields like roles (Admin/Ordinary), full name, and email.

2. **Member Management**: The app allows administrators to register new members and track their attendance. Members can be marked as present or absent, and their joining date is recorded automatically.

3. **Savings and Social Fund**: Members can contribute to savings and social funds through the app. The app calculates the total savings and social fund contributions for each member based on active cycles.

4. **Loan Management**: Members can apply for loans, and administrators can manage these applications. The app calculates the maximum loan amount a member can receive based on their savings. It also tracks loan repayments and provides information on the loan status.

5. **Cycle Management**: Administrators can create and manage savings and loan cycles. Cycles have a start and end date, and only active cycles are considered for savings and loan calculations.

6. **Attendance Tracking**: The app tracks member attendance and provides insights into their participation over time.

7. **Responsive Design**: The web app is designed to be responsive, ensuring a seamless user experience across devices.

## How to Use

To use the Table Banking Web App, follow these steps:

1. **Installation**: Clone the project from the repository and set up the Django environment.

2. **Database Setup**: Configure the database settings in the project's settings file and run migrations to create the database schema.

3. **Run the Server**: Start the Django development server and access the app through a web browser.

4. **User Registration**: Register as an admin user to access the admin panel and manage the app's functionalities.

5. **Member Management**: Add new members, mark attendance, and manage member records through the admin panel.

6. **Savings and Loans**: Track member savings, social fund contributions, and loan applications. Monitor loan repayments and manage loan cycles.

7. **Reporting**: Use the app's reporting features to generate insights and reports on member activities, savings, and loans.

## Technologies Used

- Django: Python-based web framework for backend development.
- HTML/CSS/JavaScript: Frontend technologies for user interface design.
- PostgreSQL: Database management system for data storage.
- Bootstrap: Frontend framework for responsive design.

## Future Enhancements

- **Improved User Interface**: Enhance the app's UI for a more modern and intuitive user experience.
- **Advanced Reporting**: Add more comprehensive reporting features for better data analysis.
- **Integration with Payment Gateways**: Integrate payment gateways to facilitate online transactions for savings, loans, and social fund contributions.
- **SMS/Email Notifications**: Implement notifications for members regarding savings, loans, and meeting attendance.

This Table Banking Web App is designed to streamline the operations of table banking organizations, providing them with the tools they need to manage their members and financial activities effectively.
