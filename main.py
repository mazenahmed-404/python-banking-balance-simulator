
# Getting a valid positive amount
def get_positive_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))

            if amount <= 0:
                print("The amount must be greater than zero. Try again!")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number!")


# Main function
def main():
    print("Welcome to your account in WaterMelon Bank (^_^)!")
    current_balance = 1000.0

    while True:
        print("----------------------")
        print("|1 --> Check Balance |")
        print("|2 --> Deposit       |")
        print("|3 --> Withdraw      |")
        print("|4 --> Exit          |")
        print("----------------------")

        # Getting a valid menu choice
        while True:
            action = input("\nChoose a number from the menu: ")

            if action in ("1", "2", "3", "4"):
                break

            print("Enter a valid option, please!")

        # Executing the selected action
        if action == "1":
            check_balance(current_balance)

        elif action == "2":
            current_balance = deposit(current_balance)

        elif action == "3":
            current_balance = withdraw(current_balance)

        elif action == "4":
            print("Thank you for using WaterMelon Bank. Goodbye!")
            break


# Checking the balance
def check_balance(current_balance):
    print(f"Your current balance is ${current_balance:.2f}")


# Making a deposit
def deposit(current_balance):
    amount = get_positive_amount("Enter the amount you want to deposit: ")

    current_balance += amount

    print(
        f"Deposit successful! Your new balance is "
        f"${current_balance:.2f}"
    )

    return current_balance


# Making a withdrawal
def withdraw(current_balance):
    while True:
        amount = get_positive_amount(
            "Enter the amount you want to withdraw: "
        )

        if amount > current_balance:
            print("Insufficient balance! Please enter a smaller amount.")
            continue

        break

    current_balance -= amount

    print(
        f"Withdrawal successful! Your new balance is "
        f"${current_balance:.2f}"
    )

    return current_balance


main()
