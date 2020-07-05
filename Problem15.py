# 15. Imagine you are designing a banking application. What would a customer look like?
# What attributes would she have? What methods would she have?


class Customer:

    def __init__(self, name, date_of_birth, address, contact_num, account_number, balance):
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address
        self.contact_num = contact_num
        self.account_number = account_number
        self.balance = balance

    def balance_deposit(self):
        print("Depositing balance...")

    def balance_withdrawl(self):
        print("Withdrawing balance")

    def balance_enqury(self):
        print("Checking balance...")

    def transaction_info(self):
        print("Getting information about transactions ...")


