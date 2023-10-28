from EntidadeDB import EntidadeDB

class Avalicao(EntidadeDB):
    def __init__(self, nome, descricao, idProfessor, turma, disciplina):
        self.nome = nome
        self.descricao = descricao
        self.idProfessor = idProfessor # Podem existir dois professores de nome igual.
        self.turma = turma # Não podem existir duas turmas de nome igual
        self.disciplina = disciplina # Não podem existir duas disciplinas de nome igual

    def criar_avaliacao(self):
        query = "CALL criar_avaliacao(%s, %s, %s, %s, %s)"
        values = (self.nome, self.descricao, self.idProfessor, self.turma, self.disciplina)
        self._iniciarConn()
        self._cursor.execute(query, values)
        self._conn.commit()
        self._fecharConn()

    def listar_avaliacoes(self):
        pass

    def editar_avaliacao(self):
        pass

    def deletar_avalicao(self):
        pass
