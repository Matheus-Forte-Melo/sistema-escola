from EntidadeDB import EntidadeDB

class Turma(EntidadeDB):
    def __init__(self, serie="", turno="", fase="", numero=1) -> None:
        #super().__init__()
        self.serie = serie
        self.turno = turno
        self.fase = fase
        self.numero = numero
        self.integrantes = None
        self.professores = None

    # Busca turma com base na matricula de um aluno, não realiza instanciamento
    def buscar_turma_matricula(self, id):
        query = "CALL busca_turma_atual(%s)"
        values = (id,)
        atributos = self.realizarBusca(query, values)
        return atributos
    
    def buscar_turma(self, id):
        query = "CALL buscar_turma(%s)"
        values = (id,)
        atributos = self.realizarBusca(query, values)
        return atributos
    
    def publicar_banco():
        pass
    
