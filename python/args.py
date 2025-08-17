def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum is:", total)

sum_numbers(4, 5, 6)
# Output: Sum is: 15

#taking input from user
numbers = input("Enter numbers (space separated): ").split()
# Convert input strings to integers
numbers = list(map(int, numbers))
sum_numbers(*numbers)
# Output: Sum is: <calculated sum>  
# Example: Enter numbers (space separated): 1 2 3 4
# Output: Sum is: 10
