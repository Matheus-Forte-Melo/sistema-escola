from EntidadeDB import EntidadeDB

class Turma(EntidadeDB):
    def __init__(self, serie="", turno="", fase="", numero=1) -> None:
        #super().__init__()
        self.serie = serie
        self.turno = turno
        self.fase = fase
        self.numero = numero
        self.integrantes = None
        self.professores = None

    def buscar_todas_turmas(self): # Se o nome da classe for adm permitir usar isso?
        query = 'SELECT id, CONCAT(serie, "° Ano do ", fase, " - ", turno, " ", numero) FROM turmas'  
        self._iniciarConn()
        self._cursor.execute(query)
        return self._cursor.fetchall()

    # Busca os registros de uma turma com base na matricula de um aluno ou nome da turma.
    def buscar_turma(self, valor, busca_matricula=True):
        if busca_matricula:
            query = "CALL buscar_turma_por_matricula(%s)"
        else:
            query = "CALL buscar_turma_pelo_nome(%s)"
        values = (valor,)
        return self.realizarBusca(query, values)


