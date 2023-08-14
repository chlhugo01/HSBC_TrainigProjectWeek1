from datetime import datetime
import transaction as tr

class account:

    def __init__(self, id, name, balance):
        self.__transactionlist = []
        self.__id = id
        self.__name = name
        self.__balance = balance
      
    def get_transactionlist(self):
        return self.__transactionlist

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance
