# TODO Encapsular as paradas

from UsuarioDB import UsuarioDB

class Aluno(UsuarioDB): # Herdando métodos de comunicação
    def __init__(self) -> None:
        pass

    # Retorna uma tupla com os atributos referentes ao registro do banco com a senha correspondente
    def realizarLogin(self, nome, senha):
        query = "CALL buscar_aluno(%s, %s)"
        values = (nome, senha)
        atributos = self._buscar_nome_senha(query, values)
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
        return aluno
    
    # Não tem nenhum atributo propriamente encapsulado pq vc mudar sua matricula i.e nao vai mudar nada no sistema, só vai
    # fazer você propositalmente causar erros de busca, já que essa classe não tem acesso
    # A nada que possa interferir/alterar atributos nas entranhas do banco de dados
    
    def getMatricula(self):
        return self.__matricula
    
    def getTurma(self):
        return self.__turma

    def getResponsaveis(self):
        return self.__responsaveis

    def getNome(self,  completo=False):
        if completo:
            return f"{self.__primeiro_nome} {self.__sobrenome}"
        return self.__primeiro_nome
    
    def getNascimento(self):
        return self.__nascimento



    
    
        
