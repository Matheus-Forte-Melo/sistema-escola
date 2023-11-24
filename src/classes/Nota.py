from EntidadeDB import EntidadeDB

class Notas(EntidadeDB):
    def __init__(self) -> None:
        pass
    
    def buscar_notas_matricula(self, matricula, disciplina):
        query = "CALL busca_notas_matricula(%s, %s)"
        values = (matricula, disciplina)
        notas = self.realizarBusca(query, values)
        return self.copiar_notas_string(notas)
    
    @staticmethod
    def copiar_notas_string(notas):
        output = []
        comentarios = [] 
        for pos, a in enumerate(notas):
            output.append([pos + 1, str(a[0]), a[1], a[2]])
            comentarios.append(a[3])
        return (output, comentarios)
    
    # Atualmente não sendo utilizado em lugar algum
    def notas_para_dict(self, notas):
        for nota in notas:
            if nota[1] not in self.notas:
                self.notas[nota[1]] = []
            self.notas[nota[1]].append(nota[0])

    def buscar_disciplina(self, matricula):
        query = "CALL busca_disciplinas(%s)"
        values = (matricula,)
        disciplinas = self.realizarBusca(query, values)

        output = []
        for disciplina in disciplinas:
            output.append(disciplina[0])
        return output



# print("="*25, "\n")
# for pos, comentario in enumerate(comentarios):
#     print(f"\033[32m[!]\033[0mComentario da avaliação n°{pos + 1}: {comentario}\n")
# print("="*25)
