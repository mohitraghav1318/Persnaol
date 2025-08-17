def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# show_info(name="Mohit", age=22, city="Meerut")
# Output:
# name: Mohit
# age: 22
# city: Meerut

show_info(language="Python", level="Beginner")
# Output:
# language: Python
# level: Beginner
# taking input from user
user_input = input("Enter your details (key=value pairs, space separated): ")
# Convert input string to dictionary
user_details = dict(item.split("=") for item in user_input.split()) 
show_info(**user_details)
# Example input: name=John age=30 city=NewYork
# Output:
# name: John    
# age: 30
# city: NewYork