"""
Writing to a text file and opening it to read the contents.
"""

file_name = "sample.txt"

# Create the file and write some text to it.
with open(file_name, "w", encoding="utf-8") as file:
    file.write("This Message Is For Kaantha:\n")
    file.write("Hello Iam Tiger Muthuvel Pandian.\n")
    file.write("Good Morning.\n")
    file.write("Good Afternoon.\n")
    file.write("Good Night.\n")

# Open the file in read mode and read all of its contents.
with open(file_name, "r", encoding="utf-8") as file:
    contents = file.read()

print(contents)
