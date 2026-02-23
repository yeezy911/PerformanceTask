def budget(expenses):
    total = 0
    food_total = 0
    fun_total = 0
    other_total = 0

    # Iteration through list
    for item in expenses:
        total += item[1]

        # Selection based on category
        if item[0].lower() == "food":
            food_total += item[1]
        elif item[0].lower() == "fun":
            fun_total += item[1]
        else:
            other_total += item[1]

    # The output depends on the input
    print("\nTotal Spending: $", total)
    print("Food: $", food_total)
    print("Fun: $", fun_total)
    print("Other: $", other_total)

    # Different path based on total
    if total > 150:
        print("Warning: You spent over $150!")
    else:
        print("Good job staying under 150!")

# Creates an empty set which will store expenses
expenses = []

while True:
    category = input("Enter category (food, fun, other) or 'done' to finish: ")

    if category.lower() == "done":
        break

    amount = float(input("Enter amount spent: "))

    # Adds a new item to the list
    expenses.append([category, amount])

# Calling function with parameter
budget(expenses)