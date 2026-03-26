# 1. Invoice Processing
# You are given:
invoices = [
    {"invoice_id": 1, "amount": 150, "status": "paid"},
    {"invoice_id": 2, "amount": -30, "status": "paid"},
    {"invoice_id": 3, "amount": 200, "status": "pending"},
    {"invoice_id": 4, "amount": 100, "status": "paid"}
]
# Write a function that:
# •	Calculates total amount for each invoice (just use amount here) 
# •	Returns only valid invoices 
# Conditions:
# •	amount must be positive 
# •	status must be "paid"

def process_invoices(input):
    valid_invoices = []
    total_amount = 0

    for invoice in invoices:
        if invoice["amount"] > 0 and invoice["status"] == "paid":
            valid_invoices.append(invoice)
            total_amount += invoice["amount"]

    return f"Valid invoices: {valid_invoices},\nTotal amount: {total_amount}"


print(process_invoices(invoices))
