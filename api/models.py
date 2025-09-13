# Sample Document Structure
# {
# "employee_id": "E123",
# "name": "John Doe",
# "department": "Engineering",
# "salary": 75000,
# "joining_date": "2023-01-15",
# "skills": ["Python", "MongoDB", "APIs"]
# }


import mongoengine

class Employee(mongoengine.Document):
    employee_id = mongoengine.StringField(required=True, unique=True)
    name = mongoengine.StringField(required=True)
    department = mongoengine.StringField()
    salary = mongoengine.FloatField()
    joining_date = mongoengine.DateField()
    skills = mongoengine.ListField(mongoengine.StringField())

    meta = {"collection": "employees"} 
    