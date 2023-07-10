from django.db import models

# Create your models here.
class Job(models.Model) :
    job_id = models.IntegerField()
    job_role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    post_date = models.DateTimeField()
    posted = models.BooleanField(default=False)

    def __str__(self):
        return self.job_role + ', ' + self.company

class Person(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    address=models.TextField(max_length=100)
    phone=models.CharField(max_length=12)
    about=models.TextField(max_length=100)
    position=models.CharField(max_length=50, choices=(
        ("Manager", "manager"),
        ("Software Developer", "SDE"),
        ("Security Analyst", "SE")
    )),
    job_applied=models.ForeignKey(Job, on_delete=models.CASCADE)