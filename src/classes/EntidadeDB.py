# Classe pai das subclasses que não são necessariamente atreladas a um usuário
import mysql.connector

class EntidadeDB:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def _iniciarConn(self):
        self._conn = mysql.connector.connect(
            user="root",
            password="",
            host="127.0.0.1",
            database="sistemaescolar"
        )
        self._cursor = self._conn.cursor()

    def _fecharConn(self):
        if self._conn is not None:
            self._conn.close()
            self._cursor.close()

    def realizarBusca(self, query, values):
        self._iniciarConn()
        self._cursor.execute(query, values)
        output = self._cursor.fetchall()
        self._fecharConn()
        return output

    @classmethod
    def _instanciar_da_tupla(cls, tupla):
        pass