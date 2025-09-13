from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

# ------------------------------
# GET: list employees (optionally by department)
# POST: create new employee
# ------------------------------
@api_view(["GET", "POST"])
def employees(request):
    if request.method == "GET":
        department = request.GET.get("department")
        if department:
            employees_qs = Employee.objects(department=department).order_by("-joining_date")
        else:
            employees_qs = Employee.objects.all().order_by("-joining_date")
        serializer = EmployeeSerializer(employees_qs, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            if Employee.objects(employee_id=serializer.validated_data["employee_id"]).first():
                return Response(
                    {"error": "Employee ID must be unique"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            employee = Employee(**serializer.validated_data)
            employee.save()
            return Response(EmployeeSerializer(employee).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------
# GET / PUT / DELETE single employee
# ------------------------------
@api_view(["GET", "PUT", "DELETE"])
def employee_detail(request, employee_id):
    try:
        employee = Employee.objects.get(employee_id=employee_id)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            employee.update(**serializer.validated_data)
            updated_employee = Employee.objects.get(employee_id=employee_id)
            return Response(EmployeeSerializer(updated_employee).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        employee.delete()
        return Response(
            {"message": f"Employee {employee_id} deleted successfully"},
            status=status.HTTP_200_OK
        )

# ------------------------------
# GET average salary by department
# ------------------------------
@api_view(["GET"])
def avg_salary_by_department(request):
    pipeline = [
        {"$group": {"_id": "$department", "avg_salary": {"$avg": "$salary"}}},
        {"$project": {"_id": 0, "department": "$_id", "avg_salary": 1}}
    ]
    result = list(Employee.objects.aggregate(*pipeline))
    return Response(result)

# ------------------------------
# GET search employees by skill
# ------------------------------
@api_view(["GET"])
def search_by_skill(request):
    skill = request.GET.get("skill")
    if not skill:
        return Response({"error": "Please provide a skill"})
    
    employees_qs = Employee.objects(skills=skill)
    serializer = EmployeeSerializer(employees_qs, many=True)
    return Response(serializer.data)
