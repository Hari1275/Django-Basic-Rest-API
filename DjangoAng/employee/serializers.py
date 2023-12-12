from rest_framework import serializers
from employee.models import Department,Emp

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=('DepartmentId','DepartmentName')

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields=('EmpId','EmpName','Department','DateofJoin','Photo')