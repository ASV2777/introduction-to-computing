gross_income = int(input("Enter gross income = $"))
no_of_dependents = int(input("Enter no. of dependents = "))

standard_deduction = 10000
dependent_deduction = 3000
tax_rate = 0.2

taxable_income = gross_income - standard_deduction - (dependent_deduction * no_of_dependents)

tax = taxable_income * tax_rate

print("Tax is : $", tax)
