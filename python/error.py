try:
    # risky code
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    print(x / y)
except ValueError:
    print("That's not a number! 😅")
except ZeroDivisionError:
    print("Cannot divide by zero! 😬")
except Exception as e:  # catches any other error
    print("Something went wrong:", e)
finally:
    print("This always runs! ✅")
