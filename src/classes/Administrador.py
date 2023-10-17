from UsuarioDB import UsuarioDB

class Administrador(UsuarioDB):
    def __init__(self):
        super().__init__()
        
    def realizarLogin(self, nome, senha):
        query = "CALL buscar_adm(%s, %s)"
        values = (nome, senha)
        atributos = self._buscar_nome_senha(query, values)
        return self._instanciar_da_tupla(atributos[0]) # Desempacota a lista e deixa somente a tupla

    def getNome(self, completo=False):
        if completo:
            return f"{self.primeiro_nome} {self.sobrenome}"
        return self.primeiro_nome
        


         




