# Exercise 12: Sum All Values
def sum_of_values(expenses:dict[str]) -> int:
    return sum(list(expenses.values()))

print(sum_of_values({"rent": 1200, "food": 300, "transport": 150, "utilities": 200}))



#2

# expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}

# total = sum(expenses.values())
# print("Total expenses:", total)