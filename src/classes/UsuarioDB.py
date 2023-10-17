import mysql.connector
# Esta é a classe principal de todos os usuários. Todas as 3 categorias de usuário no sistema herdam as funcionalidade desta classe

class UsuarioDB:
    def __init__(self) -> None:
        self.id = None
        self.primeiro_nome = None
        self.sobrenome = None

    def _realizarLogin(self): 
        pass

    def _iniciarConn(self):
        self._conn = mysql.connector.connect(
            user="root",
            password = "",
            host = "127.0.0.1",
            database = "sistemaescolar"
            )
        self._cursor = self._conn.cursor()

    def _fecharConn(self):
        if self._conn is not None:
            self._conn.close()
            self._cursor.close()

    # Usado para buscar no banco de dados os atributos conforme a senha e nome indicados
    def _buscar_nome_senha(self, query, values) -> list:
        self._iniciarConn()
        self._cursor.execute(query, values)
        atributos = self._cursor.fetchall()
        self._cursor.close()
        return atributos

    @classmethod
    def _instanciar_da_tupla(cls, tupla):
        instancia = cls()
        instancia.id = tupla[0]
        instancia.primeiro_nome = tupla[1]
        instancia.sobrenome = tupla[2]
        return instancia
            
# E se eu botar getteres and setters aq?
# Get nome, get sobrenome, get id

