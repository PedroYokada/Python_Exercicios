class ProdutoEletronico:
    def __init__(self, nome, marca, preco):
        self.nome = nome
        self.marca = marca
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Marca: {self.marca}, Preço: {self.preco}")

class Smartphone(ProdutoEletronico):
    def __init__(self, nome, marca, preco, armazenamento):
        super().__init__(nome, marca, preco)
        self.armazenamento = armazenamento

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Armazenamento: {self.armazenamento}GB")

class Laptop(ProdutoEletronico):
    def __init__(self, nome, marca, preco, memoria_ram):
        super().__init__(nome, marca, preco)
        self.memoria_ram = memoria_ram

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Memória RAM: {self.memoria_ram}GB")

class Televisor(ProdutoEletronico):
    def __init__(self, nome, marca, preco, tamanho):
        super().__init__(nome, marca, preco)
        self.tamanho = tamanho

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Tamanho: {self.tamanho}\"")
        
# Criando instâncias de produtos eletrônicos
smartphone = Smartphone("iPhone 13", "Apple", 5999.99, 256)
laptop = Laptop("MacBook Pro", "Apple", 8999.99, 16)
televisor = Televisor("Smart TV 4K", "Samsung", 3499.99, 55)

# Testando o método exibir_informacoes() de cada produto eletrônico
smartphone.exibir_informacoes()
laptop.exibir_informacoes()
televisor.exibir_informacoes()
