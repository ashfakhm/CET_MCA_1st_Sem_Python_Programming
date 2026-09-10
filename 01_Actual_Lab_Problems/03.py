prompt = "Enter Three Numbers You Want To Find The Largest Of Three"
print(prompt)

first = int(input())
second = int(input())
third = int(input())

print(f"You Typed {first}, {second}, {third}")

if first == second == third:
    print(f"{first} = {second} = {third}, i.e. No Largest")
elif first >= second and first >= third:
    print(f"{first} is Largest")
elif second >= first and second >= third:
    print(f"{second} is Largest")
else:
    print(f"{third} is Largest")
