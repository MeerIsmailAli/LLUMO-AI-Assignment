you can try running locally and use the below endpoints to check



Sample Document Structure
{
"employee_id": "E123",
"name": "example",
"department": "electronics",
"salary": 75000,
"joining_date": "2023-01-15",
"skills": ["Python", "MongoDB", "APIs"]
}





section 2:

post  /employees
	validation //unique employee id
	
get /employees/{employee_id}
	fetch details , return 404 if error

put /employees/{employee_id}
	only on partial updates(provided fields)

delete /employees/{employee_id}
	success/failure message

section 3:

get /employees?department=Engineering
	return by sorting latest joined
get /employees/avg-salary
	use aggregations in mongodb

get /employees/search?skill=Python
