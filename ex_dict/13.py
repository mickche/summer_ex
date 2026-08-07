# Exercise 13: Extract Subset of Keys

user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}
keys_to_keep = ["id", "username", "email"]

subset = {k: user[k] for k in keys_to_keep}
print(subset)
