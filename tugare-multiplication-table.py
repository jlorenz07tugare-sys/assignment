while True:
    rows = int(input("Enter row: "))
    cols = int(input("Enter col: "))

    if rows <= 0 or cols <= 0:
        print("Program terminated.")
        break

    search = int(input("Search: "))

    for x in range(1, rows + 1):
        for y in range(1, cols + 1):
            value = x * y
            if value == search:
                print(f"[{value}]", end=" ")
            else:
                print(value, end=" ")
        print()
    print()
