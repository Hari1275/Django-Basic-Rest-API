from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from employee.models import Department,Emp
from employee.serializers import DepartmentSerializer,EmpSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        department=Department.objects.all()
        department_seralizer=DepartmentSerializer(department,many=True)

        return JsonResponse( department_seralizer.data, safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        dept_seralizer=DepartmentSerializer(data=department_data)
        if dept_seralizer.is_valid():
            dept_seralizer.save()
            return JsonResponse("added sucussfully",safe=False)
        return JsonResponse("added failed",safe=False)
             

    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Department.objects.get(DepartmentId=department_data['DepartmentId'])
        dept_seralizer=DepartmentSerializer(department,data=department_data)
        if dept_seralizer.is_valid():
            dept_seralizer.save()
            return JsonResponse("update sucussfully",safe=False)
        return JsonResponse("update failed",safe=False)

    elif request.method=='DELETE':
        department=Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("delete sucussfully",safe=False)
        return JsonResponse("delete failed",safe=False)

# //////////

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employee=Emp.objects.all()
        employee_seralizer=EmpSerializer(employee,many=True)

        return JsonResponse( employee_seralizer.data, safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        dept_seralizer=EmpSerializer(data=employee_data)
        if dept_seralizer.is_valid():
            dept_seralizer.save()
            return JsonResponse("added sucussfully",safe=False)
        return JsonResponse("added failed",safe=False)
             

    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Emp.objects.get(EmpId=employee_data['EmpId'])
        dept_seralizer=EmpSerializer(employee,data=employee_data)
        if dept_seralizer.is_valid():
            dept_seralizer.save()
            return JsonResponse("update sucussfully",safe=False)
        return JsonResponse("update failed",safe=False)

    elif request.method=='DELETE':
        employee=Emp.objects.get(EmpId=id)
        employee.delete()
        return JsonResponse("delete sucussfully",safe=False)
        return JsonResponse("delete failed",safe=False)





#/////

@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']

    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)