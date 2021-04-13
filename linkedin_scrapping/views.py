from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .models import JobPosts


def index(request):
    return render(request, 'index.html')


def jobs(request):
    if request.method == 'POST':
        JobPosts.objects.all().delete()
        browser = webdriver.Chrome("chromedriver.exe")
        browser.get("https://www.linkedin.com")
        
        username = browser.find_element_by_id("session_key")
        username.send_keys(request.POST.get('email',''))
        password = browser.find_element_by_id("session_password")
        password.send_keys(request.POST.get('password',''))
        
        login_button = browser.find_elements_by_class_name("sign-in-form__submit-button")[0]
        login_button.click()
        
        browser.get("https://www.linkedin.com/jobs/")
        
        # for job title
        jobs = browser.find_elements_by_class_name("job-card-square__title")
        title=[]
        for job in jobs:
            title.append(job.text)
            
        # for company name
        jobs = browser.find_elements_by_class_name("job-card-container__company-name")
        comp_name=[]
        for job in jobs:
            comp_name.append(job.text)
            
        # for job location
        jobs = browser.find_elements_by_class_name("job-card-container__metadata-item")
        job_loc=[]
        for job in jobs:
            job_loc.append(job.text)
            
        for i in range (0, len(comp_name)):
            job = JobPosts()
            job.job_title = title[i]
            job.company_name = comp_name[i]
            job.job_location = job_loc[i]
            job.save()
            
        job = JobPosts.objects.all()
        return render(request, 'jobs.html', {'jobs':job})


