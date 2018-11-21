#AnaPaulaGemaRegaladoDominguez
import os, sys
sys.path.insert(0,"../system")
from Account import Account
from Bank import Bank
from Client import Client
from CheckingAccount import CheckingAccount
from SavingAccount import SavingAccount
from Account import Account

class GUI:

#Se define la clase Menu
    def __init__(self):
        self.client_list={}
        self.client_list_name={}
        self.number_clients=0
        self.bank_list={}
        self.bank_list_name={}
        self.number_banks=0
        self.bienvenida()

#Se crea un metodo para dar la bienvenida que da las opciones de elegir un banco
#crear un cliente nuevo, manejar a un cliente existente o salir
    def bienvenida(self):
        isWorking=True
        print("+=+=+=Welcome+=+=+=")
        while(isWorking):
            print("===Select an option===")
            print("0 to start the bank's menu")
            print("1 to create a new client")
            print("2 to manage an existent client")
            print("3 to exit")
            opcion = input("Select an option: ")
            if (opcion == '3'):
                print("Bye :)")
                isWorking=False
            elif (opcion == '2'):
                self.manageClient()
            elif (opcion == '1'):
                self.createClient()
            elif(opcion == "0"):
                self.chooseBanks()
            else:
                print("\n\nVerify your inpunt\n\n")
#Se crea un metodo para poder crear un cliente nuevo
#(En el caso de elegir "1 to create a new client")
    def createClient(self):
        names =input(">Type your names (and only names): ")
        last_names = input(">Type your last names: ")
        direction = input(">Type your direction: ")
        age = input(">Type your age: ")
        account = self.chooseAccount()
        bank = self.chooseBank()
        cliente=Client(names,last_names,direction,age,account,bank)
        self.client_list[self.number_clients] = cliente
        self.client_list_name[self.number_clients] = cliente.names
        self.number_clients+=1

#Se crea un metodo para poder elegir si se desea crear una cuenta de credito
#o una cuenta de ahorros (En el caso de elegir "1 to create a new client")
    def chooseAccount(self):
        print("===Creating account menu===")
        print("1 to create a checking account")
        print("2 to create a saving account")
        option = input("---Select an option---")
        if option != "1" and option != "2":
            print("\nSelect a valid options\n")
            self.chooseAccount()
        return self.returnAccount(option)

#Se crea un metodo para crear una cuenta de credito o de ahorros
#(En el caso de elegir "1 to create a new client")
    def returnAccount(self,value):
        try:
            if value == "1":
                return CheckingAccount()
            elif value == "2":
                return SavingAccount()
            else:
                raise ValueError
        except ValueError as e:
             print("\n\nCheck your input values\n\n")
             self.returnAccount(value)

#Se crea un metodo para elegir un banco o crear un banco
#(En el caso de elegir "0 to start the bank's menu")
    def chooseBank(self):
        print("===Bank Menu===")
        print(">1 to choose an already created bank")
        print(">2 to create a new bank")
        try:
            option = int(input("Select an option: "))
            if option == 1 :
                self.returnBank(1)
            elif option == 2:
                self.returnBank(2)
            else:
                raise ValueError
        except ValueError as e:
            print("\n\nSelect a valid option\n\n")
            self.chooseBank()

#Se crea un metodo para obtener un banco o crear uno nuevo
#(En el caso de elegir "0 to start the bank's menu")           
    def returnBank(self,option):
        if option == 1:
            if (self.number_banks==0):
                print("\n\nThe bank list is empty\n\n")
                print("Creating a new bank\n\n")
                self.returnBank(2)
            else:
                print(self.bank_list_name)
                chosen_bank = int(input(">Choose an index of the banks "))
                if chosen_bank in self.bank_list:
                    return self.bank_list[chosen_bank]
                else:
                    print("\n\nSelect a valid index\n\n")
                    self.returnBank(1)
        elif option == 2:
            name = input("Choose a name for the bank ")
            address = input("Type the address for the bank ")
            new_bank =  Bank(name,address)
            self.bank_list[self.number_banks] = new_bank
            self.bank_list_name[self.number_banks]= new_bank.name
            self.number_banks+=1
            return new_bank

#Se crea un metodo para manejar a un cliente existente
#(En el caso de elegir "2 to manage an existent client")
    def manageClient(self):
        print('---Manage client menu---')
        print('Select a person: ')
        if self.client_list == {}:
            print("\n\nThe client's list is empty\n\n")
            return
        else:
            print(self.client_list_name)
            try:
                index = int(input('Select a person index '))
                if not index in self.client_list:
                    raise ValueError
                else:
                    self.chooseClientAccount(self.client_list[index])
            except ValueError as e:
                print("Select a valid option")
                self.manageClient()

#Se crea un metodo para que el cliente pueda visualizar sus cuentas existentes,
#agregar una cuenta nueva, eliminar una cuenta o manejar una de sus cuentas
    def chooseClientAccount(self,client):
        print('0 to show your accounts')
        print('1 to add an account')
        print('2 to delete an account')
        print('3 to manage an account')
        print('4 to exit')
        try:
            option = int(input("Select an option "))
            if option == 0:
                print(client.list_account_name)
                self.chooseClientAccount(client)
            elif option ==1:
                account_to_work = self.chooseAccount()
                client.addAccount(account_to_work)
                self.chooseClientAccount(client)
            elif option ==2 :
                try:
                    to_erase = int(input("Select an index "))
                    if to_erase not in client.list_account:
                        raise ValueError
                    else:
                        client.deleteAccount(to_erase)
                except ValueError as e:
                    print("Select a valid index ")
                    self.chooseClientAccount(client)
            elif option ==3:
                self.manageAccounts(client)
            elif option ==4:
                return
            else:
                raise ValueError
        except ValueError as e:
            print("Select a valid option")
            self.manageClient()

#Se crea un metodo para que el cliente pueda visualizar sus cuentas existentes
#para poder elegir una y manejarla
    def manageAccounts(self,client):
        print("Your accounts are: ")
        print(client.list_account_name)
        try:
            account = int(input("Select an account"))
            if account not in client.list_account:
                raise ValueError
            else:
                account_to_work = client.list_account[account]
                self.depositOrWithdraw(account_to_work)
        except ValueError as e:
            print("Select a valid index")
            self.manageAccounts(client)

#Se crea un metodo para que el cliente pueda depositar o retirar de su cuenta
#(Despues de elegir una cuenta)
    def depositOrWithdraw(self,account):
        print("Select an option")
        print("1 to make a deposit")
        print("2 to withdraw")
        print("3 to exit")
        try:
            option = int(input("Select an account"))
            if option == 1:
                account.deposit(input("Type how much you want to deposit"))
                self.depositOrWithdraw(account)
            elif option ==2:
                account.withdraw(input("Type how much you want to withdraw"))
                self.depositOrWithdraw(account)
            elif option ==3:
                return
            else:
                raise ValueError
        except ValueError as e:
            print("Select a valid option")


    def chooseBanks(self):
        print("===Banks menu===")
        print("0 to show all banks")
        print("1 to select a bank")
        print("2 to exit")
        try:
            option = int(input("Select an option "))
            if option == 0:
                print(self.bank_list_name)
            elif option == 1:
                try:
                    bank_index= int(input("Select the index of a bank"))
                    if bank_index not in self.bank_list:
                        raise ValueError
                    else:
                        self.manageBank(self.bank_list[bank_index])
                except ValueError as e:
                    print("Select a validate index")
                    self.chooseBanks()
            elif option ==2:
                return
        except ValueError as e:
            print("Select a validate index")
            self.chooseBanks()

#Se crea un metodo para manejar un banco, añadiendo las opciones de ver la lista
#de clientes, agregar un cliente, eliminar un cliente o salir
    def manageBank(self, bank):
        print("The clients list: ")
        print(bank.client_list_name)
        print("1 to add a client")
        print("2 to erase a client")
        print("3 to exit")
        try:
            option = int(input("Select an option "))
            if option == 1:
                print("All the clients are")
                print(self.client_list_name)
                try:
                    client_id= int(input("Select a client id"))
                    if client_id not in self.client_list:
                        raise ValueError
                    else:
                        bank.add_client(self.client_list[client_id])
                except ValueError as e:
                    print ("That index doesn't exists")
                    self.manageBank()
            elif option == 2:
                try:
                    client_id= int(input("Select a client id"))
                    if client_id not in self.client_list:
                        raise ValueError
                    else:
                        bank.erase_client(self.client_list[client_id])
                except ValueError as e:
                    print ("That index doesn't exists")
                    self.manageBank()
            elif option ==3:
                return
            else:
                raise ValueError
        except ValueError as e:
            print ("That option doesn't exists")
            self.manageBank()
if __name__=="__main__":
    GUI = GUI()
