# Class Search
![Notre Dame Logo Blue](https://user-images.githubusercontent.com/69359897/226090345-7d5c2192-f8dd-414b-abba-56f60442f7ed.png) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ![Notre Dame Logo Gold](https://user-images.githubusercontent.com/69359897/226090371-153ea336-68c6-429f-858a-bd094d1a37e4.png)

## Overview
- The Notre Dame Class Search Tool allows Notre Dame students to add and track different class sections from https://classsearch.nd.edu.  The user can add,  remove, or view class sections by running `main.py`.
- When the user adds a class section, the file `classes.txt` will be created or updated. After adding the class section, the user can recieve an email with status updates by running `update_classes.py`, which updates the number of seats in `classes.txt`. 
- `update_classes.py` can be automated on Unix-based systems with Cron, or on Windows-based systems with Task Scheduler.

## Setup
The following command will pull and install the latest commit from this repository:
```
$ git clone https://github.com/johnflanagan827/class-search.git
$ cd class-search
```
To install the dependencies, please run:
```
$ pip install -r requirements.txt
```

### App password
You will need to generate an app password, which is a special password that is designed for use with third-party applications such as Python scripts.  To turn on app passwords and generate an app password for a Google Account, you will need to follow these steps:

1. Go to your [Google Account](https://myaccount.google.com).
2. Search for **App passwords** in the search bar and select the first result.
3. Follow the prompt to enable app passwords. 
4. Click the **Select app** drop-down menu and select **Other**. Name the app password and click the **Generate** button.

You can now update the `.env` file with your Gmail username and app password.

## Example
Here is a GIF showing an example of how the class-search works in the terminal:

![class-search GIF](https://user-images.githubusercontent.com/69359897/226090065-29b5bdce-1c9a-440e-8dde-61ec7e18f99b.gif)

## About
The Notre Dame Class Search Tool uses [Selenium](https://www.selenium.dev/) 4.7.2 with [ChromeDriver](https://chromedriver.chromium.org/) to scrape data from https://classsearch.nd.edu.  The Python libraries [email](https://docs.python.org/3/library/email.html) and [ssl](https://docs.python.org/3/library/ssl.html) are used to securely send emails.  [Dotenv](https://www.npmjs.com/package/dotenv) is used to more securely store email usernames and passwords in the `.env` file.

*Note: Currently, email updates are only supported with Gmail.*

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

### What does this mean?

This means that you are free to use, modify, and distribute this software as long as you comply with the terms of the GPL v3.0 license. Some of the key terms include:

- You must include a copy of the license with any distribution of this software.
- Any modifications or derivative works based on this software must also be licensed under the GPL v3.0.
- You must give proper attribution to the original author of this software.
