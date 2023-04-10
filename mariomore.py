# sets parameters for acceptable ints
while True:
    height = int(input("Height: "))
    if height > 0 and height <= 8:
        break
    else:
        print("Height must be a positive int no greater than 8")

#nested for loop, follows grid pattern starting from top left
'''
Three conditions determine when to print a space " ".
1. column == height
2. column == height = 1
3. row + column < height - 1

1 and 2 produce "double space" column between pyamids
3 produces spaces before pyramid
'''
for row in range(0,height):
    for column in range(0,height + row + 3): #derrived upper limit of range from (height + row + 2 = columns)
        if (column == height or column == height + 1 or row + column < height - 1): 
            print(" ", end="")
        else:
            print("#", end="")
    print()