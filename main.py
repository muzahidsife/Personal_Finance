def amount():
    while True:
        account_balance = input("What is your account balance right now? ")
        if account_balance.isdigit():
            amount = int(account_balance)
            break
        else:
            print("Enter a digit.")

    return amount


def deposit_withdraw(amount):
    user = input("Do you want to deposit or withdraw? ")
    if user == "deposit":
        deposit = input("How much do you want to deposit? ")
        amount += int(deposit)
        print("Your current balance is:", amount)
    elif user == "withdraw":
        withdraw = input("How much do you want to withdraw? ")
        if amount < int(withdraw):
            print("Insufficient balance.")
        else:
            amount -= int(withdraw)
            print("Your current balance is:", amount)


balance = amount()
deposit_withdraw(balance)
