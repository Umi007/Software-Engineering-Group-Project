Zero Footprint Web Application Description
==========================================
Table of Contents
------------------
* [Background](#background)
* [Install](#install)
* [Important Information](#important-information)
* [Project Structure](#project-structure)
* [Licence](#licence)
------------------
Background 
------------------
This project is a web application to educate our target group, which usually 
is older children and young adults (13-25), of their affect on the environment
and the problems the world currently faces, and hopefully help them mitigate 
their impact.

------------------
Install
------------------
### Config Python Interpreter
* The app should be run in either `python 3.9` or `python 3.8`
### Setting Application Configuration
  * Before you running the code, you should add a new configuration for this web app.
    * Go to your `pycharm menu`, should be on the top
    * Select `Run > Edit Configuration`
    * Add a new python configuration and set the script path for `app.py`
    * Click `Apply` and then `OK`
  * Set up connection with database
    * The default connection option is off-campus one. If you are on-campus please 
    follow the instruction below. Or if the unexpect SSH error occur, 
    please follow the local set up instruction.
        * Off-campus
          * `Resoureces>`env`>`setting.csv`
          * Please fill in you account and password for linux computer
        * On-campus
          * `Resoureces`>`config.py`
          * Comment out `line 22-47` and `line 61-77`
          * Uncomment `line 50-51`
          * Go to `app.py`
          * Comment out `line 15` and `line 105`
        * Local set up
          * `Resoureces`>`config.py`
          * Comment out `line 22-47` and `line 62-77`
          * Uncomment `line 54`
          * Go to `app.py`
          * Comment out `line 15` and `line 105`
          * Go to `Python Console`
          * Type the following code
            * `from models import init_db`
            * `init_db()`
### Dependencies Install
* Option 1
  * Go to 'Terminal'
  * Type in `pip install -r requirement.txt`, make sure you are in the main project directory.
* Option 2:
  * Find and open the `requirement.txt` in pycharm in the main directory of the project.
  * The information in yellow will show at the top, select `install requirement`
* Instruction of handling possible installing error 
  * `Crypto` package cannot find error
    * Go to the directory of your project in your system directory
    * Check whether the directory have a file called `Crypto` or `crypto`
    * If the file is named `crypto`, change it to `Crypto`
### Project Structure Set-up Reminder
* Please check whether the `Resources` directory is marked as `Source folder`, colored in blue.   
If not, go to pycharm `setting`, `preference` in Mac, > `Project` >`Project Structure`.
Choose the folder and mark as `Sources`.
* Please check whether the `templates` directory is marked as `Templates folder`, colored in purple.   
If not, go to pycharm `setting`, `preference` in Mac, > `Project` >`Project Structure`.
Choose the folder and mark as `Templates`.
------------------
Important Information
------------------
* If you register in the app, the role of your account is default as user.
If you want to log in as admin to see what is going on in admin page, we 
have provided a test admin account which you can login to get the security 
code to log into our app.
  * email:`zerofooprint@outlook.com`
  * password: `Admin1!`(for our app)
  * email password: `Hi_Fi_team05`(for email, to get the security code)
------------------
Project Structure
------------------
.<br>
├── README.md `help` <br>
├── Resources <br>
│   ├── RBAC.py `Role Bases Access Control`<br>
│   ├── account_info.csv `Initail account information`<br>
│   ├── admin_accounts.csv `Initail account for admin`<br>
│   ├── auto_import.py `Automatic import data into database`<br>
│   ├── config.py `Database connection setting`<br>
│   ├── env<br>
│   │   ├── setting.env `Database account setting`<br>
│   │   └── teamemail.env `Team email account information`<br>
│   ├── post.csv <br>
│   ├── quizQuestions.csv<br>
│   └── verification.py<br>
├── admin `Some forms and functions about admin page`<br>
├── app.py <br>
├── calculator `Some forms and functions about calculator page`<br>
├── carbon.log `Security log`<br>
├── carbongram `Some forms and functions about social fucntion`<br>
├── forum<br>
├── information<br>
├── models.py `Database tables`<br>
├── quiz `Some functions about quiz fucntion`<br>
├── requirements.txt `Dependencies`<br>
├── static <br>
│   ├── carbongramMain.js<br>
│   ├── css<br>
│   │   └── style.css<br>
│   ├── img<br>
│   ├── main.js<br>
│   └── quiz.js<br>
├── templates `HTML`<br>
└── users `Some forms and functions about user fucntion`<br>
------------------
Licence
------------------
Copyright, 2022, Newcastle University

  
