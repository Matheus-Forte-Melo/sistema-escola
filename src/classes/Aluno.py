# TODO Encapsular as paradas
#from Turma import Turma
from UsuarioDB import UsuarioDB

class Aluno(UsuarioDB): # Herdando métodos de comunicação
    def __init__(self, primeiro_nome="", sobrenome="", nascimento="", turma=0, responsaveis=0, senha="") -> None:
        self.__primeiro_nome = primeiro_nome 
        self.__sobrenome = sobrenome
        self.__nascimento = nascimento
        self.__turma = turma
        self.__responsaveis = responsaveis
        self._senha = senha

    # Retorna uma tupla com os atributos referentes ao registro do banco com a senha correspondente
    def realizarLogin(self, nome, senha):
        query = "CALL buscar_aluno(%s, %s)"
        values = (nome, senha)
        atributos = self.realizarBusca(query, values)
        return self._instanciar_de_tupla(atributos[0])

    # Retorna uma instancia da classe aluno com atributos referentes a tupla
    @classmethod
    def _instanciar_de_tupla(cls, tupla):
        # Esse metodo se comporta diferente dos demais pois seu campo de identificação é matricula,
        # Poderia fazer uma condição usando __class__.__name__ mas quero ter um exemplo de polimorfismo
        aluno = cls() 
        aluno.__matricula = tupla[0] # Eventualmente trocar por um dict se pa
        aluno.__primeiro_nome = tupla[1]
        aluno.__sobrenome = tupla[2]
        aluno.__nascimento = tupla[3]
        aluno.__turma = tupla[4]
        aluno.__responsaveis = (tupla[5], tupla[6])
        aluno.__idTurma = tupla[7]
        return aluno
    
    def getMatricula(self):
        return self.__matricula
    
    def getTurma(self, nome=True):
        if nome:
            return self.__turma
        return self.__idTurma

    def getResponsaveis(self):
        return self.__responsaveis

    def getNome(self,  completo=False):
        if completo:
            return f"{self.__primeiro_nome} {self.__sobrenome}"
        return self.__primeiro_nome
    
    def getSobrenome(self):
        return self.__sobrenome
    
    def getDataNascimento(self):
        return self.__nascimento

    def getNascimento(self):
        return self.__nascimento

    #property senha?
    