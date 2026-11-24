def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount, "Success"
    return balance, "Insufficient Balance"

if __name__ == "__main__":
    bal = float(input("Initial balance: "))
    amt = float(input("Withdrawal amount: "))
    new_bal, msg = withdraw(bal, amt)
    print(f"{msg}. Balance: {new_bal:.2f}")