# https://www.youtube.com/watch?v=bCQrN8qCxiU

class Animal:
    def __init__(self):
        pass
    
    def fazerSom(self):
        print("Animais não fazem apenas um som, instâncie uma subclasse.") # Não precisa de construtor pq nao vou usar nenhum atributo novo. E nem nenhum tipo de super construtor. Só preciso dos métodos

class Cachorro(Animal):
    pass # Não precisa de construtor pq nao vou usar nenhum atributo novo. E nem nenhum tipo de super construtor. Só preciso dos métodos

    def fazerSom(self):
        print("Au Au, Woof Woof")

class Gato(Animal):
    pass

    def fazerSom(self):
        print("Miau Meow UwU Purr")


