# Exercise 12: Sum All Values
def func(expenses:dict[str]) -> int:
    return sum([i for i in expenses.values()])

print(func({"rent": 1200, "food": 300, "transport": 150, "utilities": 200}))



#2

# expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}

# total = sum(expenses.values())
# print("Total expenses:", total)