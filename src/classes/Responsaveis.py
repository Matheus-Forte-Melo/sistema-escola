from EntidadeDB import EntidadeDB

class Responsaveis(EntidadeDB):
    def __init__(self, primeiro_nome_1, sobrenome_1, primeiro_nome_2, sobrenome_2):
        self.primeiro_nome_1 = primeiro_nome_1
        self.sobrenome_1 = sobrenome_1
        self.primeiro_nome_2 = primeiro_nome_2
        self.sobrenome_2 = sobrenome_2

    def cadastrar(self):
        query = "SELECT cadastrar_responsaveis(%s, %s, %s, %s)"
        values = (self.primeiro_nome_1, self.sobrenome_1, self.primeiro_nome_2, self.sobrenome_2)
        self._iniciarConn()
        self._cursor.execute(query, values)
        id_responsavel = self._cursor.fetchall()
        self._conn.commit()
        self._fecharConn()
        return id_responsavel[0][0]
    
