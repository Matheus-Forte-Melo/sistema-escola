import mysql.connector
# Esta é a classe principal de todos os usuários. Todas as 3 categorias de usuário no sistema herdam as funcionalidade desta classe

class UsuarioDB:
    
    def realizarLogin(self): 
        pass

    def iniciarConn(self):
        self._conn = mysql.connector.connect(
            user="root",
            password = "",
            host = "127.0.0.1",
            database = "sistemaescolar"
            )
        self._cursor = self._conn.cursor()

    def fecharConn(self):
        if self._conn is not None:
            self._conn.close()
            self._cursor.close()
            

