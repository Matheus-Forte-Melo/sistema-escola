from UsuarioDB import UsuarioDB

class Professor(UsuarioDB):
    def __init__(self) -> None:
        self.disciplinas = None
        self.turmas_lecionadas = None

    def realizarLogin(self, nome, senha):
        query = "CALL buscar_professor(%s, %s)"
        values = (nome, senha)
        atributos = self._buscar_nome_senha(query, values)
        return self._instanciar_da_tupla(atributos[0])
    
    @classmethod
    def _instanciar_da_tupla(cls, tupla):
        instancia = super()._instanciar_da_tupla(tupla)
        cls.buscar_disciplinas(instancia)
        cls.buscar_qntd_turma(instancia)
        return instancia

    def buscar_qntd_turma(self):
        query = f"CALL buscar_qnt_turmas_prof(%s);"
        values = (self.id,)
        self._iniciarConn()
        self._cursor.execute(query, values)
        self.turmas_lecionadas = self._cursor.fetchall()
        self._fecharConn()

    def buscar_disciplinas(self) -> None:
        query = f"CALL buscar_disciplinas_prof(%s)"
        values = (self.id,)
        self._iniciarConn()
        self._cursor.execute(query, values)
        self.disciplinas = self._cursor.fetchall()
        self._fecharConn()

    def getId(self):
        return self.id
    
    def getNome(self,  completo=False):
        if completo:
            return f"{self.primeiro_nome} {self.sobrenome}"
        return self.primeiro_nome
    
    def getDisciplinas(self):
        return self.disciplinas

    def getTurmas(self):
        return self.turmas_lecionadas[0][0]
        
