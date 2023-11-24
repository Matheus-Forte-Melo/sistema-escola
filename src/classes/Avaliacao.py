from EntidadeDB import EntidadeDB

class Avalicao(EntidadeDB):
    def __init__(self, id=0, nome="", descricao="", idProfessor=int, turma="", disciplina="") -> None:
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.idProfessor = idProfessor # Podem existir dois professores de nome igual.
        self.turma = turma # Não podem existir duas turmas de nome igual
        self.disciplina = disciplina # Não podem existir duas disciplinas de nome igual

    def buscar_notas(self):
        query = "CALL buscar_notas_avaliacao(%s)"
        values = (self.id,)
        return self.realizarBusca(query, values)

    def criar_avaliacao(self) -> None:
        query = "CALL criar_avaliacao(%s, %s, %s, %s, %s)"
        values = (self.nome, self.descricao, self.idProfessor, self.turma, self.disciplina)
        print(values)
        self._iniciarConn()
        self._cursor.execute(query, values)
        self._conn.commit()
        self._fecharConn()

    def atualizar(self): 
        values = (self.id, self.nome, self.descricao)
         # Ele faz update em todos esses valores, mudados ou não. Poderia economizar no tráfego do banco simplesmente montando uma query personalizada durante o menu de edição mas quis experiementar desse modo (aproveitar que ninguem vai usar esse sistema pra dar uma brincada com outras opções).
        query = "CALL atualizar_avaliacao(%s, %s, %s)"
        self._iniciarConn()
        self._cursor.execute(query, values)
        self._conn.commit()
        self._fecharConn()

    def deletar(self):
        query = "CALL deletar_avaliacao(%s)"
        values = (self.id,)
        self._iniciarConn()
        self._cursor.execute(query, values)
        self._conn.commit()
        self._fecharConn()
