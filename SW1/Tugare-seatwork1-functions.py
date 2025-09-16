def convertDollars(amount):
    iRupee_rate = 83.05   
    bPound_rate = 0.73   
    cYuan_rate = 7.12    

    iRupee = amount * iRupee_rate
    bPound = amount * bPound_rate
    cYuan = amount * cYuan_rate
    return iRupee, bPound, cYuan

while True:
    dollar = input("Enter dollar ($) (* to exit): ").strip()
    if dollar == '*':
        print("Bye")
        break

    inputs = dollar.split('@')
    dollars = [float(i) for i in inputs if i.replace('.', '', 1).isdigit()]

    if not dollars:
        continue

    print(f"{'Dollar ($)':<15}{'Indian Rupee (R)':<20}{'British Pound (Pound)':<25}{'China (Yuan)'}")

    for amt in dollars:
        inr, gbp, cny = convertDollars(amt)
        print(f"{amt:<15.2f}{inr:<20.2f}{gbp:<25.2f}{cny:.2f}")
