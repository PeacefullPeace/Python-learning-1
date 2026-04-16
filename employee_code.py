first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
full_name = input("What's your first_name + ' ' + last_name?")
print(full_name)
address = input("Where do you live? ")
house_number = input("House number: ")
full_address = address + ", " + house_number
print(full_address)
employee_age = input("How old are you?")
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
experience_years = input("How experienced am i?")
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)
position = input("What position do i hold?")
salary = input("How much do i earn")
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
employee_code = input("What's my employee_code? ")
department = employee_code[0:3]
year_code = employee_code[4:8]
initials = employee_code[9:11]
print(f"Department: {department} | Year: {year_code} | Initials: {initials}")
