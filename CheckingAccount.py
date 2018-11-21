#AnaPaulaGemaRegaladoDominguez
from Account import Account

class CheckingAccount(Account):

   #Se define la clase Cuenta de Credito
    def __init__(self, amount=0,overdraft=0.00):
        if(amount>=0) and (overdraft>=0):
            if(overdraft==0):
                print('Creating saving account with %s balance and no overdraft' %(amount) )
            else:
                print('Creating saving account with %s balance and %s overdraft' %(amount,overdraft))
            self.amount=amount
            self.overdraft=overdraft
            self.type= "Checking account"
        else:
            print('Error while creating the account, please verify your inputs')

   #Se crea un metodo para retirar dinero
    def withdraw(self, amt):
        finished=False
        if (amt>=0):
            if(amt<=self.amount):
                finished=True
                self.amount-=amt
                print('Withdrawing %s: %s' %(amt,finished))
            else:
                if(self.amount + self.overdraft >= amt):
                    finished =True
                    self.amount-=amt
                    print('Withdrawing %s: %s' %(amt,finished))
                else:
                    print('Withdrawing %s: %s' %(amt,finished))
        print("Your balance is %s" % self.amount)
        return finished

    def __str__(self):
        return "Checking account with %s balance and %s overdraft" % (self.amount,self.overdraft)
