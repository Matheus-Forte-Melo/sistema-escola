from EntidadeDB import EntidadeDB

class Avalicao(EntidadeDB):
    def __init__(self, nome, descricao, idProfessor, turma, disciplina):
        self.nome = nome
        self.descricao = descricao
        self.idProfessor = idProfessor # Podem existir dois professores de nome igual.
        self.turma = turma # Não podem existir duas turmas de nome igual
        self.disciplina = disciplina # Não podem existir duas disciplinas de nome igual

    def editar_avaliacao(self):
        pass

    def deletar_avalicao(self):
        pass

avalicao = Avalicao("Prova sobre a evolução humana", "DEFAULT", 2, "3° Ano do Ensino Médio - Matutino 1", "Biologia")

avalicao.inserir_valores()