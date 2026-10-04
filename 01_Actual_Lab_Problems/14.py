# Program to sort a dictionary in ascending and descending order
student = {
    "Name": "Ashfakh",
    "Gender": "M",
    "Phone": None,
    "Age": 22,
}

# Sort by keys
ascending = dict(sorted(student.items(), key=lambda x: x[0]))
descending = dict(sorted(student.items(), key=lambda x: x[0], reverse=True))

print("Ascending order:", ascending)
print("Descending order:", descending)
