class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
                
    def buzinar(self):
        print('Plim plim plim')
        
    def parar(self):
        print('Freando...')
        print('Bicicleta parada')
        
    def pedalar(self):
        print('Pedalando...')
        print('Bicicleta em movimento')
        
    def trocar_marcha(self,nro_marcha):
        print(f'Trocando para a marcha {nro_marcha}')
           
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta('vermelha', 'Caloi', 2022, 600)
b1.buzinar()
b1.pedalar()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta('azul', 'Monark', 2021, 500)
b2.buzinar()
print(b2)
b2.trocar_marcha(3)