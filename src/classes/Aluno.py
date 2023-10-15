from UsuarioDB import UsuarioDB

class Aluno(UsuarioDB): # Herdando métodos de comunicação
    def __init__(self) -> None:
        pass

    def realizarLogin(self, senha):
        self.iniciarConn() 
        # Fazendo query
        query = "SELECT matricula, primeiro_nome, sobrenome, nascimento, responsaveis FROM alunos WHERE `senha` = %s"
        values = (senha,)
        self._cursor.execute(query, values)
        atributos = self._cursor.fetchall()
        self.fecharConn()

        return self.instanciar_de_tupla(atributos[0])
        
    @classmethod
    def instanciar_de_tupla(cls, tupla):
        aluno = cls()
        aluno.__matricula = tupla[0]
        aluno.__primeiro_nome = tupla[1]
        aluno.__sobrenome = tupla[2]
        aluno.__nascimento = tupla[3]
        aluno.__responsaveis = tupla[4]
        return aluno


# senha = "oopp12125"
# aluno = Aluno().realizarLogin(senha)
# print(aluno.matricula)
# aluno.realizarLogin(senha)
