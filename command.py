from abc import ABCMeta, abstractstaticmethod

#Icommand Interface
class ICommand(metaclass=ABCMeta):
  
  @abstractstaticmethod
  def execute():
    """Método de uma interface estática"""
    
# Lampada
class Lampada:
  
  def ligar_lampada(self):
    print("Lampada foi ligada")
  
  def desligar_lampada(self):
    print("Lampada foi desligada")
    
# Comandos de lampada
class LigarLampada(ICommand):
  def __init__(self, lampada):
    self._lampada = lampada
    
  def execute(self):
    self._lampada.ligar_lampada()

class DesligarLampada(ICommand):
  def __init__(self, lampada):
    self._lampada = lampada
    
  def execute(self):
    self._lampada.desligar_lampada()

# Televisão
class Televisao:
    def __init__(self):
        self.volume = 0
        
    def ligar_televisao(self):
      print("Televisão foi ligada")
  
    def desligar_televisao(self):
      print("Televisão foi desligada")

    def aumentar_volume_televisao(self):
      if self.volume < 100:
        self.volume += 10
        print(f"O volume da TV foi aumentado para {self.volume}")
      else: 
        print("Volume da TV está no máximo")

    def diminuir_volume_televisao(self):
      if self.volume > 0:
        self.volume -= 10
        print(f"O volume da TV foi diminuido para {self.volume}")
      else:
        print("Volume da TV está no mínimo")

    def trocar_canal(self):
        print(f"O canal da TV foi trocado")

# Comandos de Televisão
class LigarTelevisao(ICommand):
  def __init__(self, televisao):
    self._televisao = televisao
    
  def execute(self):
    self._televisao.ligar_televisao()

class DesligarTelevisao(ICommand):
  def __init__(self, televisao):
    self._televisao = televisao
    
  def execute(self):
    self._televisao.desligar_televisao()

class AumentarVolumeTelevisao(ICommand):
  def __init__(self, televisao):
    self._televisao = televisao
    
  def execute(self):
    self._televisao.aumentar_volume_televisao()

class DiminuirVolumeTelevisao(ICommand):
  def __init__(self, televisao):
    self._televisao = televisao
    
  def execute(self):
    self._televisao.diminuir_volume_televisao()

class TrocarCanal(ICommand):
  def __init__(self, televisao):
    self._televisao = televisao
    
  def execute(self):
    self._televisao.trocar_canal()
    
# Sistema de som
class SistemaDeSom:
    def __init__(self):
        self.volume = 0

    def ligar_som(self):
      print("Som foi ligado")
  
    def desligar_som(self):
      print("Som foi desligado")
    
    def aumentar_volume_som(self):
      if self.volume < 100:
        self.volume += 10
        print(f"O volume do sistema de som foi aumentado para {self.volume}")
      else: 
        print("Volume do sistema de som está no máximo")

    def diminuir_volume_som(self):
      if self.volume > 0:
        self.volume -= 10
        print(f"O volume do sistema de som foi diminuido para {self.volume}")
      else:
        print("Volume do sistema de som está no mínimo")

# Comandos de Som
class LigarSom(ICommand):
  def __init__(self, som):
    self._som = som
    
  def execute(self):
    self._som.ligar_som()

class DesligarSom(ICommand):
  def __init__(self, som):
    self._som = som
    
  def execute(self):
    self._som.desligar_som()

class AumentarVolumeSom(ICommand):
  def __init__(self, som):
    self._som = som
    
  def execute(self):
    self._som.aumentar_volume_som()

class DiminuirVolumeSom(ICommand):
  def __init__(self, som):
    self._som= som
    
  def execute(self):
    self._som.diminuir_volume_som()

# Invocador
class ControleRemoto:
  def __init__(self):
    self._comandos = {}
    
  def register(self, nome_comando, comando):
    self._comandos[nome_comando] = comando
  
  def execute(self, nome_comando):
    if nome_comando in self._comandos:
      self._comandos[nome_comando].execute()
    else:
      print("Comando não encontrado")

#Cliente
if __name__ == "__main__":
  # Dispositivos
  LAMPADA = Lampada()
  TELEVISAO = Televisao()
  SOM = SistemaDeSom()
  
  # Comandos
  LIGAR_LAMPADA = LigarLampada(LAMPADA)
  DESLIGAR_LAMPADA = DesligarLampada(LAMPADA)
  
  LIGAR_TELEVISAO = LigarTelevisao(TELEVISAO)
  DESLIGAR_TELEVISAO = DesligarTelevisao(TELEVISAO)
  AUMENTAR_VOLUME_TELEVISAO = AumentarVolumeTelevisao(TELEVISAO)
  DIMINUIR_VOLUME_TELEVISAO = DiminuirVolumeTelevisao(TELEVISAO)
  TROCAR_CANAL = TrocarCanal(TELEVISAO)
  
  LIGAR_SOM = LigarSom(SOM)
  DESLIGAR_SOM = DesligarSom(SOM)
  AUMENTAR_VOLUME_SOM = AumentarVolumeSom(SOM)
  DIMINUIR_VOLUME_SOM = DiminuirVolumeSom(SOM)
  
  # Controle remoto
  CONTROLE_REMOTO = ControleRemoto()
  
  CONTROLE_REMOTO.register("Ligar lampada", LIGAR_LAMPADA)
  CONTROLE_REMOTO.register("Desligar lampada", DESLIGAR_LAMPADA)
  CONTROLE_REMOTO.register("Ligar televisão", LIGAR_TELEVISAO)
  CONTROLE_REMOTO.register("Desligar televisão", DESLIGAR_TELEVISAO)
  CONTROLE_REMOTO.register("Aumentar volume televisão", AUMENTAR_VOLUME_TELEVISAO)
  CONTROLE_REMOTO.register("Diminuir volume televisão", DIMINUIR_VOLUME_TELEVISAO)
  CONTROLE_REMOTO.register("Trocar de canal", TROCAR_CANAL)
  CONTROLE_REMOTO.register("Ligar sistema de som", LIGAR_SOM)
  CONTROLE_REMOTO.register("Desligar sistema de som", DESLIGAR_SOM)
  CONTROLE_REMOTO.register("Aumentar volume sistema de som", AUMENTAR_VOLUME_SOM)
  CONTROLE_REMOTO.register("Diminuir volume sistema de som", DIMINUIR_VOLUME_SOM)
  
  CONTROLE_REMOTO.execute("Ligar lampada")
  CONTROLE_REMOTO.execute("Desligar lampada")
  CONTROLE_REMOTO.execute("Ligar televisão")
  CONTROLE_REMOTO.execute("Desligar televisão")
  CONTROLE_REMOTO.execute("Aumentar volume televisão")
  CONTROLE_REMOTO.execute("Diminuir volume televisão")
  CONTROLE_REMOTO.execute("Trocar de canal")
  CONTROLE_REMOTO.execute("Ligar sistema de som")
  CONTROLE_REMOTO.execute("Desligar sistema de som")
  CONTROLE_REMOTO.execute("Aumentar volume sistema de som")
  CONTROLE_REMOTO.execute("Diminuir volume sistema de som")