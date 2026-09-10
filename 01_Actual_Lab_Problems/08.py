num = int(input("Enter The Number You Want To Find The Count Of Digits: "))
orginal_num = num
count = 0


while num > 0:
    count += 1
    num = num // 10

print(f"The Number Of Digits in {orginal_num} is {count} ")
