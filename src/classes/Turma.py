from EntidadeDB import EntidadeDB

class Turma(EntidadeDB):
    def __init__(self) -> None:
        super().__init__()
        self.serie = None
        self.turno = None
        self.fase = None
        self.numero = None
        self.integrantes = None
        self.professores = None

    # Busca turma com base na matricula de um aluno, não realiza instanciamento
    def buscar_turma_matricula(self, id):
        query = "CALL busca_turma_atual(%s)"
        values = (id,)
        self._iniciarConn()
        self._cursor.execute(query, values)
        atributos = self._cursor.fetchall()
        self._fecharConn()
        return atributos
    