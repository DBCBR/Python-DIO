# Definição da classe base Passaro
class Passaro:
    def voar(self):
        print("Voando...")  # Método que imprime "Voando..."

# Definição da classe Pardal que herda de Passaro
class Pardal(Passaro):
    def voar(self):
        super().voar()  # Chama o método voar da classe base Passaro

# Definição da classe Avestruz que herda de Passaro
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")  # Sobrescreve o método voar para imprimir "Avestruz não voa"

# Função que aceita um objeto e chama seu método voar
def plano_de_voo(obj):
    obj.voar()  # Chama o método voar do objeto passado como argumento

# Cria uma instância de Pardal e chama plano_de_voo com ela
plano_de_voo(Pardal())  # Saída: "Voando..."

# Cria uma instância de Avestruz e chama plano_de_voo com ela
plano_de_voo(Avestruz())  # Saída: "Avestruz não voa"
