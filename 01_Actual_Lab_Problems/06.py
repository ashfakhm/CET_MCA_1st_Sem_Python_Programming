count = 0
i = 1
sum = 0

while count < 100:
    if i % 2 == 0:
        sum += i
        count += 1
    i += 1

print(f"Sum Of First 100 Even Numbers Are {sum}")
