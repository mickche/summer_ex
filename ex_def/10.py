def describe_pet(animal_type, pet_name):
    return f"У мене є {animal_type}\nМого {animal_type} звуть {pet_name}"

print(describe_pet("hamster", "Harry"))
print(describe_pet(animal_type="dog", pet_name="Willie"))

