# Create a custom exception InvalidSalaryError
# Then write a function:
# •	Takes salary as input 
# •	Raises error if: 
# o	salary < 0 
# o	salary > 10000 
# •	Otherwise returns "Valid salary" 

class InvalidSalaryError(Exception):
    pass

def validate_salary(salary):
    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative")
    elif salary > 10000:
        raise InvalidSalaryError("Salary cannot exceed 10000")
    else:
        return "Valid salary"

# Example 
try:
    print(validate_salary(5000))
    print(validate_salary(-50))
except InvalidSalaryError as e:
    print("Error:", e)
