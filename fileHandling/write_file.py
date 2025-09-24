# with open("data.txt", "w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a test file.\n")
#     file.write("Writing to files in Python is easy!\n")
#     file.write("Goodbye, World!\n")
# print("Data written to file successfully.")

# Input from user
name = input("Enter your name: ")
age = input("Enter your age: ")
with open("data1.txt", "a") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")