from UsuarioDB import UsuarioDB

class Professor(UsuarioDB):
    def __init__(self) -> None:
        self._disciplinas = []
        self._turmas_lecionadas = None
        self.avaliacoes = None

    def realizarLogin(self, nome, senha):
        query = "CALL buscar_professor(%s, %s)"
        values = (nome, senha)
        atributos = self.realizarBusca(query, values)
        return self._instanciar_da_tupla(atributos[0])
    
    @classmethod
    def _instanciar_da_tupla(cls, tupla):
        instancia = super()._instanciar_da_tupla(tupla)
        cls.buscar_disciplinas(instancia)
        cls.buscar_qntd_turma(instancia)
        return instancia

    def buscar_qntd_turma(self):
        query = f"CALL buscar_turmas_prof(%s);"
        values = (self._id,)
        self._turmas_lecionadas = self.realizarBusca(query, values)

    def buscar_disciplinas(self) -> None:
        query = f"CALL buscar_disciplinas_prof(%s, %s)" # Não funciona mais por enquanto, passar outro arg -> ""
        values = (self._id, "")
        disciplinas = self.realizarBusca(query, values)
        for disciplina in disciplinas:
            self._disciplinas.append(disciplina[0]) 

    def buscar_avaliacoes(self, nome_turma:str) -> tuple:
        query = "CALL buscar_avaliacoes(%s, %s)"
        values = (self._id, nome_turma)
        self.avaliacoes = self.realizarBusca(query, values)

    def buscar_disciplinas_turma(self, nome_turma):
        output = []
        query = "CALL buscar_disciplinas_prof(%s, %s)"
        values = (self._id, nome_turma)
        disciplinas = self.realizarBusca(query, values)
        for disciplina in disciplinas:
            output.append(disciplina[0])
        return output # Da de melhorar isso, simplificar com aquilo lá em cima

    def getId(self):
        return self._id # Será que isso é necessário?!!!
    
    def getNome(self,  completo=False):
        if completo:
            return f"{self._primeiro_nome} {self._sobrenome}"
        return self._primeiro_nome
    
    def getDisciplinas(self):
        return self._disciplinas # Será que isso é necessário?

    def getTurmas(self, quant=True):
        if quant:
            return len(self._turmas_lecionadas)
        return self._turmas_lecionadas
    
    # def criar_avaliacao(self, Avaliacao):
    #     #avaliacao = Avaliacao()
    #     pass
