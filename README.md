# web_scrapping_using_selenium

Extracting job information from LinkedIn Jobs using Selenium.
The goal of this project is to scrape job postings and related information from LinkedIn.
After running the below code, we will get the following information about the job posting:

Job Title </br>
Company Name </br>
Location </br>

### How to run application in your system:
1. Create virtual environment in the root directory by using.
   > py -m venv env
2. Now activate the virtual environment by using.
   > env/Scripts/activate
   (this should activate the virtual environment on your system)
3. Install all the dependencies.
   All the dependencies which project requires are consolidated in requirements.txt file, so to install them simply use.
   > pip install -r requirements.txt
4. Now finally run the application by using following command.
   > python manage.py runserver
   (and you should see the app in action on http://localhost:8000/)
   
#### For getting the scrapped details:
     Enter your linkedin credentials in the form to see the scrapped data. 
     Don't worry! This application does not save any credentials
