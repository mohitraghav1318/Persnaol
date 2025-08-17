# # with open("Persnaol/python/files.py", "w") as file:
# #     file.write("print('Hello, World!')\n")
    
# #     print("File 'files.py' created successfully with a simple print statement.")

# with open("Persnaol/python/file.txt", "r") as f:
#     print(f.read())                # Full text
#     f.seek(0)                      # Move cursor to start for next example
#     print(f.readline())            # First line only
#     f.seek(0)
#     print(f.readlines())           # List of all lines


# with open("myfile.txt", "w") as f:
#     f.write("First line\n")
#     f.write("Second line\n")


try:
    with open("random.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
