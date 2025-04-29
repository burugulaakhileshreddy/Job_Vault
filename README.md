Job Vault
Job Vault is a personal portfolio and job application manager built with Django. It's designed to help users keep track of multiple job applications in one place, providing more structure and accessibility than traditional spreadsheets.

About the Project
Job Vault allows you to:

Host multiple personal portfolios

Store job applications details with company details, platforms, job links.

Attach tailored resumes and cover letters for each job

Store important communication or notes (like recruiter messages or interview feedback)

Categorize applications for easy tracking and future reference

This tool provides a streamlined alternative to managing your job search compared to storing everything in Excel sheets or random folders.

This project is built using HTML and CSS for the frontend, and Python Django for the backend. It follows a clean, responsive design and utilizes Django’s powerful features to manage backend logic and database interactions.

Frontend: HTML is used for structuring the content, while CSS styles the layout, ensuring a responsive and user-friendly interface.

Backend: Django handles the server-side logic, offering a secure, scalable framework for the application. The project uses SQLite 3 as the inbuilt database for efficient data storage and management.

Git Workflow 

main -	Live production code – stable and deployed
develop - Integration branch for all tested and completed features
features - Developers build and add new features here
release - Prepares final versions before going to main; connects to develop
Testing - QA team performs testing on features or release versions
Issues - Contains fixes for bugs found during testing; source: testing
hotfix - Emergency fixes for issues in production or pre-production
pre-production - Staging area before deploying to production

Issues Branch source is testing
Release branch source is develop
Testing branch souce is Release
Rest all the branches source is main branch

To Run This Project:

Software Requirements

Make sure the following software is installed on your system:
Python
Git
PyCharm (IDE)



Step-1: Check Python & Git Installation
After installing Python and Git, open your terminal and run:

python --version
git --version
If both return a version number, you're good to go!

Step-2: Configure Git in PyCharm
Open PyCharm

Go to File > Settings (or PyCharm > Preferences on macOS)

Navigate to:
Version Control > Git

Set the Path to Git executable:

Windows:
C:\Program Files\Git\bin\git.exe

macOS/Linux:
/usr/bin/git or simply git

Click Test to verify Git is working

Click OK to save settings

Step-3: Set Git User Info
To associate your name and email with Git commits, run the following in PyCharm’s terminal:

git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

Step-4: Clone the Repository in PyCharm
Copy the repository URL

Open PyCharm

Go to File > New Project from Version Control

Paste the URL in the "Get from Version Control" window

Choose your destination folder

Click Clone

Step-5: Set Up Python Interpreter
Once the project is cloned:

PyCharm might prompt you to set up a Python interpreter

Select the system Python that was already installed

Click OK or Apply

Step-6: Install Project Dependencies
In PyCharm's terminal, install Django:

pip install django

Step-7: Project Structure Overview
Job_Vault/
├── .venv/                   # Virtual environment
├── Project/                 # Django project folder
│   ├── Jv_app/              # Main Django app
│   ├── media/               # Media files
│   ├── db.sqlite3           # Database
│   ├── .gitignore
│   ├── manage.py            # Django management script
├── External Libraries/
├── Scratches and Consoles/

Job_Vault: PyCharm project name

Project: Django project name

Jv_app: Django app name

Double-check that files like settings.py match what’s in the Git repository.

Step-8: Run the Project
In the terminal, run the following commands in order:

python manage.py makemigrations   # Create initial DB migrations
python manage.py migrate          # Apply migrations to the database
python manage.py runserver        # Start the development server
Visit http://127.0.0.1:8000/ in your browser to see the running application.

You're All Set!
