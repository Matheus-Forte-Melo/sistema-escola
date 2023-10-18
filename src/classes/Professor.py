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
    
    def buscar_disciplinas_lecionadas(self):
        pass

    def buscar_turmas_lecionadas(self):
        pass

    def getId(self):
        return self.id
    
    def getNome(self,  completo=False):
        if completo:
            return f"{self.primeiro_nome} {self.sobrenome}"
        return self.primeiro_nome
        
