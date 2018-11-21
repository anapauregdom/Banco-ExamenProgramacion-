#AnaPaulaGemaRegaladoDominguez
from Account import Account
from Bank import Bank

class Client:

   #Se define la clase Cliente
    def __init__(self,name,last_names,direction,age,account,bank):
        print("Creating the customer " + name)
        self.names=name
        self.last_names=last_names
        self.direction=direction
        self.age=age
        self.bank=bank
        self.list_account={}
        self.list_account_name={}
        self.number_account=1
        self.list_account[self.number_account] = account
        self.list_account_name[self.number_account] = str(account)

   #Se crea un metodo para añadir una cuenta
    def addAccount(self,account):
        self.list_account[self.number_account]=account
        self.list_account_name[self.number_account]=str(account)
        self.number_account+=1

   #Se crea un metodo para eliminar una cuenta
    def deleteAccount(self,index):
        del self.list_account[index]
        del self.list_account_name[index]
        self.number_account-=1

  #Regresa la direcciòn del cliente
    def getDirection(self):
        return self.__direction

  #Regresa el nombre del cliente
    def get_name(self):
        return self.__name

  #Regresa la edad del cliente
    def get_age(self):
        return self.__age

  #Regresa la cuenta del cliente
    def get_Account(self):
        return self.__Account
  #Regresa el Banco del cliente
    def get_Bank(self):
        return self.__Bank

  #Cambia la direccion del cliente por nueva_direccion
    def set_direction(self, nueva_direction):
        self.__direction = new_direction

  #Cambia el nombre del cliente por un nuevo nombre
    def set_name(self,new_name):
        self.__name=new_name

    def __str__(self):
        temp="Name: "+str(self.__name)
        temp+="\n Direction: "+str(self.__direction)
        temp+="\n Age: "+str(self.__age)
        temp+="\n Account: "+str(self.__Account)
        temp+="\n "+str(self.__Bank)
        return temp
