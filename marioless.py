# sets parameters for acceptable input
while True:
    height = int(input("Height: "))
    if height > 0 and height <= 8:
        break
    else:
        print("Height must be a positive integer no greater than 8")

#nested for loop, follows grid pattern starting from top left
for row in range(0,height):
    for column in range(0,height):
        if (row + column < height - 1):
            print(" ", end="")
        else:
            print("#", end="")
    print()