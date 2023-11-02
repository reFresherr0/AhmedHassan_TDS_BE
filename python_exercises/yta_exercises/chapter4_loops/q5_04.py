customers = []           # A list to hold customers

# define function to add customer to the bank
def add_customer():
    name = input("Enter customer name: ")
    balance = float(input("Enter initial balance: "))
    customer = [name, balance]
    customers.append(customer)
    print("Customer added successfully.")

# define function to remove customer from the bank
def remove_customer():
    name = input("Enter customer name: ")
    for customer in customers:
        if customer[0] == name:
            customers.remove(customer)
            print("Customer removed successfully.")
            return
    print("Customer not found.")

# define function to deposit money into a customer's account
def deposit():
    name = input("Enter customer name: ")
    for customer in customers:
        if customer[0] == name:
            amount = float(input("Enter amount to deposit: "))
            customer[1] += amount
            print("Deposit successful.")
            return
    print("Customer not found.")

# define function to withdraw money from a customer's account
def withdraw():
    name = input("Enter customer name: ")
    for customer in customers:
        if customer[0] == name:
            amount = float(input("Enter amount to withdraw: "))
            if amount > customer[1]:
                print("Insufficient funds.")
            else:
                customer[1] -= amount
                print("Withdrawal successful.")
            return
    print("Customer not found.")

# define function to print the balance of a specific customer's account
def print_balance():
    name = input("Enter customer name: ")
    for customer in customers:
        if customer[0] == name:
            print("Balance:", customer[1])
            return
    print("Customer not found.")

# define function to list all the customers and their account balances
def list_customers():
    for customer in customers:
        print(customer[0], ":", customer[1])

# define function to display menu and allow user to choose an operation
def menu():
    while True:
        print("\nBanking System Menu:")
        print("1. Add a customer")
        print("2. Remove a customer")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Print balance")
        print("6. List all customers")
        print("0. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_customer()
        elif choice == 2:
            remove_customer()
        elif choice == 3:
            deposit()
        elif choice == 4:
            withdraw()
        elif choice == 5:
            print_balance()
        elif choice == 6:
            list_customers()
        elif choice == 0:
            break
        else:
            print("Invalid choice. Try again.")

# call menu() function to start program
menu()
