for i in range(1, 11):
    match i:
        case int() if i == 5:
            print("5 ko skip kar diya gaya")
            continue
        case _:
            print(i)
