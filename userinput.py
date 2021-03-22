# sudo coding

# Using the function input() to get this details from the User by the interpreter:

# The first name:
first_name = input("Please enter your first name: ")

# The last name:
last_name = input("Please enter your last name: ")

# The age name:
age = input("Please enter your age: ")

# The salary name:
salary = input("Please enter your salary: ")

# The date of birth name:
date_birth = input("Please enter your date of birth: ")

# The post code name:
post_code = input("Please enter your post code: ")

# Print the type of each data type that we have received from the customer.
# We use the function type

print("The type of the data first name is: ")
print(type(first_name))
print("The type of the data last name is: ")
print(type(last_name))
print("The type of the data age is: ")
print(type(age))
print("The type of the data salary is: ")
print(type(salary))
print("The type of the data date of birth is: ")
print(type(date_birth))
print("The type of the data post code is: ")
print(type(post_code))

# To convert the data age from String to int we use the function int()
# Casting is when you convert a variable value from one type to another

age = int(age)
print("The type of the data age after converting is: ")
print(type(age))
