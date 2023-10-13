class Classe:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def metodo(self):
        return "Teste"

class Classe2:
    def __init__(self, escola) -> None:
        self.escola = escola

    def metodo2(self):
        return "Teste2"

class SubClasse(Classe):
    def __init__(self) -> None:
        pass

classe = Classe("José", 54)
classe2 = Classe2("Alvino Tribess")
subclasse = SubClasse()
print(subclasse.metodo())

print(subclasse.__dict__)
# print(subclasse.metodo2())


# class SubClasse(Classe):
#     def __init__(self) -> None: # Dá de herdar só os métodos, so fazer outro construtor, ele vai dar override porque ele vê primeiro no instance level
#         pass