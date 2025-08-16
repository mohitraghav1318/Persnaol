#khud se value assing ki hai
# numbers = [1, 2, 3, 4, 7 , 9 ] 
# input from user
numbers = input("enter numbers (space separated): ").split()
# split() se string list banegi, example: ['1', '2', '3', '4']

numbers = list(map(int, input("enter numbers (space separated): ").split()))
print(numbers)


if (n := len(numbers)) > 5:
    print(numbers)
    print(f"List bahut badi hai, length = {n}")

else:
    print(numbers)
    print(f"list size = {n}")

