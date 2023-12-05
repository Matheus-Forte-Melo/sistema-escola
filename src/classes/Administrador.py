from UsuarioDB import UsuarioDB
from Aluno import Aluno

class Administrador(UsuarioDB):
    def __init__(self):
        super().__init__()
        
    def realizarLogin(self, nome, senha):
        query = "CALL buscar_adm(%s, %s)"
        values = (nome, senha)
        atributos = self.realizarBusca(query, values)
        return self._instanciar_da_tupla(atributos[0]) # Desempacota a lista e deixa somente a tupla

    def getId(self):
        return self.id
    
    def getNome(self,  completo=False):
        if completo:
            return f"{self.primeiro_nome} {self.sobrenome}"
        return self.primeiro_nome

    def matricular_estudante(self, aluno): # Aluno ----> vai receber Instância de aluno
        query = "CALL matricular_aluno(%s, %s, %s, %s, %s, %s)"
        values = (aluno.getNome(), aluno.getSobrenome(), aluno.getDataNascimento(), aluno.getTurma(), aluno.getResponsaveis(), aluno._senha)
        self._iniciarConn()
        self._cursor.execute(query, values)
        self._conn.commit()
        self._fecharConn()

    def transferir_estudante(self, aluno, turma):
        pass


    # def criar_turma(self, turma):
    #     pass

    # def editar_turma(self, turma):
    #     pass

    # def deletar_turma(self, turma):
    #     pass
         




