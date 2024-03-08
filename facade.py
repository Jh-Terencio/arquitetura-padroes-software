# Explicação sobre o Facade:
# * O padrão de design Facade é utilizado para fornecer uma interface simplificada para um conjunto de interfaces em um subsistema. Ele oculta a complexidade do subsistema e fornece uma interface única para o cliente interagir, facilitando o uso do sistema.

# Pagamentos
class Pagamento:
    def processar_pagamento(self, valor):
        print(f"Pagamento efetuado com sucesso. Valor pago: R${valor:.2f}")


# Voos
class Voo:
    def __init__(self):
        self.voos_disponiveis = {
            "Rio de Janeiro": {"2024-13-12", "2024-18-11", "2024-11-05"},
            "Maragogi": {"2024-13-12", "2024-18-11", "2024-11-05"},
            "Lisboa": {"2024-13-12", "2024-18-11", "2024-11-05"}
        }

    def verifica_disponibilidade(self, data, origem, destino):
        if origem in self.voos_disponiveis and destino in self.voos_disponiveis:
            if data in self.voos_disponiveis[origem] and data in self.voos_disponiveis[destino]:
                print(f'O voo de {origem} para {destino} está disponível!')
                return True
        return False

    def reserva_voo(self):
        print(f"Voo reservado com sucesso!")


# Hoteis
class Hotel:
    def __init__(self):
        self.hoteis_disponiveis = {
            "C1": {"2024-13-12", "2024-25-12"},
            "C2": {"2024-18-11", "2024-30-11"},
            "C3": {"2024-11-05", "2024-15-05"}
        }

    def verifica_disponibilidade(self, data, cidade):
        if cidade in self.hoteis_disponiveis and data in self.hoteis_disponiveis[cidade]:
            return True
        return False

    def reserva_hotel(self, data, cidade):
        print(f'Hotel em {cidade} reservado para a data {data}!')


# Carros
class Carro:
    def __init__(self):
        self.carros_disponiveis = {
            "C1": {"2024-13-12", "2024-25-12"},
            "C2": {"2024-18-11", "2024-30-11"},
            "C3": {"2024-11-05", "2024-15-05"}
        }

    def verifica_disponibilidade(self, data, cidade):
        if cidade in self.carros_disponiveis and data in self.carros_disponiveis[cidade]:
            return True
        return False

    def alugar_carro(self, data, cidade):
        print(f'Carro em {cidade} alugado para a data {data}!')


# Facade
class FacadeViagem:
    def __init__(self):
        self.voos = Voo()
        self.hoteis = Hotel()
        self.carros = Carro()
        self.pagamento = Pagamento()

    def reservar_viagem(self, data, origem, destino, cidade):
        disponibilidade_voos = self.voos.verifica_disponibilidade(data, origem, destino)
        disponibilidade_hoteis = self.hoteis.verifica_disponibilidade(data, cidade)
        disponibilidade_carros = self.carros.verifica_disponibilidade(data, cidade)

        if disponibilidade_voos and disponibilidade_hoteis and disponibilidade_carros:
            # Todas as verificações de disponibilidade passaram, agora efetue as reservas
            self.voos.reserva_voo()
            self.hoteis.reserva_hotel(data, cidade)
            self.carros.alugar_carro(data, cidade)

            # Processa o pagamento
            valor_total = 1500.0  # Valor fictício, ajuste conforme necessário
            self.pagamento.processar_pagamento(valor_total)
            return True
        else:
            print("Reserva não efetuada por falta de disponibilidade")
            return False


# Exemplo de uso
viagem = FacadeViagem()
viagem.reservar_viagem("2024-13-12", "Rio de Janeiro", "Lisboa", "C1")
