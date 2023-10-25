from EntidadeDB import EntidadeDB

class Avalicao(EntidadeDB):
    def __init__(self, nome, data, comentario, turma):
        super().__init__() 