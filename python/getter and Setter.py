
class Student:
    def __init__(self, name):
        self.name = name  # goes through setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value): # 💖 Setter
        if value.strip() == "":
            print("Name can't be empty 😡")
            self._name = "Unknown"  # 👈 SET kar rahe hain, compare nahi
        else:
            self._name = value
# User input
name_input = input("Enter your name: ")
s1 = Student(name_input)

print(f"Hello , {s1.name}")
