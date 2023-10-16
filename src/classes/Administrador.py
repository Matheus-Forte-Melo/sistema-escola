from UsuarioDB import UsuarioDB

class Administrador(UsuarioDB):
    def __init__(self):
        self.__id = None
        self.__primeiro_nome = None
        self.__sobrenome = None

    def realizarLogin(self, nome, senha):
        query = "CALL buscar_adm(%s, %s)"
        values = (nome, senha)
        self._iniciarConn()
        self._cursor.execute(query, values)
        atributos = self._cursor.fetchall()
        self._cursor.close()
        return self.__instanciar_de_tupla(atributos[0])
    
    @classmethod
    def __instanciar_de_tupla(cls, tupla):
        adm = cls()
        adm.__id = tupla[0]
        adm.__primeiro_nome = tupla[1]
        adm.__sobrenome = tupla[2]
        return adm

    def getNome(self, completo=False):
        if completo:
            return f"{self.__primeiro_nome} {self.__sobrenome}"
        return self.__primeiro_nome
        




         




