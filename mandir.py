for r in range(1,17):
    for c in range(1,8):
        if r==7 or r==16 or c==1 and r>7 or c==7 and r>6 or r+c==8 and r>3 or c-r==0 and r>4 or c==4 and r<4 or r==2 and c==5 or c==3 and r>10 or c==5 and r>10 or c==4 and r==11:
            print("* ", end="  ")
        else:
            print("   ", end=" ")
    print()
