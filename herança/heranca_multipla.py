class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass

leao = Leao(nro_patas=4, 
            cor_pelo="amarelo e laranja")
print(leao)

ornitorrinco = Ornitorrinco(nro_patas=4, 
                            cor_pelo="marrom", 
                            cor_bico="laranja")
print(ornitorrinco)