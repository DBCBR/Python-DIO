from abc import ABC, abstractmethod

# Definição da classe abstrata ControleRemoto
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass  # Método abstrato que deve ser implementado pelas subclasses
    
    @abstractmethod
    def desligar(self):
        pass  # Método abstrato que deve ser implementado pelas subclasses
    
    @property
    @abstractmethod
    def marca(self):
        pass  # Propriedade abstrata que deve ser implementada pelas subclasses

# Definição da classe ControleTv que herda de ControleRemoto
class ControleTv(ControleRemoto):
    def ligar(self):
        print('Ligando a TV...')
        print('TV ligada!')
    
    def desligar(self):
        print('Desligando a TV...')
        print('TV desligada!')
    
    @property    
    def marca(self):
        return 'Samsung'

# Definição da classe ControleArCondicionado que herda de ControleRemoto
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o ar condicionado...')
        print('Ar condicionado ligado!')
    
    def desligar(self):
        print('Desligando o ar condicionado...')
        print('Ar condicionado desligado!')
        
    @property    
    def marca(self):
        return 'LG'

# Cria uma instância de ControleTv e chama seus métodos
controle = ControleTv()
controle.ligar()
controle.desligar()

# Cria uma instância de ControleArCondicionado e chama seus métodos
controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
