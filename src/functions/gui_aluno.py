from gui_users import *

def menu_aluno():
    aluno = login(classe=Aluno())
    while True:
        printarFiglet(f"{saudacoesTempo(getDataTempo())}, Estudante!")
        print(f"Logado como: {aluno.getNome(completo=True)}")
        escolhas = ["Ver Perfil", "Listar Notas", "Listar Turma", "Sair do Sistema"]
        acao = input_select("O que deseja fazer:", escolhas)
        match acao:
            case "Ver Perfil":
                ver_perfil(aluno)                
            case "Listar Turma":
                listar_turma_aluno(aluno)
            case "Listar Notas":
                listar_notas_aluno(aluno)
            case "Sair do Sistema":
                break

def listar_turma_aluno(aluno):
    turma_atual = Turma().buscar_turma(aluno.getTurma(False), busca_matricula=True)
    tabela = criarTabela(["Primeiro Nome", "Sobrenome", "Nascimento"], turma_atual)
    print("A media da turma é de {} pontos")
    printarTabela(tabela)
    acao = input_select("O que deseja fazer:", ["Voltar"])

def listar_notas_aluno(aluno):
    disciplinas = Notas().buscar_disciplina(aluno.getMatricula()) # Não funciona mais, é necessário mudar o procedimento para que ele busque todas as avaliações, e depois busque a disciplina pelo uso de um join
    disciplinas.append("Voltar")
    while True:
        acao = input_select("Qual disciplina você deseja vizuaizar:", disciplinas)

        if acao != "Voltar":
            dados_colunas, comentarios = Notas().buscar_notas_matricula(aluno.getMatricula(), acao) 
            tabela = criarTabela(["Numero", "Avaliacao", "Nota", "Data", "Professor(a)"], dados_colunas)
            printarTabela(tabela)
            acao = input_select("O que desejeva fazer", ["Voltar"])
        else:
            break

        
def exibir_perfil_aluno(aluno):
    print(f"Matricula: {aluno.getMatricula()}\n"
            f"Nome: {aluno.getNome(True)}\n"
            f"Nascimento: {aluno.getNascimento()}\n"
            f"Você estuda na turma: {aluno.getTurma()}\n"
            f"Responsáveis:\n", end="" 
            f"{aluno.getResponsaveis()[0]} e {aluno.getResponsaveis()[1]}\n")
    

def ver_perfil(instancia) -> None:
        printarLinha(40)
        exibir_perfil_aluno(instancia)
        printarLinha(40)
        acao = input_select("O que deseja fazer", ["Voltar"])
        
