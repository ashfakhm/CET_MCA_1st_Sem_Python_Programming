# Program to display first and last colours from a comma-separated list
colours = input("Enter colours separated by commas: ")
colour_list = [color.strip() for color in colours.split(',') if color.strip()]

if colour_list:
    print("First colour:", colour_list[0])
    print("Last colour:", colour_list[-1])
else:
    print("No colours entered.")
