for i in range(1, 12):
    for j in range(1, 12):
        if (i==1 and j>6) or i==6 or (i==11 and j<6) or (j==1 and i<6) or j==6 or (j==11 and i>6):
            print("*", end="  ")
        elif (i==3 and j==3) or (i==3 and j==9) or (i==9 and j==3) or (i==9 and j==9):
            print("*", end="  ")
        else:
            print("  ", end=" ")
    print()