#AnaPaulaGemaRegaladoDominguez

class Account():

   #Se define la clase Cuenta
    def __init__(self, amount):
        if(amount >=0):
            self.amount=amount
        else:
          raise ValueError("the amount can't be less than 0") 

   #Se crea un metodo para obtener el balance de la cuenta
    def getBalance(self):
        return self.amount

   #Se crea un metodo para depositar dinero en la cuenta
    def deposit(self,amt):
        if amt>=0 :
            self.amount+= amt
            print("Deposit %s : %s" %(amt, True))
            return True
        else:
            return False

   #Se crea un metodo para retirar dinero de la cuenta
    def withdraw(self,amt):
        completed=False
        if amt>=0:
            if (amt <= self.amount):                
                self.amount -= amt
                completed=True
        else:
            print("Withdraw %s : %s" %(amt, completed))
        return completed

    def __str__(self):
        return "La cuenta creada tiene %s de credito" % self.amount
