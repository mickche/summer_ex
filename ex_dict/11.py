# Exercise 11: Check Value Existence
def check_roles(roles):
    print("'editor' exists as a value:", "editor" in roles.values())
    print("'manager' exists as a value:", "manager" in roles.values())
check_roles({"alice": "admin", "bob": "editor", "carol": "viewer"})
