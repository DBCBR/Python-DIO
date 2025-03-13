class Veiculo:
    def __init__(self, cor, placa, numero_de_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_de_rodas = numero_de_rodas

    def ligar_motor(self):
        print("Ligando o motor...")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_de_rodas, carregado):
        super().__init__(cor, placa, numero_de_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("preta", "ABC-1234", 2)
carro = Carro("vermelho", "XYZ-9876", 4)
caminhao = Caminhao("azul", "QWE-4567", 6, False)

print(moto)
print(carro)
print(caminhao)