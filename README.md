
# Assignment

a simple djangorestframework application with mongodb using mongoengine
You can try running locally and use the below endpoints to check.


Sample Document Structure:
{
  "employee_id": "E123",
  "name": "example",
  "department": "electronics",
  "salary": 75000,
  "joining_date": "2023-01-15",
  "skills": ["Python", "MongoDB", "APIs"]
}

## Section 2: CRUD Operations

POST /employees/

    Validation: unique employee id

GET /employees/{employee_id}/

    Fetch details, return 404 if not found

PUT /employees/{employee_id}/

    Only on partial updates (provided fields)

DELETE /employees/{employee_id}/

    Success/failure message

## Section 3: Additional Queries

GET /employees?department=Engineering

    Return employees sorted by latest joined

GET /employees/avg-salary/

    Use aggregations in MongoDB

GET /employees/search?skill=Python
GET /employees/avg-salary/

Use aggregations in MongoDB

GET /employees/search?skill=Python
