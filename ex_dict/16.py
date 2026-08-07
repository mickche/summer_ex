# Exercise 16: Modify Nested Dictionary

def chenge_nested_key(d):
    d_nested = d['location']
    d_nested.update({'city': 'Munich',})
    return d

print(chenge_nested_key({"name": "TechCorp", "location": {"city": "Berlin", "country": "Germany"}}))


