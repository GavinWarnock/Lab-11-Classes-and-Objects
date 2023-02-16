class Person:
    def __init__(self, name_of_person, amount_of_money_in_account):
        self.name = name_of_person
        self.account = amount_of_money_in_account
    
    def send_funds(self, amount_to_transfer):
        if amount_to_transfer > self.account:
            print("Insufficient funds available!")
        elif amount_to_transfer <= self.account:
            self.account = self.account - amount_to_transfer
            print(f"{self.name} has {self.account} left in their account.")
            return self.account

    def receive_funds(self, person, funds_to_transfer):
        self.account = funds_to_transfer + self.account
        print(f"{person.name} transferred {funds_to_transfer} to you. Your current balance is {self.account}")

