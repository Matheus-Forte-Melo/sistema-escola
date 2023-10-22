from gui_users import *

def menu_aluno():
    aluno = login(classe=Aluno())
    while True:
        printarFiglet(f"{saudacoesTempo(getDataTempo())}, Estudante!")
        print(f"Logado como: {aluno.getNome(completo=True)}")
        acao = inquirer.select(
            message="O que deseja fazer:",
            choices=["Ver Perfil", "Listar Notas", "Listar Turma", "Sair do Sistema",]
        ).execute()
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
    turma_atual = Turma().buscar_turma_matricula(aluno.getTurma(False))
    tabela = criarTabela(["Primeiro Nome", "Sobrenome", "Nascimento"], turma_atual)
    print("A media da turma é de {} pontos")
    printarTabela(tabela)
    acao = inquirer.select(message="O que deseja fazer:",choices=["Voltar"]).execute()

def listar_notas_aluno(aluno):
    disciplinas = Notas().buscar_disciplina(aluno.getMatricula())
    disciplinas.append("Voltar")
    while True:
        acao = inquirer.select(message="Qual disciplina deseja visualizar:",choices=disciplinas).execute()

        if acao != "Voltar":
            dados_colunas, comentarios = Notas().buscar_notas_matricula(aluno.getMatricula(), acao)
            tabela = criarTabela(["Numero", "Nota", "Data", "Professor"], dados_colunas)
            printarTabela(tabela)
            acao = inquirer.select(message="O que deseja fazer:",choices=["Voltar"]).execute()
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
        nome_classe = instancia.__class__.__name__
        printarLinha(40)
        exibir_perfil_aluno(instancia)
        printarLinha(40)
        acao = inquirer.select(message="O que deseja fazer:",
                               choices=["Voltar"]).execute()
        
