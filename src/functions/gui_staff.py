from gui_users import *

def menu_professor():
    professor = login(classe=Professor())
    while True:
        printarFiglet(f"{saudacoesTempo(getDataTempo())}, Professor(a)!")
        print(f"Logado(a) como: {professor.getNome(completo=True)}")
        escolhas = ["Ver Perfil", "Gerenciar Avaliações/Notas", "Sair do Sistema"]
        acao = input_select("O que deseja fazer", escolhas)

        match acao:
            case "Ver Perfil":
                ver_perfil(professor)
            case "Gerenciar Avaliações/Notas":
                turma = selecionar_turma(professor, registros=True)
                if turma[1] != "Voltar":
                    menu_gerenciar_avaliacoes_notas_1(professor, turma)           
            case "Sair do Sistema":
                break

def menu_gerenciar_avaliacoes_notas_1(professor, turma):
    avaliacao = "\033[31m[!] Não definida. Para prosseguir defina-a\033[0m"
    indefinir = False
    opcoes = ["Definir avaliação", Separator(), "Criar nova avaliação" , "Trocar turma", Separator(), "Voltar"]
    while True:
        print("[!] Selecione uma turma para gerenciar suas notas e avaliações")
        print(f"\033[33m>>> Turma selecionada: {turma[1]}\033[0m")
        sleep(0.50)
        print(f"\033[33m>>> Avaliação selecionada: {avaliacao}\033[0m")
        sleep(0.65)
        acao = input_select("O que deseja fazer:", opcoes)
        
        match acao:
            case "Trocar turma":
                turma = selecionar_turma(professor, registros=True)
            case "Criar nova avaliação":
                indefinir = criar_avaliacao(professor, turma[1])
            case "Definir avaliação":
                professor.buscar_avaliacoes(turma[1])
                avaliacao = selecionar_avaliacao(professor, turma[1])
            case "Definir outra avaliação":
                professor.buscar_avaliacoes(turma[1])
                avaliacao = selecionar_avaliacao(professor, turma[1])
            case "Gerenciar avaliação selecionada":
                indefinir = menu_gerenciar_avaliacoes(professor, turma[1], avaliacao)
            case "Atribuir nota a avaliação selecionada":
                pass
            case "Voltar":
                break
        
        if avaliacao == "0-Pular" or turma == "Voltar" or indefinir:
            avaliacao = "\033[31m[!] Não definida. Para prosseguir defina-a\033[0m"
            opcoes = ["Definir avaliação", Separator(), "Criar nova avaliação" , "Trocar turma", Separator(), "Voltar"]
            indefinir = False
        else:
            opcoes = ["Definir outra avaliação", "Gerenciar avaliação selecionada",
                        "Atribuir nota a avaliação selecionada", "Voltar"]

def menu_gerenciar_avaliacoes(professor, turma, avaliacao): 
    while True:
        professor.buscar_avaliacoes(turma)
        print(professor.avaliacoes)
        print(avaliacao)
        print(f"\033[32mGerenciando avaliação {avaliacao} da turma: {turma}!\033[0m")
        escolhas = ["Editar Avaliação", "Deletar Avaliação", "Voltar"]
        acao = input_select("O que deseja fazer", escolhas)
        
        match acao:
            case "Editar Avaliação":
                editar_avaliacao(professor, turma, avaliacao)
            case "Deletar Avaliação":
                deletado = deletar_avaliacao(professor, turma, avaliacao)
                return deletado
            case "Voltar":
                break

def completer_aval(professor, turma, mensagem="", avanco="") -> str:
    auto_completer = {}
    listar_avaliacoes(professor, turma)
    for pos, avaliacao in enumerate(professor.avaliacoes):
        auto_completer[f"{pos+1}-{avaliacao[1]}"] = None
    auto_completer[f"0-{avanco}"] = None
    return input_text(mensagem, auto_completer) # deixar mais dinamico

def deletar_avaliacao(professor, turma, avaliacao) -> bool: # Levantar erro caso botar algo que não existe  
    confirmar = input_confirm(f"Confirma deleção de {professor.avaliacoes[int(avaliacao[0])-1]}")
    if confirmar:
        avl = professor.avaliacoes[int(avaliacao[0])-1]
        avaliacao_obj = Avalicao(avl[0])
        avaliacao_obj.deletar()
        print("--> Deleção concluída! <---")
        sleep(1)
        return True

    print("--> Voltando! <---")
    sleep(0.5)
    return False

def editar_avaliacao(professor, turma, avaliacao_selecionada): # Levantar erro caso botar algo que não existe
    avl = professor.avaliacoes[int(avaliacao_selecionada[0])-1]
    edit = input_checkbox("Editar", ["Nome", "Descrição"])
    avl_atualizada = input_atualizacoes_aval(list(avl), edit)
    avaliacao = Avalicao(avl_atualizada[0], avl_atualizada[1], avl_atualizada[2])
    avaliacao.atualizar()
   
    print("--> Edição concluída! <---")
    sleep(1)
    print("--> Voltando! <---")
    sleep(0.35)

def input_atualizacoes_aval(avaliacao, edit) -> list:
    output = {}
    for value in edit:
        output[value] = input_text(f"Insira o(a) {value}:") 

    if "Nome" in output.keys():
        avaliacao[1] = output["Nome"]
    if "Descrição" in output.keys():
        avaliacao[2] = output["Descrição"].strip()
    return avaliacao # Me superei nessa, unica coisa que tá organizada nessa caralha de código

def listar_avaliacoes(professor, turma):
    professor.buscar_avaliacoes(turma)  
    dados = []
    for pos, avaliacao in enumerate(professor.avaliacoes):
        dados.append([str(pos + 1), avaliacao[1], avaliacao[3], avaliacao[2]])

    tabela = criarTabela(["Num", "Avaliação", "Disciplina","Descrição"], dados) 
    printarTabela(tabela)
    return(dados) # Não está sendo utilizado para nada

def criar_avaliacao(professor, nome_turma):
    nome = input_text("Insira o título da avaliação:")
    print("\033[32m[!]\033[0m Caso não queira inserir nenhum detalhe apenas aperte [ENTER]")
    descricao = input_text("Insira os detalhes da avaliação:")
    disciplina = input_select("Qual disciplina", professor.buscar_disciplinas_turma(nome_turma))
    
    avaliacao = Avalicao(
        nome=nome.capitalize(), descricao=descricao, idProfessor=professor.getId(), 
        turma=nome_turma, disciplina=disciplina)
    confirm = input_confirm("Deseja confirmar:")
    
    if confirm:
        print(avaliacao.nome, avaliacao.descricao, avaliacao.idProfessor, avaliacao.turma, avaliacao.disciplina)
        avaliacao.criar_avaliacao()
        professor.buscar_avaliacoes(nome_turma)
        print("--> Criação concluída! <---")
        sleep(1)
        return True

    print("--> Voltando! <---")
    sleep(0.5)
    return False
    
def menu_gerenciar_notas(professor):
    turma = selecionar_turma(professor, registros=True) 
    avaliacao = selecionar_avaliacao(professor, turma[1])
    tabela = criarTabela(["Matricula", "Nome do Aluno", "Sobrenome do Aluno"], turma[0])
    printarTabela(tabela)
    print(f"Avaliação selecionada: {avaliacao}")
    escolhas = ["Selecionar outra avaliação","Atribuir Nota Individual", "Atribuir Nota à Turma","Editar Nota", "Voltar"]
    selecao = input_select("O que deseja fazer:", escolhas)
    
    match selecao:
        case "Selecionar outra avaliação":
            selecionar_avaliacao(professor, turma[1])
        case "Atribuir Nota à Turma":
            atribuir_notas_turma(turma[1])
        case "Atribuir Nota Individual":
            pass

def selecionar_avaliacao(professor, turma): 
    acao = completer_aval(professor, turma, "Selecione:", "Pular").strip()
    avl_existe = False
    corte_indice = 2 if len(professor.avaliacoes) < 10 else 3 
    # Corte do índice é igual a 2 se a quantidade de avaliações é menor que dez, se não, é 3 
    
    for avl in professor.avaliacoes:
        if avl[1] == acao[corte_indice:]:
            avl_existe = True
            break
    
    if avl_existe or acao == "0-Pular":
        return acao    
    return "\033[31m[!] Não definida. Para prosseguir defina-a\033[0m"
    

# Seleciona uma turma. Retorna os registros dela se registros = True e apenas a selecao se False
def selecionar_turma(professor, registros=True): # Talvez mudar para se parecer com selecionar avaliação
    escolhas = []
    for turma_tupla in professor.getTurmas(False):
        escolhas.append(turma_tupla[1]) 
    escolhas.append("Voltar")

    selecao = input_select("Qual turma:", escolhas)
    if registros:
        return (Turma().buscar_turma(selecao, busca_matricula=False), selecao) # Retorna a turma e o nome
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
        disciplinas = staff.getDisciplinas()

        if len(disciplinas) == 2:
            print(f"Você leciona {disciplinas[0]} e {disciplinas[1]}.")
        elif len(disciplinas) > 2:
            disciplinas_out = f"{', '.join(disciplinas[:-1])} e {disciplinas[-1]}"
            print(disciplinas_out)
        else:
            print(f"Você leciona {', '.join(disciplinas)}")

def ver_perfil(instancia) -> None:
        nome_classe = instancia.__class__.__name__
        exibir_perfil_staff(instancia, nome_classe)
        printarLinha(40)
        acao = input_select("O que deseja fazer", ["Voltar"])