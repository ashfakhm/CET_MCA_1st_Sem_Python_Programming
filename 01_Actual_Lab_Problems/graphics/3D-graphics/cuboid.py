"""Surface area and total edge length calculations for a cuboid."""


def area(length, breadth, height):
    return 2 * (
        length * breadth + length * height + breadth * height
    )


def perimeter(length, breadth, height):
    return 4 * (length + breadth + height)
