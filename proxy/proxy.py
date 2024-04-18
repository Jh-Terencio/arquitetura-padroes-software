from abc import ABCMeta, abstractmethod

class ICliente(metaclass = ABCMeta):
    @abstractmethod
    def requisicao(self):
        """ Método de requisição """

class ClienteReal(ICliente):
    def requisicao(self):
        print("Cliente: Lidando com a requisição.")

class ClienteProxy(ICliente):
    def __init__(self, cliente, nivel_acesso):
      self.nivel_acesso = nivel_acesso
      self.cliente = cliente
      self.logs_acesso = []

    def requisicao(self):
        if self.verificar_acesso():
            self.cliente.requisicao()
            self.registrar_acesso()
        else:
            print("Proxy: Acesso negado.")
            self.logs_acesso.append("login negado devido a baixo nível de acesso")

    def verificar_acesso(self):
        if self.nivel_acesso >= 5:
          return True
        else:
          return False
        
    def registrar_acesso(self):
        print("Proxy: Acesso permitido")
        self.logs_acesso.append("Login feito com sucesso")

    def mostrar_logs_acesso(self):
        for log in self.logs_acesso:
            print(log)
