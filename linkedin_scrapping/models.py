from django.db import models


class JobPosts(models.Model):
    job_title = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    job_location = models.CharField(max_length=50)
