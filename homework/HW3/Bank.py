from enum import Enum
from IPython.display import clear_output

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount:
    def __init__(self, owner, accountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0
        
    # withdraw method
    def withdraw(self, amount):
        # first check if amount is neg
        if amount < 0:
            raise Exception('You cannot withdraw a negative amount of money.')
        if amount <= self.balance:
            self.balance -= amount
        # amount is greater than balance
        else:
            raise Exception('You cannot withdraw more than what you have in this acccount.')
    
    def deposit(self, amount):
        # first check if amount is neg
        if amount < 0:
            raise Exception('You cannot deposit a negative amount of money.')
        else:
            self.balance += amount
        
    def __str__(self):
        return "A {} account owned by {}.".format(self.accountType.name, self.owner)
    
    def __len__(self):
        return self.balance

class BankUser(object):
    def __init__(self, owner):
        self.name = owner
        self.checking = None
        self.savings = None

    # function to check if user has an account of requested type
    def _accountChecker(self, accountType):
        # checks if accountType is savings, and if user has savings
        if accountType == AccountType.SAVINGS:
            if self.savings != None:
                return True
        # checks if accountType is checking, and if user has checking
        else:
            if self.checking != None:
                return True
        # user does not have account of requested type
        return False
    
    def addAccount(self, accountType):
        # checks if accountType is savings, and if user already has savings
        if accountType == AccountType.SAVINGS and self.savings == None:
            self.savings = BankAccount(self.name, accountType)
        # checks if accountType is checking, and if user already has checking
        elif accountType == AccountType.CHECKING and self.checking == None:
            self.checking = BankAccount(self.name, accountType)
        else:
            raise Exception('{} already has an account of this type.'.format(self.name))

    # get balance method                
    def getBalance(self, accountType):
        # uses accountChecker helper function
        if self._accountChecker(accountType):
            if accountType.value == 1:
                return len(self.savings)
            else:
                return len(self.checking)
        else:
            raise Exception('{} does not have an account of this type.'.format(self.name))
                
    # deposit method
    def deposit(self, accountType, amount):
        # uses accountChecker helper function
        if self._accountChecker(accountType):
            if accountType.value == 1:
                self.savings.deposit(amount)
            else:
                self.checking.deposit(amount)
        else:
            raise Exception('{} does not have an account of this type.'.format(self.name))

    # withdraw method               
    def withdraw(self, accountType, amount):
        # uses accountChecker helper function
        if self._accountChecker(accountType):
            if accountType.value == 1:
                self.savings.withdraw(amount)
            else:
                self.checking.withdraw(amount)
        else:
            raise Exception('{} does not have an account of this type.'.format(self.name))
                
    def __str__(self):
        # if no accounts have been opened
        if self.savings == None and self.checking == None:
            return ("{} has not opened any account.".format(self.name))
        # if checking but not savings has been opened
        elif self.savings == None:
            return ("{} has ${} in their checking account.".format(self.name, self.getBalance(AccountType.CHECKING)))
        # if savings but not checking has been opened
        elif self.checking == None:
            return ("{} has ${} in their savings account.".format(self.name, self.getBalance(AccountType.SAVINGS)))
        # both are open
        else:
            return ("{} has ${} in their checking account and ${} in their savings account.".format(self.name, 
                                                                                                    self.getBalance(AccountType.CHECKING),
                                                                                                    self.getBalance(AccountType.SAVINGS)))
def ATMSession(bankUser):
    def Interface(bankUser):
        screen = 1
        screen1 = "1) Exit\n2) Create Account\n3) Check Balance\n4) Deposit\n5) Withdraw"
        screen2 = "1) Checking\n2) Savings\n3) Go back"
        while True:
            # clear output on every run of loop
            clear_output()
            # main screen
            if screen == 1:
                print (screen1)
                try:
                    opt = int(input('Enter Option: '))
                except ValueError:
                    print ('Invalid option.')
                    input ('Enter any key to continue.')
                    continue
                # exiting
                if opt == 1:
                    print ('Thank you for banking.')
                    break
                # choosing the other four options
                elif opt >= 2 and opt<= 5:
                    screen = opt
                # any other key, goes back to main menu
                else:
                    print ('Invalid option.')
                    input ('Enter any key to continue.')
            # creating an account
            elif screen == 2:
                print (screen2)
                try:
                    opt = int(input('Enter Option: '))
                # any invalid option will redirect to main menu
                except ValueError:
                    print ('Invalid option.')
                    input ('Enter any key to continue.')
                    screen = 1
                    continue
                # adds checking account
                if opt == 1:
                    try:
                        bankUser.addAccount(AccountType.CHECKING)
                        print (str(bankUser))
                        input('Enter any key to continue.')
                    except Exception as e:
                        print (e)
                        input('Enter any key to continue.')
                # adds savings account
                elif opt == 2:
                    try:
                        bankUser.addAccount(AccountType.SAVINGS)
                        print (str(bankUser))
                        input('Enter any key to continue.')
                    except Exception as e:
                        print (e)
                        input('Enter any key to continue.')
                # going back to main menu
                elif opt == 3:
                	pass
                # any other key, goes back to menu
                else:
                    print ('Invalid option.')
                    input ('Enter any key to continue.')
                screen = 1
            # checking balance
            elif screen == 3:
                print (screen2)
                try:
                    opt = int(input('Enter Option: '))
                except ValueError:
                    print ('Invalid option.')
                    input ('Enter any key to continue.')
                    screen = 1
                    continue
                if opt == 1:
                    try:
                        print ('{} has ${} in their checking account.'.format(bankUser.name, 
                                                                            bankUser.getBalance(AccountType.CHECKING)))
                        input('Enter any key to continue.')
                    except Exception as e:
                        print (e)
                        input('Enter any key to continue.')
                elif opt == 2:
                    try:
                        print ('{} has ${} in their savings account.'.format(bankUser.name, 
                                                                            bankUser.getBalance(AccountType.SAVINGS)))
                        input('Enter any key to continue.')
                    except Exception as e:
                        print (e)
                        input ('Enter any key to continue.')
                elif opt == 3:
                	pass
                else:
                    print ('Invalid option.')
                    input ('Enter any key to continue.')
                screen = 1
            # depositing
            elif screen == 4:
                print (screen2)
                try:
                    opt = int(input('Enter Option: '))
                except ValueError:
                    print ('Invalid option.')
                    input ('Enter any key to continue.')
                    screen = 1
                    continue
                if opt == 1:
                    try:
                        amount = int(input('Enter Integer Amount, Cannot Be Negative: '))
                        bankUser.deposit(AccountType.CHECKING, amount)
                        print (str(bankUser))
                    except (Exception, ValueError) as e:
                        print (e)
                    input('Enter any key to continue.')
                elif opt == 2:
                    try:
                        amount = int(input('Enter Integer Amount, Cannot Be Negative: '))
                        bankUser.deposit(AccountType.SAVINGS, amount)
                        print (str(bankUser))
                    except (Exception, ValueError) as e:
                        print (e)
                    input('Enter any key to continue.')
                elif opt == 3:
                	pass
                else:
                    print ('Invalid option.')
                    input ('Enter any key to continue.')              
                screen = 1
            # withdrawing
            elif screen == 5:
                print (screen2)
                try:
                    opt = int(input('Enter Option: '))
                except ValueError:
                    print ('Invalid option.')
                    input ('Enter any key to continue.')
                    screen = 1
                    continue
                if opt == 1:
                    try:
                        amount = int(input('Enter Integer Amount, Cannot Be Negative: '))
                        bankUser.withdraw(AccountType.CHECKING, amount)
                        print (str(bankUser))
                    except (Exception, ValueError) as e:
                        print (e)
                    input('Enter any key to continue.')                
                elif opt == 2:
                    try:
                        amount = int(input('Enter Integer Amount, Cannot Be Negative: '))
                        bankUser.withdraw(AccountType.SAVINGS, amount)
                        print (str(bankUser))
                    except (Exception, ValueError) as e:
                        print (e)
                    input('Enter any key to continue.')
                elif opt == 3:
                	pass
                else:
                    print ('Invalid option.')
                    input ('Enter any key to continue.')
                screen = 1
    return Interface(bankUser)                                                                                  