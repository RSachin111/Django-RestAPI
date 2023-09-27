from django.db import models

# Create your models here.

# Comnpany model
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(
        ('IT','IT'),
        ('Non IT', 'Non IT')
        ))
    added_date= models.DateField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name +'-'+ self.location

#Employee Model
class Employee(models.Model):
    name =models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=100)
    number=models.IntegerField()
    position=models.CharField(max_length=50,choices=(
        ('Manager','Manager'),
        ('Software Developer','SD'),
        ('Project Leader','PL'),
        ))

    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    

   