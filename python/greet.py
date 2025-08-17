import argparse

parser = argparse.ArgumentParser(description="Greet a user!")
parser.add_argument("name", help="User's name")
parser.add_argument("--age", type=int, help="User's age", default=None)

args = parser.parse_args()
 
if args.age:
    print(f"Hello, {args.name}! You are {args.age} years old.")
else:
    print(f"Hello, {args.name}!")
# No age provided, just greeting by name.