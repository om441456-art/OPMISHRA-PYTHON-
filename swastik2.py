for r in range(1, 14):
    for c in range(1, 14):
        if (r==2 and (c==2 or c>7)) or r==7 or (r==12 and c<7) or (c==2 and r<7) or c==7 or (c==12 and r>7):
            print("*", end="  ")
        elif (r==4 and c==4) or (r==4 and c==10) or (r==10 and c==4) or (r==10 and c==10):
            print("*", end="  ")
        else:
            print("  ", end=" ")
    print()