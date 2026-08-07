# Exercise 16: Modify Nested Dictionary

def func(d):
    d_nested = d['location']
    d_nested.update({'city': 'Munich',})
    return d

print(func({"name": "TechCorp", "location": {"city": "Berlin", "country": "Germany"}}))


