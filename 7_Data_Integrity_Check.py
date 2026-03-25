

# Validate:
# • id must not be None
# • name must not be empty
# • salary must be positive

# Return:
# • invalid records
# • reason for each issue

employees = [
{"id": 1, "name": "Alice", "salary": 700},
{"id": 2, "name": "", "salary": 500},
{"id": 3, "name": "Bob", "salary": -200},
{"id": None, "name": "Eve", "salary": 900}
]

def validate_employees(employees):
    if not employees:
        return "No data provided"

    invalid_records = []

    for emp in employees:
        reasons = []

        if emp["id"] is None:
            reasons.append("ID is missing")

        if not emp["name"]:
            reasons.append("Name is empty")

        if emp["salary"] <= 0:
            reasons.append("Salary must be positive")

        if reasons:
            invalid_records.append({
                "employee": emp,
                "issues": reasons
            })

    return invalid_records

print(validate_employees(employees))