class Produto:
    def __init__(self, nome, categoria, valor):
        self.nome = nome
        self.categoria = categoria
        self.valor = valor

    def __repr__(self):
        return f"{self.nome} ({self.categoria}, {self.valor:.2f})"


class ProdutoIterator:
    def __init__(self, produtos):
        self.index = 0
        # Organiza os produtos por categoria e depois por valor crescente
        self.produtos_ordenados = sorted(produtos, key=lambda p: (p.categoria, p.valor))
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.produtos_ordenados):
            produto = self.produtos_ordenados[self.index]
            self.index += 1
            return produto
        else:
            raise StopIteration


class Cliente:
    def main(self):
        produtos = [
            Produto("Prod1", "A", 99.9),
            Produto("Prod2", "B", 19.9),
            Produto("Prod3", "A", 29.9),
            Produto("Prod4", "C", 5.5),
            Produto("Prod5", "C", 20.9),
            Produto("Prod6", "A", 59.9),
            Produto("Prod7", "B", 49.9),
            Produto("Prod8", "C", 15.0),
            Produto("Prod9", "B", 10.0),
            Produto("Prod10", "A", 39.9)
        ]
        
        iterator = ProdutoIterator(produtos)
        for produto in iterator:
            print(produto)


# Criar uma instância da classe Cliente e chamar o método main
cliente = Cliente()
cliente.main()
