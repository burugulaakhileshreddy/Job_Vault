from django.db import models
from django.contrib.auth.models import User

class Internships(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='internships',null=False,default='default@gmail.com')
    Company_Name = models.CharField(max_length=200)
    Date = models.DateField()
    Platform = models.CharField(max_length=200)
    Resume = models.FileField(upload_to='documents/Job_Vault/')
    Cover_Letter = models.FileField(upload_to='documents/Job_Vault/')
    Link = models.CharField(max_length=600)
    Notes = models.TextField()

    def __str__(self):
        return self.Company_Name


class Full_Time(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='full_time',null=False,default='default@gmail.com')
    Company_Name = models.CharField(max_length=200)
    Date = models.DateField()
    Platform = models.CharField(max_length=200)
    Resume = models.FileField(upload_to='documents/Job_Vault/')
    Cover_Letter = models.FileField(upload_to='documents/Job_Vault/')
    Link = models.CharField(max_length=600)
    Notes = models.TextField()

    def __str__(self):
        return self.Company_Name


class C2C(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c2c',null=False,default='default@gmail.com')
    Company_Name = models.CharField(max_length=200)
    Date = models.DateField()
    Platform = models.CharField(max_length=200)
    Resume = models.FileField(upload_to='documents/Job_Vault/')
    Cover_Letter = models.FileField(upload_to='documents/Job_Vault/')
    Link = models.CharField(max_length=600)
    Notes = models.TextField()

    def __str__(self):
        return self.Company_Name


class W2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='w2',null=False,default='default@gmail.com')
    Company_Name = models.CharField(max_length=200)
    Date = models.DateField()
    Platform = models.CharField(max_length=200)
    Resume = models.FileField(upload_to='documents/Job_Vault/')
    Cover_Letter = models.FileField(upload_to='documents/Job_Vault/')
    Link = models.CharField(max_length=600)
    Notes = models.TextField()

    def __str__(self):
        return self.Company_Name

class Portfolios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Portfolio_Name = models.CharField(max_length=200)
    Portfolio = models.FileField(upload_to='documents/Job_Vault/')
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Portfolio_Name




