# Exercise 13: Extract Subset of Keys

def subset(user,keys_to_keep):
    return {k: user[k] for k in keys_to_keep}

print(subset({"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"},["id", "username", "email"]))
