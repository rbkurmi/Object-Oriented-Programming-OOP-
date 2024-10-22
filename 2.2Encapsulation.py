class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    # Public method to access private attribute
    def get_balance(self):
        return self.__balance


# Creating an instance
account = BankAccount(5000)

# Accessing balance using method (encapsulated)
print(account.get_balance())  # Output: 5000

# Trying to access private attribute directly (will cause an error)
# print(account.__balance)  # This will raise an AttributeError
