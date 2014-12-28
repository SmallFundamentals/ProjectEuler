def main():
    lines = [line.strip().split() for line in open('input.txt')]

    for row in range(20):
        for col in range(20):
            lines[row][col] = int(lines[row][col])

    maxProduct = 0
    allProduct = []
    
    # Horizontal -
    for row in range(20):
        for col in range(20-4):
            allProduct.apppend(lines[row][col] * lines[row][col+1] * lines[row][col+2] * lines[row][col+3])
            if maxProduct < lines[row][col] * lines[row][col+1] * lines[row][col+2] * lines[row][col+3]:
                print("OVERTAKEN. \n CURRENT = " + str(maxProduct))
                maxProduct = lines[row][col] * lines[row][col+1] * lines[row][col+2] * lines[row][col+3]
                print(" NEW = " + str(maxProduct))
                direction = 0
                startIndex = [row, col]

    # Vertical |
    for col in range(20):
        for row in range(20-4):
            allProduct.apppend(lines[row][col] * lines[row+1][col] * lines[row+2][col] * lines[row+3][col])
            if maxProduct < lines[row][col] * lines[row+1][col] * lines[row+2][col] * lines[row+3][col]:
                print("OVERTAKEN. \n CURRENT = " + str(maxProduct))
                maxProduct = lines[row][col] * lines[row+1][col] * lines[row+2][col] * lines[row+3][col]
                print(" NEW = " + str(maxProduct))
                direction = 1
                startIndex = [row, col]

    # Diagonal \
    for row in range(20):
        for col in range(20):
            if row > 16 or col > 16:
                continue
            allProduct.apppend(lines[row][col] * lines[row+1][col+1] * lines[row+2][col+2] * lines[row+3][col+3])
            if maxProduct < lines[row][col] * lines[row+1][col+1] * lines[row+2][col+2] * lines[row+3][col+3]:
                print("OVERTAKEN. \n CURRENT = " + str(maxProduct))
                maxProduct = lines[row][col] * lines[row+1][col+1] * lines[row+2][col+2] * lines[row+3][col+3]
                print(" NEW = " + str(maxProduct))
                direction = 2
                startIndex = [row, col]
            else:
                print("DIAGONAL \\ :  \n " + str(lines[row][col] * lines[row+1][col+1] * lines[row+2][col+2] * lines[row+3][col+3]) + " is less than " + str(maxProduct))

    # Diagonal /
    for row in range(20):
        for col in range(20):
            if row < 3 or col < 3:
                continue
            allProduct.apppend(lines[row][col] * lines[row-1][col-1] * lines[row-2][col-2] * lines[row-3][col-3])
            if maxProduct < lines[row][col] * lines[row-1][col-1] * lines[row-2][col-2] * lines[row-3][col-3]:
                print("OVERTAKEN. \n CURRENT = " + str(maxProduct))
                maxProduct = lines[row][col] * lines[row-1][col-1] * lines[row-2][col-2] * lines[row-3][col-3]
                print(" NEW = " + str(maxProduct))
                direction = 3
                startIndex = [row, col]
            else:
                print("DIAGONAL / : \n " + str(lines[row][col] * lines[row-1][col-1] * lines[row-2][col-2] * lines[row-3][col-3]) + " is less than " + str(maxProduct))

    print(maxProduct)
    print("Direction = " + str(direction))    
    print("Index = " + str(startIndex))
    
main()
