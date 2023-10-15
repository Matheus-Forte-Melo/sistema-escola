from UsuarioDB import UsuarioDB

class Aluno(UsuarioDB): # Herdando métodos de comunicação
    def __init__(self) -> None:
        pass

    # Retorna uma tupla com os atributos referentes ao registro do banco com a senha correspondente
    def realizarLogin(self, nome, senha):
        self.iniciarConn() 
        # Fazendo query \\ Mudar para um stored procedure eventualmente
        query = "CALL buscar_aluno(%s, %s)"
        values = (nome, senha)
        self._cursor.execute(query, values)
        atributos = self._cursor.fetchall()
        self.fecharConn()

        return self.instanciar_de_tupla(atributos[0])

    # Retorna uma instancia da classe aluno com atributos referentes a tupla
    @classmethod
    def instanciar_de_tupla(cls, tupla):
        aluno = cls()
        aluno.__matricula = tupla[0]
        aluno.__primeiro_nome = tupla[1]
        aluno.__sobrenome = tupla[2]
        aluno.__nascimento = tupla[3]
        aluno.__responsaveis = tupla[4]
        return aluno
    
    def getMatricula(self):
        return self.__matricula

    def getNome(self):
        return self.__primeiro_nome

    def getNascimento():
        pass

    def getResponsaveis():
        pass
    

# senha = "oopp12125"
# nome = "Matheus Forte de Melo"
# aluno = Aluno().realizarLogin(nome, senha)
# print(aluno.matricula)
# aluno.realizarLogin(senha)
