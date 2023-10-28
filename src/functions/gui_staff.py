from gui_users import *

def menu_professor():
    professor = login(classe=Professor())
    while True:
        printarFiglet(f"{saudacoesTempo(getDataTempo())}, Professor(a)!")
        print(f"Logado(a) como: {professor.getNome(completo=True)}")
        acao = inquirer.select(
            message="O que deseja fazer",
            choices=["Ver Perfil", "Gerenciar Avaliações", "Gerenciar Notas", "Sair do Sistema"]
            ).execute()

        match acao:
            case "Ver Perfil":
                ver_perfil(professor)
            case "Gerenciar Avaliações":
                menu_gerenciar_avaliacoes(professor)
            case "Gerenciar Notas":
                menu_gerenciar_notas(professor)                
            case "Sair do Sistema":
                break

def menu_gerenciar_avaliacoes(professor):
    turma = selecionar_turma(professor, registros=False)
    if turma != "Voltar":
        while True:
            print("\033[31m[!] Para mudar a turma volte e entre neste menu novamente.\033[0m")
            print(f"\033[32mGerenciando avaliações da turma: {turma}!\033[0m")
            acao = inquirer.select(message="O que deseja fazer",
            choices=["Criar Avaliação", "Editar Avaliação", "Deletar Avaliação", "Voltar"]).execute()
            
            match acao:
                case "Criar Avaliação":
                    criar_avaliacao(professor, turma)
                case "Editar Avaliação":
                    pass
                case "Deletar Avaliação":
                    pass
                case "Voltar":
                    break

def criar_avaliacao(professor, turma):
    nome = inquirer.text(message="Insira o título da avaliação:").execute()
    print("\033[32m[!]\033[0m Caso não queira inserir nenhum detalhe apenas aperte [ENTER]")
    descricao = inquirer.text(message="Insira os detalhes da avaliação:").execute()
    disciplina = inquirer.select(message="Qual disciplina",choices=professor.getDisciplinas()).execute()

    avaliacao = Avalicao(nome.capitalize(), descricao, professor.getId(), turma, disciplina)
    confirm = inquirer.confirm(message="Confirmar?", default=True, confirm_letter="s", reject_letter="n",
                               transformer=lambda result: "SIm" if result else "Não",).execute()
    
    if confirm:
        avaliacao.criar_avaliacao()
    del(avaliacao)
    
def menu_gerenciar_notas(professor):
    turma = selecionar_turma(professor)
    tabela = criarTabela(["Matricula", "Nome do Aluno", "Sobrenome do Aluno"], turma)
    printarTabela(tabela)
    selecao = inquirer.select(message="O que deseja fazer",
                              choices=["Atribuir Nota Individual", "Atribuir Nota à Turma", "Editar Nota", "Voltar"]).execute()
    
    match selecao:
        case "Atribuir Nota à Turma":
            atribuir_notas_turma(turma)
        case "Atribuir Nota Individual":
            pass

# Seleciona uma turma. Retorna os registros dela se registros = True e apenas a selecao se False
def selecionar_turma(professor, registros=True):
    escolhas = []
    for turma_tupla in professor.getTurmas(False):
        escolhas.append(turma_tupla[1]) 
    escolhas.append("Voltar")

    selecao = inquirer.select(message="Qual turma:", choices=escolhas).execute()
    if registros:
        return Turma().buscar_turma(selecao, busca_matricula=False)
    return selecao

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