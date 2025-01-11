
def calculate_tax(income):
    tax = 0
    if income <= 250000:
        tax = 0
    elif 250001 <= income <= 500000:
        tax = (income - 250000) * 0.05
    elif 500001 <= income <= 1000000:
        tax = (income - 500000) * 0.2 + 250000 * 0.05
    else:
        tax = (income - 1000000) * 0.3 + 500000 * 0.2 + 250000 * 0.05
    return tax

try:
    print("...Calculating income tax...\n")  
    
    income = float(input("Enter your annual income (₹): "))
    
    tax_amount = calculate_tax(income)
    print(f"\nYour calculated tax is.... ₹{tax_amount:.2f}")
except ValueError:
    print("Invalid input! Please enter a numeric value.")
