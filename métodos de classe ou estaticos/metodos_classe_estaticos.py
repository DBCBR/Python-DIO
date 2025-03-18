class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod    
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior(idade):
        return idade >= 18
        
p = Pessoa.criar_de_data_nascimento(1986, 10, 16, 'David')
print(p.nome, p.idade)

print(Pessoa.e_maior(25))
print(Pessoa.e_maior(15))
