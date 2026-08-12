for i in range(1, 12):
    for j in range(1, 12):
        if i == 6 or j == 6:
            print("*", end="  ")
        else:
            print("  ", end=" ")
    print()