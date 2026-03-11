def zakat_calculator():
    print("Welcome to our zakat calculator.")

    cash = float(input("Enter your total cash and bank balance: "))
    gold_value = float(input("Enter the current price of gold per vori: "))
    gold_amount = float(input("Enter the amount of your gold in vori: "))
    gold = gold_amount * gold_value

    silver_value = float(input("Enter the current price of silver per vori: "))
    silver_amount = float(input("Enter the amount of your silver in vori: "))
    silver = silver_value * silver_amount

    business_assets = float(input("Enter the total amount of your business assets: "))
    investments = float(input("Enter the total amount of your investments: "))
    liabilities = float(input("Enter the total amount of your liabilities: "))

    total_assets = cash + gold + silver + business_assets + investments - liabilities
    nisab = 7.5 * gold_value

    if total_assets >= nisab:
        zakat = total_assets * 0.025
        print("You have to pay", zakat, "BDT as your zakat.")
    else:
        print("No zakat due (below nisab)")
zakat_calculator()
