from gui_users import *

def menu_professor():
    professor = login(classe=Professor())
    while True:
        printarFiglet(f"{saudacoesTempo(getDataTempo())}, Professor(a)!")
        print(f"Logado(a) como: {professor.getNome(completo=True)}")
        acao = inquirer.select(
        message="O que deseja fazer", choices=["Ver Perfil", "Gerenciar Avaliações", "Gerenciar Notas", "Sair do Sistema"]).execute()

        match acao:
            case "Ver Perfil":
                ver_perfil(professor)
            case "Gerenciar Notas":
                menu_gerenciar_notas(professor)                
            case "Sair do Sistema":
                break

def menu_gerenciar_notas(professor):
    escolhas = []
    for turma_tupla in professor.getTurmas(False):
        escolhas.append(turma_tupla[1]) 
    escolhas.append("Voltar")

    selecao = inquirer.select(message="Qual turma:", choices=escolhas).execute()
    turma = Turma().buscar_turma(selecao, busca_matricula=False)
    tabela = criarTabela(["Matricula", "Nome do Aluno", "Sobrenome do Aluno"], turma)
    printarTabela(tabela)
    selecao = inquirer.select(message="O que deseja fazer",
                              choices=["Atribuir Nota Individual", "Atribuir Nota à Turma", "Editar Nota", "Voltar"]).execute()
    
    match selecao:
        case "Atribuir Nota à Turma":
            atribuir_notas_turma(turma)
        case "Atribuir Nota Individual":
            pass

def atribuir_nota(aluno):
    while True:
        try:
            print(f"\033[32m[!]\033[0m Atribuindo nota a \033[32m{aluno[1]} {aluno[2]}.\033[0m")
            nota = float(input("Digite a nota: "))
            assert nota > 0 and nota <= 10
            break
        except Exception:
            print("\033[31m[!] Erro ao inserir nota! Tente Novamente.\033[0m")

def atribuir_notas_turma(turma):
    comentario = inquirer.text(message="Descreva a avaliação:", amark="!").execute()
    for aluno in turma:
        atribuir_nota(aluno)

def atribuir_nota_aluno():
    pass

def menu_administrador():
    adm = login(classe=Administrador())
    while True:
        printarFiglet(f"{saudacoesTempo(getDataTempo())}, Admin!")
        print(f"Logado(a) como: {adm.getNome(completo=True)}")
        acao = inquirer.select(
            message="O que deseja fazer",
            choices=["Ver Perfil", "Gerenciar Alunos", "Gerenciar Turmas", "Gerenciar Notas", "Sair do Sistema"]).execute()

        match acao:
            case "Ver Perfil":
                ver_perfil(adm)                
            case "Sair do Sistema":
                break
    
def exibir_perfil_staff(staff, nome_classe):
    print(f"Id: {staff.getId()} \n", end=""
          f"Nome: {staff.getNome(True)}\n")
    if nome_classe == "Professor":
        print(f"Você leciona para {staff.getTurmas()} turmas!")
        print(f"Você leciona {len(staff.getDisciplinas())} disciplina(s): {staff.getDisciplinas()}")

def ver_perfil(instancia) -> None:
        nome_classe = instancia.__class__.__name__
        exibir_perfil_staff(instancia, nome_classe)
        printarLinha(40)
        acao = inquirer.select(message="O que deseja fazer:",
                               choices=["Voltar"]).execute()