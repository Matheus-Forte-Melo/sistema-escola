from gui_users import *

def menu_professor():
    professor = login(classe=Professor())
    while True:
        printarFiglet(f"{saudacoesTempo(getDataTempo())}, Professor(a)!")
        print(f"Logado(a) como: {professor.getNome(completo=True)}")
        escolhas = ["Ver Perfil", "Gerenciar Avaliações", "Gerenciar Notas", "Sair do Sistema"]
        acao = input_select("O que deseja fazer", escolhas)

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
            escolhas = ["Criar Avaliação", "Editar Avaliação", "Deletar Avaliação", "Voltar"]
            acao = input_select("O que deseja fazer", escolhas)
            
            match acao:
                case "Criar Avaliação":
                    criar_avaliacao(professor, turma)
                case "Editar Avaliação":
                    editar_avaliacao(professor, turma)
                case "Deletar Avaliação":
                    deletar_avaliacao(professor, turma)
                case "Voltar":
                    break

def deletar_avaliacao(professor, turma): # Levantar erro caso botar algo que não existe
    auto_completer = {}
    listar_avaliacoes(professor, turma)
    for pos, avaliacao in enumerate(professor.avaliacoes):
        auto_completer[f"{pos+1}-{avaliacao[1]}"] = None
    auto_completer["0-Voltar"] = None
    escolha = input_text("Qual avaliacão deletar:", auto_completer)

    if escolha != "0-Voltar":
        confirmar = input_confirm(f"Confirma deleção de {professor.avaliacoes[int(escolha[0])-1]}")
        if confirmar:
            avl = professor.avaliacoes[int(escolha[0])-1]
            avaliacao = Avalicao(avl[0])
            avaliacao.deletar()
            print("--> Deleção concluída! <---")
            sleep(1)

    print("--> Voltando! <---")
    sleep(0.5)

def editar_avaliacao(professor, turma): # Levantar erro caso botar algo que não existe
    auto_completer = {}
    listar_avaliacoes(professor, turma)
    for pos, avaliacao in enumerate(professor.avaliacoes):
        auto_completer[f"{pos+1}-{avaliacao[1]}"] = None
    auto_completer["0-Voltar"] = None
    acao = input_text("O que deseja fazer", autocomplete=auto_completer) 
    
    if acao != "0-Voltar":
        avl_selecionada = professor.avaliacoes[int(acao[7])-1] # Puta gambiarra, mas funciona
        # Essa variavél é atribuida com base no número de "acao"
        edit = input_checkbox("Editar", ["Nome", "Descrição"])
        
        avl_atualizada = input_atualizacoes_aval(list(avl_selecionada), edit)
        avaliacao = Avalicao(avl_atualizada[0], avl_atualizada[1], avl_atualizada[2])
        avaliacao.atualizar()
        print("--> Edição concluída! <---")
        sleep(1)

    print("--> Voltando! <---")
    sleep(0.5)

def input_atualizacoes_aval(avaliacao, edit) -> list:
    output = {}
    for value in edit:
        output[value] = input_text(f"Insira o(a) {value}:") 

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
    nome = input_text("Insira o título da avaliação:")
    print("Passei por aqui")
    print("\033[32m[!]\033[0m Caso não queira inserir nenhum detalhe apenas aperte [ENTER]")
    descricao = input_text("Insira os detalhes da avaliação:")
    disciplina = input_select("Qual disciplina", professor.buscar_disciplinas_turma(nome_turma))
    

    avaliacao = Avalicao(
        nome=nome.capitalize(), descricao=descricao, idProfessor=professor.getId(), 
        turma=nome_turma, disciplina=disciplina)
    confirm = input_confirm("Deseja confirmar:")
    
    if confirm:
        avaliacao.criar_avaliacao()
        professor.buscar_avaliacoes(nome_turma)
        print("--> Criação concluída! <---")
        sleep(1)

    print("--> Voltando! <---")
    sleep(0.5)
    del(avaliacao)
    
def menu_gerenciar_notas(professor):
    turma = selecionar_turma(professor)
    tabela = criarTabela(["Matricula", "Nome do Aluno", "Sobrenome do Aluno"], turma)
    printarTabela(tabela)
    escolhas = ["Atribuir Nota Individual", "Atribuir Nota à Turma","Editar Nota", "Voltar"]
    selecao = input_select("O que deseja fazer:", escolhas)
    
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

    selecao = input_select("Qual turma:", escolhas)
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
    comentario = input_text("Descreveva a avaliação: ", simbolo="!")
    for aluno in turma:
        atribuir_nota(aluno)

def atribuir_nota_aluno():
    pass

def menu_administrador():
    adm = login(classe=Administrador())
    while True:
        printarFiglet(f"{saudacoesTempo(getDataTempo())}, Admin!")
        print(f"Logado(a) como: {adm.getNome(completo=True)}")
        escolhas = ["Ver Perfil", "Gerenciar Alunos", "Gerenciar Turmas", "Gerenciar Notas", "Sair do Sistema"]
        acao = input_select("O que deseja fazer", escolhas)

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
        acao = input_select("O que deseja fazer", ["Voltar"])