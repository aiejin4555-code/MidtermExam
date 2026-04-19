#Kassandra Faye Llagas
#BSIT SE 1A

print("==========================================")
print("        STUDENT -- INFORMATION            ")
print("==========================================")
print(" ")

while True:
    studentNameInput = input("Student name: ")
    if studentNameInput.replace(" ", "").isalpha():
        inputed_name = studentNameInput.strip().title()
        break
    print("Please try again! Any special character or numbers are not allowed.")

while True:
    budgetInput = input("Weekly budget: ")
    if budgetInput.replace(".", "", 1).isdigit():
        inputed_budget = float(budgetInput)
        if inputed_budget > 0:
            break
        else:
            print("Error: Budget must be greater than zero.")
    else:
        print("Error: Please enter a valid number for the budget.")

categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]
expense_category = [
    "Lunch, snacks, coffee",
    "Bus, jeepney, ride-share",
    "Load, data plan, WiFi top-up",
    "Notebook, pen, bond paper",
    "Games, movies, hangout"
]

print(" ")
print("==========================================")
print("    WEEKLY EXPENSE -- CATEGORIES          ")
print("==========================================")
counter = 1
for category in categories:
    print(f" {counter}. {category:<18} [e.g. {expense_category[counter-1]}]")
    counter = counter + 1
print("==========================================")

expenses_list = []
total_spent = 0

for expense_entry_num in range(1, 6):
    print(" ")
    print(f"--- EXPENSE {expense_entry_num} ---")

    while True:
        categoryInput = input("Select Category (0 to skip): ")
        if categoryInput.isdigit():
            category_num = int(categoryInput)
            if 0 <= category_num <= 5:
                break
            else:
                print("Error: Selection must be between 0 and 5.")
        else:
            print("Error: Please enter a valid numeric category.")

    if category_num == 0:
        print("Entry skipped.")
        continue
    elif 1 <= category_num <= 5:

        while True:
            inputed_description = input("Description: ")
            if inputed_description.strip() != "":
                inputed_description = inputed_description.strip()
                break
            print("Error: Description is required.")

        while True:
            amountInput = input("Amount: ")
            if amountInput.replace(".", "", 1).isdigit():
                amount = float(amountInput)
                if amount >= 0:
                    break
                else:
                    print("Error: Amount cannot be negative.")
            else:
                print("Error: Please enter a valid number for the amount.")

        tag = ""
        if amount > (inputed_budget * 0.25):
            tag = " [High Expense Alert!]"

        expenses_list.append({
            "category": categories[category_num - 1],
            "description": inputed_description,
            "amount": amount,
            "tag": tag
        })

        total_spent = total_spent + amount

    else:
        print("Invalid category selected. Entry skipped.")

remaining_balance = inputed_budget - total_spent
if remaining_balance >= 0:
    status = "Budget OK. Keep it up!"
else:
    status = "Overspent. Reduce spending!"

print(" ")
print("======================================================")
print(f"      {inputed_name.upper()} -- WEEKLY EXPENSE LOG")
print("======================================================")
print(f"  Weekly Budget  : P{inputed_budget}")
item_number = 1
for item in expenses_list:
    print(f"  [{item_number}] {item['category']}")
    print(f"      {item['description']} P{item['amount']}  {item['tag']}")
    item_number = item_number + 1
print("------------------------------------------------------")
print(f"  Total Spent    : P{total_spent}")
print(f"  Remaining      : P{remaining_balance}")
print(f"  Status         : {status}")
print("======================================================")