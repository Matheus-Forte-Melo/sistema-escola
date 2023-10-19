import mysql.connector

class Turma:
    def __init__(self) -> None:
        self.serie = None
        self.turno = None
        self.fase = None
        self.numero = None

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

    def buscarTurma(self, id):
        query = "CALL busca_turma_atual(%s)"
        values = (id,)
        self._iniciarConn()
        self._cursor.execute(query, values)
        atributos = self._cursor.fetchall()
        self._fecharConn()
        return atributos