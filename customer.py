class customer:

    def __init__(self, id, name, email, address):
        self.__accountList = []
        self.__id = id
        self.__name = name
        self.__email = email
        self.__address = address

    def set_accountList(self,account):
        self.__accountList.append(account)
        

    def get_accountList(self):
        return self.__accountList

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address
