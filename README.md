# User-Management-Web-App
User Management Web App is a simple Flask and PostgreSQL-based system that allows users to register, update, and search for their data through a web interface. It features secure form submissions and efficient database management, making it ideal for small-scale user management or full-stack development projects.


User Management App - README

Overview:
----------
This is a simple User Management application built using Flask and PostgreSQL. The application allows users to add, view, and delete records from a PostgreSQL database.

Prerequisites:
--------------
1. Python 3.x installed on your machine.
2. PostgreSQL installed and a database named `user_database` created with a `users` table.
3. Required Python packages installed (see requirements below).

Requirements:
--------------
Run the following command to install required libraries:
$ pip install flask psycopg2-binary

Application Structure:
----------------------
- app.py: The main application file containing all the routes and database connection functions.
- templates/: Directory containing HTML files (home.html, add_user.html, view_users.html).
- static/: (Optional) To include any static resources like CSS.

Setup and Execution:
----------------------
1. Database Setup:
   - Open pgAdmin or your preferred PostgreSQL client.
   - Create a database `user_database` and a `users` table.

2. Configure Environment:
   - In your terminal or VS Code, set up a virtual environment and activate it:
     $ python -m venv venv
     $ .\venv\Scripts\activate  (on Windows) or $ source venv/bin/activate (on Mac/Linux)

   - Set the FLASK_APP environment variable:
     $ $env:FLASK_APP = "app"  (on PowerShell)
     $ export FLASK_APP=app    (on Bash)

3. Running the Application:
   $ flask run

Accessing the Application:
--------------------------
Once running, access the application at:
http://127.0.0.1:5000/

Functional Routes:
------------------
- `/` : Home page to navigate between options to add or view users.
- `/add_user` : Page for adding new user information.
- `/view_users` : Page to view and delete user records.

Contact:
--------
For any questions or issues, please reach out at [Your Email Address].
