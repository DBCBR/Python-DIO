class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
             
    def __del__(self):
        print("Removendo a instância da classe...")
        
    def latir(self):
        print('Au au au')
        
def criar_cachorro():
    c = Cachorro('Rex', 'Marrom', False)
    print(c.nome)


c = Cachorro('Rex', 'marrom')
c.latir()

print("Ola Mundo!")

del c

print("Ola Mundo!")
print("Ola Mundo!")
print("Ola Mundo!")

# criar_cachorro()