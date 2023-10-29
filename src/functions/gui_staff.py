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
    professor.buscar_avaliacoes(turma)
   
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
                    editar_avaliacao(professor, turma)
                case "Deletar Avaliação":
                    deletar_avaliacao(professor, turma)
                case "Voltar":
                    break

def deletar_avaliacao(professor, turma):
    auto_completer = {}
    listar_avaliacoes(professor, turma)
    for pos, avaliacao in enumerate(professor.avaliacoes):
        auto_completer[f"{pos+1}-{avaliacao[1]}"] = None
    escolha = inquirer.text(message="Qual avaliação deletar: ", completer=auto_completer).execute()

    print(professor.avaliacoes[int(escolha[0])-1]) 
    quit()

def editar_avaliacao(professor, turma): # turma
    escolhas = []
    listar_avaliacoes(professor, turma) # Possível bug de exibição caso uma descrição for muito grande
    for pos, avaliacao in enumerate(professor.avaliacoes):
        escolhas.append(f"Editar {pos+1}°: {avaliacao[1]}")
    escolhas.append("Voltar")
    acao = inquirer.select(message="O que deseja fazer", # Substituir por text completer, mt melhor, vai dar de reutilizar cod.
                           choices=escolhas).execute()
    
    if acao != "Voltar":
        avl_selecionada = professor.avaliacoes[int(acao[7])-1] # Puta gambiarra, mas funciona
        # Essa variavél é atribuida com base no número de "acao"

        edit = inquirer.checkbox(
            message="Editar:", choices=["Nome", "Descrição"],
            validate=lambda result: len(result) >= 1,
            invalid_message="Deve ter selecionado pelo menos 1",
            instruction="[BARRA DE ESPAÇO] para selecionar e [ENTER] para confirmar ").execute()
        
        avl_atualizada = input_atualizacoes_aval(list(avl_selecionada), edit)
        avaliacao = Avalicao(avl_atualizada[0], avl_atualizada[1], avl_atualizada[2])
        avaliacao.atualizar_avaliacao()
        print("Edição concluída!")

def input_atualizacoes_aval(avaliacao, edit) -> list:
    output = {}
    for value in edit:
        output[value] = inquirer.text(message=f"Insira o(a) {value}:").execute()

    if "Nome" in output.keys():
        avaliacao[1] = output["Nome"]
    if "Descrição" in output.keys():
        avaliacao[2] = output["Descrição"]
    return avaliacao

def listar_avaliacoes(professor, turma):
    professor.buscar_avaliacoes(turma) # Teóricamente isso ja foi feito | Na vdd precisa, pq atualiza o client size quando usamos essa funcao sempre q listamos. 
    dados = []
    for pos, avaliacao in enumerate(professor.avaliacoes):
        dados.append([str(pos + 1), avaliacao[1], avaliacao[3], avaliacao[2]])

    tabela = criarTabela(["Num", "Avaliação", "Disciplina","Descrição"], dados) 
    printarTabela(tabela)
    return(dados) # Não está sendo utilizado para nada

def criar_avaliacao(professor, nome_turma):
    nome = inquirer.text(message="Insira o título da avaliação:").execute()
    print("\033[32m[!]\033[0m Caso não queira inserir nenhum detalhe apenas aperte [ENTER]")
    descricao = inquirer.text(message="Insira os detalhes da avaliação:").execute()
    disciplina = inquirer.select(message="Qual disciplina",
                                 choices=professor.buscar_disciplinas_turma(nome_turma)).execute() 
    

    avaliacao = Avalicao(
        nome=nome.capitalize(),
        descricao=descricao, 
        idProfessor=professor.getId(), 
        turma=nome_turma, 
        disciplina=disciplina
        )
    confirm = inquirer.confirm(message="Confirmar?", default=True, confirm_letter="s", reject_letter="n",
                               transformer=lambda result: "SIm" if result else "Não",).execute()
    
    if confirm:
        avaliacao.criar_avaliacao()
        professor.buscar_avaliacoes(nome_turma)
    del(avaliacao)
    
def menu_gerenciar_notas(professor):
    turma = selecionar_turma(professor)
    tabela = criarTabela(["Matricula", "Nome do Aluno", "Sobrenome do Aluno"], turma)
    printarTabela(tabela)
    selecao = inquirer.select(message="O que deseja fazer",
                              choices=["Atribuir Nota Individual", "Atribuir Nota à Turma",
                                        "Editar Nota", "Voltar"]).execute()
    
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
            choices=["Ver Perfil", "Gerenciar Alunos", "Gerenciar Turmas",
                      "Gerenciar Notas", "Sair do Sistema"]).execute()

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