from abc import ABCMeta, abstractstaticmethod

class IEstrategia(metaclass=ABCMeta):
  
  @abstractstaticmethod
  def comportamento(self):
    """ Método de Habilidades """
  
  @abstractstaticmethod
  def nivel_atributo(self):
    """ Método de Habilidades """

class Agressividade(IEstrategia):
  
  def __init__(self, nivel):
    self.nivel = nivel
  
  def comportamento(self):
    print("Ataque agressivo ao inimigo!")
  
  def nivel_atributo(self):
    print(f"Força de ataque: {self.nivel}")

class Defensiva(IEstrategia):
  
  def __init__(self, nivel):
    self.nivel = nivel
  
  def comportamento(self):
    print("Defesa para proteção das tropas")
  
  def nivel_atributo(self):
    print(f"Nível de defesa: {self.nivel}")

class DefinirEstratégia(IEstrategia):
  
  def __init__(self, nivel):
    self.nivel = nivel
  
  def comportamento(self):
    print("Retirar tropas para planejar estratégia")
  
  def nivel_atributo(self):
    print(f"Nível de inteligência: {self.nivel}")
    
class Flanquemaneto(IEstrategia):
  
  def __init__(self, nivel):
    self.nivel = nivel
  
  def comportamento(self):
    print("Flanquear inimigos")
  
  def nivel_atributo(self):
    print(f"Nível de flanqueamento: {self.nivel}")


class BaseMilitar:
  def __init__(self, habilidade):
    self.habilidade = habilidade
    
  def acao(self):
    self.habilidade.comportamento()
    
  def atributos(self):
    self.habilidade.nivel_atributo()


# Testando o código
if __name__ == "__main__":

    acao = input("Sua tropa está indo ao campo de batalha, o que deseja fazer?\n[1]Atacar inimigos\n[2]Se defender dos inimigos\n[3]Definir estratégia de ataque\n[4]Flanquer inimigos\n")
      
    # Criando personagens usando as fábricas
    if acao == "1":
      nivel = input("\nDigite o nível de força do ataque: ")
      tropa = BaseMilitar(Agressividade(nivel))
      tropa.acao()
      tropa.atributos()
    elif acao == "2":
      nivel = input("\nDigite o nível de força da defesa: ")
      tropa = BaseMilitar(Defensiva(nivel))
      tropa.acao()
      tropa.atributos()
    elif acao == "3":
      nivel = input("\nDigite o nível de inteligência: ")
      tropa = BaseMilitar(DefinirEstratégia(nivel))
      tropa.acao()
      tropa.atributos()
    elif acao == "4":
      nivel = input("\nDigite o nível de força do flanqueamento: ")
      tropa = BaseMilitar(Flanquemaneto(nivel))
      tropa.acao()
      tropa.atributos()
    
