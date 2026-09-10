prompt = "Enter Radius Of Circle You Want To Find Area And Perimeter: "
radius = int(input(prompt))

pi = 3.14
area = pi * radius**2
perimeter = 2 * pi * radius

print(
    f"Area And Perimeter Of Circle With radius {radius} is\
       \nArea = {area:.2f} \nPerimeter is {perimeter:.2f}"
)
