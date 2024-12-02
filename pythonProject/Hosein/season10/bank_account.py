from typing import List


def separate_number(number: str):
    separated = ' '.join([number[i:i+4] for i in range(0, len(number), 4)])
    return separated


def format_numberIR(number: str):
    separate = ' '.join([number[i:i+4] for i in range(0, len(number), 4)])

    farmat_stringIR = f"IR {separate}"

    first_two = number[:2]
    remaining = number[2:]

    separated_remaining = ' '.join([remaining[i:i+4] for i in range(0, len(remaining), 4)])

    final_result = f"IR {first_two} {separated_remaining}"
    return final_result


class BankAccount:
    __cardNumber: List[str] = []
    last_cardNumber = 6037000000000000
    __accountNumber: List[str] = []
    last_accountNumber = 910000000000000000000000
    __cvv2: List[str] = []
    last_cvv2 = 0000
    def __init__(self, name: str, expretionDate: str, balance: int = 0):
        self.name = name
        self.expretionDate = expretionDate
        self.balance = balance
        BankAccount.last_cvv2 += 1
        self.cvv2 = str(BankAccount.last_cvv2)
        BankAccount.__cvv2.append(self.cvv2)
        BankAccount.last_accountNumber += 1
        self.accountNumber = format_numberIR(str(BankAccount.last_accountNumber))
        BankAccount.__accountNumber.append(self.accountNumber)
        BankAccount.last_cardNumber += 1
        self.cardNumber = separate_number(str(BankAccount.last_cardNumber))
        BankAccount.__cardNumber.append(self.cardNumber)

    def see_property(self):
        return f"Name: {self.name}\nCard number: {self.cardNumber}\nAccount number: {self.accountNumber}\nCvv2: {self.cvv2}\nExpretionDate: {self.expretionDate}\nBalance: {self.balance}"

    def __str__(self):
        return self.see_property()
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.expretionDate}, {self.balance})"

    def see_balance(self):
        return f"name: {self.name}\nyour balance: {self.balance}"
    
    def deposit(self):
        deposit_amount = int(input("Enter your deposit amount: "))
        self.balance += deposit_amount
        return f"Inventory increase was done successfully\n", self.see_balance()
    
    def picked(self):
        picked_amount = int(input("Enter your picked amount: "))
        if (self.balance > picked_amount):
            self.balance -= picked_amount
            return "The picked was successfully\n", self.see_balance()
        else:
            return "mojody shoma kafi nemibashad!!!!!!!!"


def main():
    acc1 = BankAccount("Hosein", "1405/07")

    print(acc1.deposit())
    print(acc1.picked())

if __name__ == "__main__":
    main()

