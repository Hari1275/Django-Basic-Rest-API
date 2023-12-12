from django.db import models

# Create your models here.
class Department(models.Model):
    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=100)

class Emp(models.Model):

    EmpId=models.AutoField(primary_key=True)
    EmpName=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    DateofJoin=models.DateField()
    Photo=models.CharField(max_length=100)