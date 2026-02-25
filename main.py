def budget(expenses):
    total = 0
    food_total = 0
    fun_total = 0
    other_total = 0

    for item in expenses:
        total += item[1]

        if item[0].lower() == "food":
            food_total += item[1]
        elif item[0].lower() == "fun":
            fun_total += item[1]
        else:
            other_total += item[1]

    print("\nTotal Spending: $", total)
    print("Food: $", food_total)
    print("Fun: $", fun_total)
    print("Other: $", other_total)

    if total > 150:
        print("Warning: You spent over $150!")
    else:
        print("Good job staying under 150!")

expenses = []

while True:
    category = input("Enter category (food, fun, other) or 'done' to finish: ")

    if category.lower() == "done":
        break

    amount = float(input("Enter amount spent: "))

    expenses.append([category, amount])

budget(expenses)
