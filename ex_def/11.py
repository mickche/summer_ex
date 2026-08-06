def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info(name="Alice", age=30, city="New York")