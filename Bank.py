#AnaPaulaGemaRegaladoDominguez

class  Bank:

 #Se define la clase Banco
  def __init__(self,name,location):
    self.name=name    
    self.location=location
    self.client_dictionary={}
    self.number_clients=0

 #Se crea un metodo para agregar un cliente 
  def add_client(self, client):
    if self.already_exists(client):
      print("Ese cliente ya existe")
      return
    else:
      client_dictionary[numbre_client] = client
      number_clients+=1

 #Se crea un metodo para obtener a un cliente 
  def already_exists(self,client):
    for x in range(number_clients):
      if client_dictionary[x] == client:
        return True
    return False

 #Se crea un metodo para eliminar a un cliente
  def erase_client(self, index):
    if index not in client_dictionary:
      print("Ese cliente no existe")
      return
    else:
      del client_dictionary[index]

  def __str__(self):  
    cadena="Bank: " +str(self.__name)
    cadena+="\n Location: "+str(self.__location)
    return cadena
