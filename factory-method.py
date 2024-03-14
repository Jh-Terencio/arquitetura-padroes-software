from abc import ABCMeta, abstractstaticmethod

# Interface para as classes de personagens
class IPersonagem(metaclass=ABCMeta):

  @abstractstaticmethod
  def habilidades(self):
      """ Método de Habilidades """

  @abstractstaticmethod
  def equipamentos(self):
      """ Método de equipamentos """

# Implementações concretas das classes de personagens
class Guerreiro(IPersonagem):

  def habilidades(self):
      return "Ataque de fúria e corte tornado!"

  def equipamentos(self):
      return "Espada e Armadura"

class Mago(IPersonagem):

  def habilidades(self):
      return "Bola de Fogo e Capa da invisibilidade!"

  def equipamentos(self):
      return "Varinha e Robe"

class Arqueiro(IPersonagem):

  def habilidades(self):
      return "Tiro Preciso e tiro múltiplo!"

  def equipamentos(self):
      return "Arco e Flechas"

# Fábrica abstrata para criar os personagens
class IFabricaPersonagem(metaclass=ABCMeta):

  @abstractstaticmethod
  def criar_personagem(self):
      """ Método para criar personagens """

# Fábricas concretas para cada classe de personagem
class FabricaGuerreiro(IFabricaPersonagem):
  def criar_personagem(self):
      return Guerreiro()

class FabricaMago(IFabricaPersonagem):
  def criar_personagem(self):
      return Mago()

class FabricaArqueiro(IFabricaPersonagem):
  def criar_personagem(self):
      return Arqueiro()

# Cliente para testar o padrão Factory Method
class Cliente:
  def __init__(self):
    self.personagens = []

  def criar_personagem(self, fabrica):
    personagem = fabrica.criar_personagem()
    self.personagens.append(personagem)
    print(f"\nNovo personagem criado: {type(personagem).__name__}")
    print(f"Habilidade: {personagem.habilidades()}")
    print(f"Equipamento: {personagem.equipamentos()}\n")

# Testando o código
if __name__ == "__main__":
  cliente = Cliente()

  continuar = input("Deseja criar um personagem? Digite Sim para criar e Não para sair.\n")
  
  while continuar != "Não":
    personagem_escolhido = input("Escolha a classe de seu personagem (Guerreiro, Mago ou Arqueiro)\n")
  
    # Criando personagens usando as fábricas
    if personagem_escolhido == "Guerreiro":
        fabrica_guerreiro = FabricaGuerreiro()
        cliente.criar_personagem(fabrica_guerreiro)
    elif personagem_escolhido == "Mago":
        fabrica_mago = FabricaMago()
        cliente.criar_personagem(fabrica_mago)
    elif personagem_escolhido == "Arqueiro":
        fabrica_arqueiro = FabricaArqueiro()
        cliente.criar_personagem(fabrica_arqueiro)
    else:
        print("Classe escolhida não existe no sistema, por favor digite o nome da classe corretamente!")
    
    continuar = input("\nDeseja criar mais um personagem? Digite Sim para criar e Não para sair.\n")
