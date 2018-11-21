#AnaPaulaGemaRegaladoDominguez
from Account import Account

class SavingAccount(Account):

   #Se define la clase Cuenta de Ahorro
    def __init__(self,init_balance=0,interest_rate=0.16):
        if(init_balance >=0) and (interest_rate >=0):
            Account.__init__(self,init_balance)
            self.interest_rate=interest_rate
            self.tipe= "Saving account"
        else:
            print("Error al crear la cuenta, verifica los valores indicados")
            return

    def __str__(self):
        return "Saving account with balance %s and an interest rate of %s" % (self.amount,self.interest_rate)
