class Descriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not value < 0:
            old_value = instance.__dict__.get(self.name, 0)
            change = value - old_value
            if change > 0:
                print(f"Increase: {change}")
            else:
                print(f"decrease: {change}")
            instance.__dict__[self.name] = value

        else:
            raise ValueError(f"invalid data {value!r}")


class BankClass:
    balance = Descriptor()

    def __init__(self, balance: int):
        self.balance = balance


bank = BankClass(2)
print(bank.__dict__)
bank.balance = 10

