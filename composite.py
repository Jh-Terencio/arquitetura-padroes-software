from abc import ABCMeta, abstractmethod, abstractstaticmethod

class ITarefa(metaclass=ABCMeta):
    def __init__(self, nome):
        self.nome = nome
        self.concluida = False
    
    @abstractmethod
    def adicionar(self, tarefa):
        """ Método de adicionar tarefa """
    
    @abstractmethod
    def remover(self, tarefa):
        """ Método de remover tarefa """
    
    @abstractmethod
    def mostrar(self, nivel):
        """ Método de mostrar tarefa """
    
    @abstractmethod
    def concluir(self):
        """ Método de concluir tarefa """
    
    @abstractmethod
    def desfazer(self):
        """ Método de desfazer tarefa """
    
class TarefaSimples(ITarefa):
    def adicionar(self, tarefa):
        """ Método de adicionar tarefa """
    
    def remover(self, tarefa):
        """ Método de remover tarefa """
    
    def mostrar(self, nivel):
        print('  ' * nivel + self.nome + " (Concluída)" if self.concluida else "  " * nivel + self.nome)
    
    def concluir(self):
        self.concluida = True
    
    def desfazer(self):
        self.concluida = False

class TarefaComposta(ITarefa):
    def __init__(self, nome):
        super().__init__(nome)
        self.subtarefas = []
    
    def adicionar(self, tarefa):
        self.subtarefas.append(tarefa)
    
    def remover(self, tarefa):
        self.subtarefas.remove(tarefa)
    
    def mostrar(self, nivel):
        print('  ' * nivel + self.nome + " (Concluída)" if self.concluida else "  " * nivel + self.nome)
        for tarefa in self.subtarefas:
            tarefa.mostrar(nivel + 1)
    
    def concluir(self):
        if all(tarefa.concluida for tarefa in self.subtarefas):
            self.concluida = True
            print(f'Tarefa {self.nome} concluída!')
        else:
            print(f'Não é possível concluir {self.nome} pois algumas subtarefas não estão concluídas.')
    
    def desfazer(self):
        self.concluida = False
        print(f'Tarefa {self.nome} desfeita!')

def main():
    # * Tarefas simples
    tarefa1 = TarefaSimples("Tarefa 1")
    tarefa2 = TarefaSimples("Tarefa 2")
    tarefa3 = TarefaSimples("Tarefa 3")
    tarefa4 = TarefaSimples("Tarefa 4")
    tarefa5 = TarefaSimples("Tarefa 5")
    tarefa6 = TarefaSimples("Tarefa 6")
    
    # * Tarefas compostas
    tarefa7 = TarefaComposta("Tarefa 7")
    tarefa8 = TarefaComposta("Tarefa 8")
    tarefa9 = TarefaComposta("Tarefa 9")
    tarefa10 = TarefaComposta("Tarefa 10")
    tarefa11 = TarefaComposta("Tarefa 11")
    tarefa12 = TarefaComposta("Tarefa 12")
    
    # * Adicionando subtarefas
    tarefa7.adicionar(tarefa1)
    tarefa7.adicionar(tarefa2)
    tarefa8.adicionar(tarefa3)
    tarefa8.adicionar(tarefa4)
    tarefa9.adicionar(tarefa5)
    tarefa9.adicionar(tarefa6)
    tarefa10.adicionar(tarefa7)
    tarefa10.adicionar(tarefa8)
    tarefa11.adicionar(tarefa9)
    tarefa12.adicionar(tarefa10)
    tarefa12.adicionar(tarefa11)
    
    # * Mostrando a estrutura das tarefas
    tarefa12.mostrar(0)
    
    # * Concluindo algumas tarefas
    tarefa1.concluir()
    tarefa2.concluir()
    tarefa3.concluir()
    tarefa5.concluir()
    
    print("\nApós concluir algumas tarefas:")
    tarefa12.mostrar(0)
    
    # * Tentando concluir uma tarefa composta antes de concluir suas subtarefas
    tarefa10.concluir()
    
    # * Concluindo as subtarefas restantes
    tarefa4.concluir()
    tarefa6.concluir()
    tarefa7.concluir()
    tarefa8.concluir()
    tarefa9.concluir()
    tarefa10.concluir()
    tarefa11.concluir()
    
    print("\nApós concluir todas as tarefas:")
    tarefa12.mostrar(0)
    
    # * Desfazendo a conclusão de algumas tarefas
    tarefa1.desfazer()
    tarefa5.desfazer()
    
    print("\nApós desfazer a conclusão de algumas tarefas:")
    tarefa12.mostrar(0)

if __name__ == "__main__":
    main()
