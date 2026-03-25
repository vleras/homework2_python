# Using lambda + filter:
# •	Return only numbers greater than 15
numbers = [5, 10, 15, 20, 25, 30]

def filter_numbers(numbers):
    if not numbers:
        return "Input list is empty"

    result = list(filter(lambda x: x > 15, numbers))

    if not result:
        return "No numbers greater than 15"
    
    return result
print(filter_numbers(numbers))