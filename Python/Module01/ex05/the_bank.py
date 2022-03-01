from xmlrpc.client import Boolean


class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
          raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
          raise AttributeError("Attribute name must be a str object.")
    
    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account: Account)-> None:
        """ Add new_account in the Bank
            @new_account:  Account() new account to append
            @return   True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if 
        # it can be appended to the attribute accounts
        # ... Your code  ...
        if isinstance(new_account, Account):
            self.accounts.append(new_account)
        else:
            print("ERROR : The argument must be an account")

    def account_verif(self,acc: Account)-> Boolean:
        acc_exist = False
        for i,acc_origin in enumerate(self.accounts):
            if acc_origin.name == acc:
                acc_exist = True
                break
        return acc_exist

    def transfer(self, origin: Account, dest: Account, amount: int):
        """" Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
        # ... Your code  ...
        if amount < 0:
            print("ERROR : The amount transfer must be superior than 0")
            return False

        else:
            origin_exist = self.account_verif(origin)
            
            dest_exist = self.account_verif(dest)
            
            if origin_exist == False:
                print("ERROR : Origin acount does not exist")
                return False
            
            elif dest_exist == False:
                print("ERROR : Destination acount does not exist")
                return False
            
            else:
                if self.accounts[i].value > amount:
                    self.accounts[i].transfer(-1*amount)
                    self.accounts[j].transfer(amount)
                    return True
                
                else:
                    print("You don't have this amount in your account")
                    return False


    def fix_account(self, name:str):
        """ fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
        # ... Your code  ...
        