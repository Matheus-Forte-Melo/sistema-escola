from terminaltables import AsciiTable
from EntidadeDB import EntidadeDB

class Notas(EntidadeDB):
    def __init__(self) -> None:
        self.notas = {}

    @classmethod
    def instanciar_notas(cls):
        pass

    def buscar_notas_matricula(self, matricula, disciplina):
        query = "CALL busca_notas_matricula(%s, %s)"
        values = (matricula, disciplina)
        self._iniciarConn()
        self._cursor.execute(query, values)
        notas = self._cursor.fetchall()
        self._fecharConn()
        return notas
    
    @staticmethod
    def copiar_notas_string(notas):
        output = []
        comentarios = [] 
        for pos, a in enumerate(notas):
            output.append([pos + 1, str(a[0]), a[1], a[2]])
            comentarios.append(a[3])
        return (output, comentarios)
                

    def notas_para_dict(self, notas):
        for nota in notas:
            if nota[1] not in self.notas:
                self.notas[nota[1]] = []
            self.notas[nota[1]].append(nota[0])


notas = Notas()
notas_aluno = notas.buscar_notas_matricula("20231014", "Português")
notas_str, comentarios = notas.copiar_notas_string(notas_aluno)


def criarTabela(header: list, colunas) -> AsciiTable:
    dados_tabela = []
    dados_tabela.append(header)

    for coluna in colunas:
        dados_tabela.append(coluna)
    
    return AsciiTable(dados_tabela)

def printarTabela(tabela:AsciiTable) -> None:
    print(tabela.table)

tabela = criarTabela(["Número", "Nota", "Data", "Professor(a)"], notas_str)
printarTabela(tabela)
print("="*25, "\n")
for pos, comentario in enumerate(comentarios):
    print(f"\033[32m[!]\033[0mComentario da avaliação n°{pos + 1}: {comentario}\n")
print("="*25)








    