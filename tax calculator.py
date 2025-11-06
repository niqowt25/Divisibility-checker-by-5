def tax_calculator():
    income = float(input("Enter your income: "))

    if income <= 1000:
        tax = income * 0.05
    elif income <= 5000:
        tax = income * 0.10
    else:
        tax = income * 0.15

    print("Tax:", tax)
    print("Net income:", income - tax)

tax_calculator()
