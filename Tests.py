#AnaPaulaGemaRegaladoDominguez
import os,sys,unittest
sys.path.insert(0,"..")
from Account import *
from CheckingAccount import CheckingAccount
from SavingAccount import SavingAccount

#Pruebas de la clase Cuenta
class TestAccount(unittest.TestCase):

#Se prueba el metodo de crear una cuenta
    def testCreation(self):
        print("---Testing account creation---")
        test_account = Account(200)
        self.assertEqual(200,test_account.amount)
        self.assertRaises(ValueError,Account,-12)
        print("\n")

#Se prueba el metodo de depositar a una cuenta
    def testDeposit(self):
        print("---Testing account's deposit method---")
        test_account = Account(200)
        test_account.deposit(211)
        self.assertEqual(411,test_account.amount)
        self.assertEqual(True, test_account.deposit(21.4))
        self.assertEqual(False,test_account.deposit(-42))
        print("\n")

#Se prueba el metodo de retirar de una cuenta
    def testWithdraw(self):
        print("---Testing account's withdraw method---")
        test_account=Account(1000)
        self.assertEqual(False,test_account.withdraw(-4))
        self.assertEqual(True,test_account.withdraw(4))
        self.assertEqual(996,test_account.amount)
        self.assertEqual(False,test_account.withdraw(1000))
        print("\n")

#Pruebas de la clase Cuenta de Credito
class TestCheckingAccount(unittest.TestCase):

#Se prueba el metodo de crear una cuenta de credito
    def testCreateAccount(self):
        print("---Testing creation of a checking account---")
        checking_account =  CheckingAccount()
        self.assertEqual(0, checking_account.amount)
        self.assertEqual(0.0, checking_account.overdraft)
        print("\n")

#Se prueba el metodo de retirar de una cuenta de credito con y sin overdraft
    def testWithdraw(self):
        print("---Testing checking account's  withdraw method--- \n")
        checking_account =  CheckingAccount()
        self.assertEqual(False, checking_account.withdraw(40))
        print ("\n")
        checking_account2 = CheckingAccount(0,10)
        self.assertEqual(True,checking_account2.withdraw(9))
        self.assertEqual(False,checking_account2.withdraw(11))
        print ("\n")
        checking_account3 = CheckingAccount(10,10)
        self.assertEqual(True,checking_account3.withdraw(19))
        self.assertEqual(-9,checking_account3.amount)
        self.assertEqual(False, checking_account3.withdraw(111))
        print("\n")

#Pruebas de la clase Cuenta de Ahorros
class TestSavingAccount(unittest.TestCase):

#Se prueba el metodo de crear una cuenta de ahorros
    def testCreation(self):
        print("---Testing saving account's creation---")
        account = SavingAccount(123)
        print("\n")

#Pruebas de la clase Cliente
#Se prueba la creacion de un cliente
class TestClient(unittest.TestCase):
    pass
if __name__=='__main__':
    unittest.main()
