from proxy import ClienteReal, ClienteProxy

class Cliente:
    def __init__(self, nivel_acesso):
      self.nivel_acesso = nivel_acesso
      self.proxy = ClienteProxy(ClienteReal(), self.nivel_acesso)

    def acesso_recurso(self):
        print("Tentando acessar recurso...")
        self.proxy.requisicao()

if __name__ == "__main__":
    cliente = Cliente(5)
    cliente.acesso_recurso() 
    print("\nLogs de Acesso Cliente 1:")
    cliente.proxy.mostrar_logs_acesso()

    cliente2 = Cliente(2)
    cliente2.acesso_recurso()
    print("\nLogs de Acesso Cliente 2:")
    cliente2.proxy.mostrar_logs_acesso()
    