
# * Considere um sistema de delivery de comida, onde os pedidos passam por diferentes status, como “aguardando confirmação do restaurante”, "em preparo", “pronto para entrega“, “saiu para entrega”, e “entregue". Qualquer semelhança com o ifood é mera coincidência. Cada estado possui diferentes ações associadas, como notificar o cliente sobre o status do pedido, chamar o entregador, receber o pagamento, e outros.

# * Proponha uma solução utilizando o padrão de design State para modelar os diferentes estados de um pedido como classes separadas. As operações que permitem mudar de estado devem ser operações disponíveis numa classe de contexto, que nesse caso, seria uma Central de Pedidos.

# * Crie um diagrama de estados representando a máquina de estados finita que você construiu. Por fim, para testar o seu sistema, crie em uma classe Cliente um objeto da Central de Pedidos e exercite todos os estados do seu sistema. Acrescente no código comentários indicando a mudança de estado.

from abc import ABCMeta, abstractstaticmethod
import time

class IEstado(metaclass=ABCMeta):
    @abstractstaticmethod
    def aguardando_confirmacao(self):
        """ Método de confirmação """

    @abstractstaticmethod
    def em_preparo(self):
        """ Método de preparo """

    @abstractstaticmethod
    def pronto_para_entrega(self):
        """ Método de pronto para entrega """

    @abstractstaticmethod
    def saiu_para_entrega(self):
        """ Método de saiu para a entrega """

    @abstractstaticmethod
    def entregue(self):
        """ Método de entregue """

class AguardandoConfirmacao(IEstado):
    def aguardando_confirmacao(self):
        print("Pedido já está aguardando confirmação")

    def em_preparo(self):
        time.sleep(5) 
        print("Pedido confirmado, em preparo")  
        return EmPreparo()

    def pronto_para_entrega(self):
        print("Pedido ainda não confirmado pelo restaurante")

    def saiu_para_entrega(self):
        print("Pedido ainda não confirmado pelo restaurante")

    def entregue(self):
        print("Pedido ainda não confirmado pelo restaurante")

class EmPreparo(IEstado):
    def aguardando_confirmacao(self):
        print("Pedido já está em preparo")

    def em_preparo(self):
        print("Pedido já está em preparo")

    def pronto_para_entrega(self):
        time.sleep(5) 
        print("Pedido pronto para entrega") 
        return ProntoParaEntrega()

    def saiu_para_entrega(self):
        print("Pedido ainda não está pronto para entrega")

    def entregue(self):
        print("Pedido ainda não está pronto para entrega")

class ProntoParaEntrega(IEstado):
    def aguardando_confirmacao(self):
        print("Pedido já está pronto para entrega")

    def em_preparo(self):
        print("Pedido já está pronto para entrega")

    def pronto_para_entrega(self):
        print("Pedido já está pronto para entrega")

    def saiu_para_entrega(self):
        time.sleep(5) 
        print("Pedido saiu para entrega")
        return SaiuParaEntrega()

    def entregue(self):
        print("Pedido ainda não saiu para entrega")

class SaiuParaEntrega(IEstado):
    def aguardando_confirmacao(self):
        print("Pedido já saiu para entrega")

    def em_preparo(self):
        print("Pedido já saiu para entrega")

    def pronto_para_entrega(self):
        print("Pedido já saiu para entrega")

    def saiu_para_entrega(self):
        print("Pedido já saiu para entrega")

    def entregue(self):
        time.sleep(5) 
        print("Pedido entregue")
        return Entregue()

class Entregue(IEstado):
    def aguardando_confirmacao(self):
        print("Pedido já foi entregue")

    def em_preparo(self):
        print("Pedido já foi entregue")

    def pronto_para_entrega(self):
        print("Pedido já foi entregue")

    def saiu_para_entrega(self):
        print("Pedido já foi entregue")

    def entregue(self):
        print("Pedido já foi entregue")

class Restaurante:
    def __init__(self):
        self.estado = AguardandoConfirmacao()

    def aguardando_confirmacao(self):
        self.estado.aguardando_confirmacao()

    def em_preparo(self):
        self.estado = self.estado.em_preparo()

    def pronto_para_entrega(self):
        self.estado = self.estado.pronto_para_entrega()

    def saiu_para_entrega(self):
        self.estado = self.estado.saiu_para_entrega()

    def entregue(self):
        self.estado = self.estado.entregue()

class Cliente:
    def __init__(self):
        self.central_pedidos = Restaurante()

    def realizar_pedido(self):

        self.central_pedidos.aguardando_confirmacao()
        
        self.central_pedidos.em_preparo()

        self.central_pedidos.pronto_para_entrega()

        self.central_pedidos.saiu_para_entrega()

        self.central_pedidos.entregue()

cliente = Cliente()
cliente.realizar_pedido()



