from abc import ABCMeta, abstractstaticmethod

# * Icommand Interface
class ICommand(metaclass=ABCMeta):
  
  @abstractstaticmethod
  def execute():
    """Método de uma interface estática"""
    
  def undo():
    """Método de uma interface estática"""

# * Comandos
class Ligar(ICommand):
  def __init__(self, dispositivo):
        self.dispositivo = dispositivo

  def execute(self):
      self.dispositivo.ligar()

  def undo(self):
      self.dispositivo.desligar()

class Desligar(ICommand):
  def __init__(self, dispositivo):
        self.dispositivo = dispositivo

  def execute(self):
      self.dispositivo.desligar()

  def undo(self):
      self.dispositivo.ligar()

class Aumentar(ICommand):
  def __init__(self, dispositivo):
        self.dispositivo = dispositivo

  def execute(self):
      self.dispositivo.aumentar()

  def undo(self):
      self.dispositivo.diminuir()
      
class Diminuir(ICommand):
  def __init__(self, dispositivo):
        self.dispositivo = dispositivo

  def execute(self):
      self.dispositivo.diminuir()

  def undo(self):
      self.dispositivo.aumentar()
class TrocarCanal(ICommand):
  def __init__(self, televisao):
    self._televisao = televisao
    
  def execute(self):
    self._televisao.trocar_canal()      
    
# * Lampada
class Lampada:
  
  def ligar(self):
    print("Lampada foi ligada")
  
  def desligar(self):
    print("Lampada foi desligada")
    
# * Televisão
class Televisao:
    def __init__(self):
        self.volume = 0
        
    def ligar(self):
      print("Televisão foi ligada")
  
    def desligar(self):
      print("Televisão foi desligada")

    def aumentar(self):
      if self.volume < 100:
        self.volume += 10
        print(f"O volume da TV foi aumentado para {self.volume}")
      else: 
        print("Volume da TV está no máximo")

    def diminuir(self):
      if self.volume > 0:
        self.volume -= 10
        print(f"O volume da TV foi diminuido para {self.volume}")
      else:
        print("Volume da TV está no mínimo")

    def trocar_canal(self):
        print(f"O canal da TV foi trocado")
    
# * Sistema de som
class SistemaDeSom:
    def __init__(self):
        self.volume = 0

    def ligar(self):
      print("Som foi ligado")
  
    def desligar(self):
      print("Som foi desligado")
    
    def aumentar(self):
      if self.volume < 100:
        self.volume += 10
        print(f"O volume do sistema de som foi aumentado para {self.volume}")
      else: 
        print("Volume do sistema de som está no máximo")

    def diminuir(self):
      if self.volume > 0:
        self.volume -= 10
        print(f"O volume do sistema de som foi diminuido para {self.volume}")
      else:
        print("Volume do sistema de som está no mínimo")

# * Controle remoto
class ControleRemoto:
  def __init__(self):
        self.comandos = []

  def registro(self, comando):
      self.comandos.append(comando)

  def execute(self):
      for comando in self.comandos:
          comando.execute()

  def undo(self):
      if self.comandos:
          self.comandos.pop().undo()
      else:
          print("Nada para desfazer")

# * Cliente
if __name__ == "__main__":
  # * Dispositivos
  LAMPADA = Lampada()
  TELEVISAO = Televisao()
  SOM = SistemaDeSom()
  
  # * Comandos
  LIGAR_LAMPADA = Ligar(LAMPADA)
  DESLIGAR_LAMPADA = Desligar(LAMPADA)
  
  LIGAR_TELEVISAO = Ligar(TELEVISAO)
  DESLIGAR_TELEVISAO = Desligar(TELEVISAO)
  AUMENTAR_VOLUME_TELEVISAO = Aumentar(TELEVISAO)
  DIMINUIR_VOLUME_TELEVISAO = Diminuir(TELEVISAO)
  TROCAR_CANAL = TrocarCanal(TELEVISAO)
  
  LIGAR_SOM = Ligar(SOM)
  DESLIGAR_SOM = Desligar(SOM)
  AUMENTAR_VOLUME_SOM = Aumentar(SOM)
  DIMINUIR_VOLUME_SOM = Diminuir(SOM)
  
  # * Controle remoto
  CONTROLE_REMOTO = ControleRemoto()
  
  # * Ações a serem feitas
  CONTROLE_REMOTO.registro(LIGAR_LAMPADA)
  CONTROLE_REMOTO.registro(DESLIGAR_LAMPADA)
  CONTROLE_REMOTO.registro(LIGAR_TELEVISAO)
  CONTROLE_REMOTO.registro(DESLIGAR_TELEVISAO)
  CONTROLE_REMOTO.registro(AUMENTAR_VOLUME_TELEVISAO)
  CONTROLE_REMOTO.registro(DIMINUIR_VOLUME_TELEVISAO)
  CONTROLE_REMOTO.registro(TROCAR_CANAL)
  CONTROLE_REMOTO.registro(LIGAR_SOM)
  CONTROLE_REMOTO.registro(DESLIGAR_SOM)
  CONTROLE_REMOTO.registro(AUMENTAR_VOLUME_SOM)
  CONTROLE_REMOTO.registro(DIMINUIR_VOLUME_SOM)
  
  # * Método que irá executar todas as ações
  CONTROLE_REMOTO.execute()
  
  # * Desfaz a ultima ação executada
  CONTROLE_REMOTO.undo()
  
# * EXPLICAÇÂO:
  # * O padrão Command é um padrão de design comportamental que permite encapsular solicitações como objetos, permitindo a parametrização de operações e fornecendo suporte para histórico e reversão de ações.
  
  # * Parametrização de operações: Refere-se à capacidade de passar diferentes parâmetros para um comando, permitindo que ele realize diferentes ações em diferentes objetos sem modificar o próprio comando. Nesse meu código cada comando, como ligar, desligar, aumentar, diminuir e trocar de canal é responsável por conhecer o objeto que irá realizar a operação. Isso permite que você crie um novo comando apenas fornecendo o dispositivo relevante.
  
  # * Histórico e reversão de ações: O controle remoto mantém uma lista de comandos executados. Quando você desfaz uma ação, ele simplesmente chama o método undo do último comando na lista. Isso permite um histórico reversível de ações, útil para desfazer e refazer operações conforme necessário.