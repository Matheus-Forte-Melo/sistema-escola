from UsuarioDB import UsuarioDB

class Professor(UsuarioDB):
    def __init__(self) -> None:
        self.__id = None
        self.__primeiro_nome = None
        self.__sobrenome = None
        self.__disciplinas = None
        self.__turmas_lecionadas = None

    def realizarLogin(self, nome, senha):
        self._iniciarConn()
        query = "CALL buscar_professor(%s, %s)"
        values = (nome, senha)
        self._cursor.execute(query, values)
        atributos = self._cursor.fetchall()
        self._fecharConn()
        return self.__instanciar_de_tupla(atributos[0])

    @classmethod
    def __instanciar_de_tupla(cls, tupla):
        professor = cls()
        professor.__id = tupla[0]
        professor.__primeiro_nome = tupla[1]
        professor.__sobrenome = tupla[2]
        return professor
    
    def buscar_disciplinas_lecionadas(self):
        pass

    def buscar_turmas_lecionadas(self):
        pass

    def getNome(self,  completo=False):
        if completo:
            return f"{self.__primeiro_nome} {self.__sobrenome}"
        return self.__primeiro_nome
        
nome = "Raquel Ely Legal"
senha = "loveenglish123"
professor = Professor().realizarLogin(nome, senha)
print(professor)
