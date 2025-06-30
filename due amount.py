cost_of_bill = 1000
amount_paid = int(input("Enter the amount paid: "))

if amount_paid < cost_of_bill:
    due_amount = cost_of_bill - amount_paid
    print("The due amount is:", due_amount)
elif amount_paid == cost_of_bill:
    print("No due amount.")
else:
    extra = amount_paid - cost_of_bill
    print("Sir, you have paid extra:", extra)
    # This code calculates the due amount by subtracting the amount paid from the total cost of the bill.
# It then prints the due amount to the console.
# Ensure that the cost of the bill and the amount paid are defined before running this code.
# This is a simple calculation and does not involve any complex logic or error handling.