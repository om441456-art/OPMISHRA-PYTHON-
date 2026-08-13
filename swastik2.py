for c in range(1, 14):
    for r in range(1, 18):
        if r==9 and c>2 and c<12 or c==7 and r>4 and r<14 or r==5 and c<7 and c>2 or r==13 and c<12 and c>7 or c==3 and r>9 and r<14 or c==11 and r<9 and r>4 or r==1 and c>3 and c<11 or r==2 and c>3 and c<11 or r==16 and c>3 and c<11 or r==17 and c>3 and c<11 or (c==5 and r==7) or (c==9 and r==7) or (c==5 and r==11) or (c==9 and r==11) or (c==2 and (r==14 or r==4)) or c==12 and (r==14 or r==4) or (c==1 and (r==3 or r==15)) or (c==13 and (r==3 or r==15)):
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print()