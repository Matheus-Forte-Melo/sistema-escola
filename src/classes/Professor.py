from UsuarioDB import UsuarioDB

class Professor(UsuarioDB):
    def __init__(self) -> None:
        self._disciplinas = None
        self._turmas_lecionadas = None

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
        query = f"CALL buscar_disciplinas_prof(%s)"
        values = (self._id,)
        self._disciplinas = self.realizarBusca(query, values)

    def getId(self):
        return self._id # Será que isso é necessário?
    
    def getNome(self,  completo=False):
        if completo:
            return f"{self._primeiro_nome} {self._sobrenome}"
        return self._primeiro_nome
    
    def getDisciplinas(self):
        return self._disciplinas

    def getTurmas(self, quant=True):
        if quant:
            return len(self._turmas_lecionadas)
        return self._turmas_lecionadas
    
    def criar_avaliacao(self, Avaliacao):
        #avaliacao = Avaliacao()
        pass

        
