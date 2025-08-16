# 1️⃣ Define your custom exception first
class TooYoungError(Exception):
    pass

# 2️⃣ Use try-except
try:
    age = int(input("Enter age: "))
    if age < 18:
        raise TooYoungError("Too young! ❌")
    
    print("ready to explore")
except TooYoungError as e:
    print(e)
