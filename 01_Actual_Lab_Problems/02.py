prompt = "Enter Two Number You Want To Swap: "
print(prompt)

a = int(input())
b = int(input())

print(
    f"Currently\
     \n A has {a} and\
     \n B has {b}"
)

b, a = a, b  # Tuple Way of Kind of Swapping using unpacking and packing method

print(
    f"After Swapping\
      \n A Now Has {a}\
      \n B Now Has {b}"
)
