first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name #String concatenation
address = '123 Main Street'
address += ', Apartment 4B' #String concatenation using += operator
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old' #String concatenation with type conversion using str() function with a string
print(employee_info)
years_experience = 5
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years' #String concatenation with type conversion using str() function with an integer
print(experience_info)
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}' #String formatting using f-string with variables embedded in the string
print(employee_card)
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3] #String slicing to extract department code from employee code
print(department)
year_code = employee_code[4:8] #String slicing to extract year code from employee code
print(year_code)
initials = employee_code[9:11] #String slicing to extract initials from employee code
print(initials)
last_three = employee_code[-3:] #String slicing to extract the last three characters from employee code using negative indexing
print(last_three)