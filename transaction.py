class transaction:
 
    def __init__(self, date, id, amount, crdr, balance, description):
        self.__date = date
        self.__id = id
        self.__amount = amount
        self.__crdr = crdr
        self.__balance = balance
        self.__description = description

    def get_date(self):
        return self.__date

    def get_id(self):
        return self.__id

    def get_amount(self):
        return self.__amount

    def get_crdr(self):
        return self.__crdr

    def get_balance(self):
        return self.__balance

    def get_description(self):
        return self.__description


