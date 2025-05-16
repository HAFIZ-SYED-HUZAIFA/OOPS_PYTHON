class Bank :
    bank_name = "HBL"

    @classmethod
    def change_bankname(cls,name) :
        cls.bank_name = name

bank1 = Bank()
bank2 = Bank()

print(bank1.bank_name)
print(bank2.bank_name)

Bank.change_bankname("Global bank")
print(bank1.bank_name)
print(bank2.bank_name)