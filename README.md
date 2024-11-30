**HOTEL MANAGEMENT SYSTEM**

Project Overview
The Hotel and House Management System is a web-based platform designed to manage and streamline operations, bookings, customer support, and check-ins for both hotels and rental houses.

The website offers intuitive features for employees and administrators, providing a unified solution for the tracking and management of data records for both accommodations. This system is designed to efficiently capture, store, and process management data through a comprehensive digital platform tailored for the hospitality industry.
___________________________________________________________________________________________________________________________________________________________________________________________

**🔨 Built With:**

Python

Django

BootStrap css

JavaScript
___________________________________________________________________________________________________________________________________________________________________________________________

**🙋‍♂️ Members:**

Mark Andrew G. Magpatoc

Jhon Zydney Belia

Reden Misael P. Relacion
___________________________________________________________________________________________________________________________________________________________________________________________

**🚀 Table of Contents**

Installation

Features

Usage

Project Documentation/Resources
___________________________________________________________________________________________________________________________________________________________________________________________

**⚙️ Installation**

Follow these steps to set up the project on your local machine.

**Prerequisites**

Make sure you have the following software installed:

**Python 3.12.5 (you can check by running python --version or python3 --version in your terminal).
pip (Python's package manager), usually installed alongside Python.
Django (installed through pip).
MySQL Workbench
If you don't have these installed, download Python from the official website, and pip comes with it.

Follow these steps to install the project:

Clone the repository:

git clone https://github.com/username/repository-name.git](https://github.com/MarkAndrewMagpatoc/IM-2)
Navigate into the project directory:

cd NewDjango
cd myblogsite
Create a virtual environment (optional but recommended):

For Windows
python -m venv myenv
myenv\Scripts\activate
For MacOS/Linux:
python3 -m venv myenv
source myenv/bin/activate
Install dependencies:

pip install -r requirements.txt
-If the project doesn't include a requirements.txt file, you can manually install Django and other dependencies as needed:

 pip install django
Check Python and Django versions: Verify that Python and Django are properly installed:

Python
python --version
Django
 python -m django --version
Set up the database: Run the database migrations to create the necessary database tables:

python manage.py migrate
Create a superuser (optional, but required to access the Django admin panel): To create an admin user, run:

python manage.py createsuperuser
Follow the prompts to create a superuser with a username, email, and password.
Run the server: Once everything is set up, start the development server:

python manage.py runserver
You can now visit the application in your browser at http://127.0.0.1:8000/. The Django admin panel can be accessed at http://127.0.0.1:8000/admin/, where you can log in using the superuser credentials you just created.
__________________________________________________________________________________________________________________________________________________________________________________________

**💻 Usage**

Running the Application
After setting up the project and starting the server with python manage.py runserver, open the following in your web browser:

Home Page: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/ (Login using the superuser credentials you created)
__________________________________________________________________________________________________________________________________________________________________________________________

**📌 Features**

Signup

Login

Logout

Check In

Check Out

List of Hotel

List of House

Booking
__________________________________________________________________________________________________________________________________________________________________________________________

**📝 Project Documentation/Resources**

UI/UX DESIGN: [Figma Prototype](https://www.figma.com/design/TktngzeTP5bf4uMTeP9248/TriStar-hotel?node-id=0-1&node-type=canvas&t=K24LS8IFFaWsJZPX-0)

Gantt Chart: https://docs.google.com/spreadsheets/d/14rnpLmH4-e8J9e8jM-xr4y8bOOb3qkEWPW3cByORIsg/edit?gid=0#gid=0

Entity Relationship Diagram (ERD): https://drive.google.com/file/d/1M0JjFfJIbTFTJlBcKgbeFMd3d9LltwkM/view?usp=sharing

Functional Requirements Document (FRD): https://drive.google.com/file/d/11yqvEiPIjfF9QuBBk4FU_TDb-uRUCXrY/view?usp=sharing
