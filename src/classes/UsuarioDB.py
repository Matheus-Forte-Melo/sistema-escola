import mysql.connector
# Esta é a classe principal de todos os usuários. Todas as 3 categorias de usuário no sistema herdam as funcionalidade desta classe

class UsuarioDB:
    def __init__(self, atributo) -> None:
        self.atributo = atributo
        self.__atributo_protegido = "Olá"
        

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

    @classmethod
    def _instanciar_da_tupla(cls, tupla):
        pass
            

user = UsuarioDB("Teste")
print(user._UsuarioDB__atributo_protegido)
# Name mangling, como q eu não sabia dessa porra ainda, entao parta tornar realmente privado
# Precisamos definir um setter (para restringir de fato) e um getter (para printar) nog
#
