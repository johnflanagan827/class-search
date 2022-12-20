# Class Search
*Note: Currently, the Notre Dame Class Tool only works for Windows and Gmail.*

## Overview
This Notre Dame Class Search Tool allows Notre Dame students to add and track different class sections from https://classsearch.nd.edu.  The user can add, or remove, or view class sections by running `main.py`.  When the user adds a class section, the file `classes.txt` will be created or updated. After adding the class section, the user can recieve an email with status updates by running email_alerts.py.  After running email_alerts.py, the number of seats in `classes.txt` is updated. This process can be automated by creating a `.bat` file and running it with Windows Task Scheduler (see more details below). 

## About
The Notre Dame Class Search Tool uses [Selenium](https://www.selenium.dev/) 4.7.2 with [ChromeDriver](https://chromedriver.chromium.org/) to scrape data from https://classsearch.nd.edu.  The Python libraries [email](https://docs.python.org/3/library/email.html) and [ssl](https://docs.python.org/3/library/ssl.html) are used to securely send emails.  [Dotenv](https://www.npmjs.com/package/dotenv) 0.21.0 is used so that users can more securely store their email username and password in the `.env` file.

## Setup
The following command will pull and install the latest commit from this repository:
```
git clone https://github.com/johnflanagan827/Class-Search
```
To install selenium and dotenv, please run:
```
pip install selenium
pip install python-dotenv
````
After installing selenium and dotenv, you will need to download the ChromeDriver executable from the [ChromeDriver](https://chromedriver.chromium.org) website.

### App password
You will need to generate an app password, which is a special password that is designed for use with third-party applications such as Python scripts.  To turn on app passwords and generate an app password for a Google Account, you will need to follow these steps:

1. Go to your [Google Account](https://myaccount.google.com) settings by clicking on your profile picture in the top right corner of any Google page and selecting "Manage your Google Account" from the drop-down menu.
2. In the "Security" section of the "Personal info & privacy" tab, click on the "Signing in to Google" option.
3. Scroll down to the "Third-party apps with account access" section and click on the "Manage third-party access" button.
4. In the "Apps with account access" window that appears, you should see a list of apps that have access to your account. To turn on app passwords, you will need to toggle the switch next to "Allow less secure apps" to the "ON" position.
5. Once you have enabled app passwords, you can generate a new app password by clicking on the "Select app" drop-down menu and selecting the app you want to generate a password for. Then, click on the "Generate" button.

You can now update the `.env` file with your Gmail username and app password.

### Automation
You can automate emails at a designated frequency by creating a `.bat` file and using Windows Task Scheduler. The `.bat` file should look something like this:
```bat
@echo off
"Path where your Python exe is stored\python.exe" "Path where your Python script is stored\update_emails.py"
```
After creating the `.bat` file, you can automate using Windows Task Scheduler with the following steps:

1. Open the Start menu and type "Task Scheduler" into the search bar. Click on the Task Scheduler app to open it.
2. In the Task Scheduler window, click on the "Action" menu and select "Create Basic Task..." from the drop-down menu.
3. In the "Create Basic Task Wizard" window that appears, enter a name and description for the task and click on the "Next" button.
4. In the "Trigger" window, select the "Daily" option and set the task to run at your designated frequency. Then, click on the "Next" button.
5. In the "Action" window, select the "Start a program" option and click on the "Next" button.
6. In the "Start a Program" window, click on the "Browse..." button and navigate to the `.bat` file that you want to run. Then, click on the "Open" button.
7. Click on the "Next" button to proceed to the "Finish" window.
8. In the "Finish" window, review the task details and click on the "Finish" button to create the task.

You are ready to use the Notre Dame Class Search Tool!
