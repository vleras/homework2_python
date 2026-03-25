# Given:
values = ["12", "25", "error", "40", "None", "60"]
# Write code to:
# •	Convert valid numeric values to integers 
# •	Skip invalid entries 
# •	Return the cleaned list

def clean_values(values):
    if not values:
        return "List is empty"

    cleaned = []

    for v in values:
        if v.isdigit():
            cleaned.append(int(v))

    if not cleaned:
        return "No valid numbers"

    return cleaned


result = clean_values(values)
print(result)