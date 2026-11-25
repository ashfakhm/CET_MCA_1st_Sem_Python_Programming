"""
Writing to a CSV file and opening it to read the contents.
"""

import csv

file_name = "sample.csv"

# Create the file and write some rows.
with open(file_name, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Ashfakh", 22, "Malappuram"])
    writer.writerow(["Abhinav", 22, "Kasargode"])
    writer.writerow(["Arun Jacob", 22, "Kochi"])

# Open the CSV file in read mode and display its rows.
with open(file_name, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(", ".join(row))
