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
                    menu_gerenciar_avaliacoes_notas(professor, turma)           
            case "Sair do Sistema":
                break

def menu_gerenciar_avaliacoes_notas(professor, turma):
    acao = None
    avaliacao = "\033[31m[!] Não definida. Para prosseguir defina-a\033[0m"
    indefinir = False
    opcoes = ["Definir avaliação", Separator(), "Criar nova avaliação" , Separator(), "Sair"]
    
    while True:
        print("[!] Selecione uma turma para gerenciar suas notas e avaliações")
        print(f"\033[33m>>> Turma selecionada: {turma[1]}\033[0m")
        print("Para trocar de turma, saia deste menu e entre novamente!")
        sleep(0.50)
        if acao != "Voltar": print(f"\033[33m>>> Avaliação selecionada: {avaliacao}\033[0m")
        sleep(0.65)
        acao = input_select("O que deseja fazer:", opcoes)
        
        match acao:
            case "Criar nova avaliação":
                indefinir = criar_avaliacao(professor, turma[1])
            case "Definir avaliação":
                professor.buscar_avaliacoes(turma[1])
                avaliacao = selecionar_avaliacao(professor, turma[1])
                if avaliacao == "\033[31m[!] Não definida. Para prosseguir defina-a\033[0m":
                     indefinir = True
            case "Definir outra avaliação":
                professor.buscar_avaliacoes(turma[1])
                avaliacao = selecionar_avaliacao(professor, turma[1])
            case "Gerenciar avaliação":
                indefinir = menu_gerenciar_avaliacoes(professor, turma[1], avaliacao)
            case "Atribuir nota à avaliação":
                menu_atribuir_nota(professor, turma, avaliacao)
            case "Voltar":
                opcoes = ["Definir avaliação", Separator(), "Criar nova avaliação" ,
                           "Trocar turma", Separator(), "Sair"]
                continue
            case "Sair":
                break
        
        if avaliacao == "0-Pular" or indefinir:
            avaliacao = "\033[31m[!] Não definida. Para prosseguir defina-a\033[0m"
            opcoes = ["Definir avaliação", Separator(), "Criar nova avaliação", Separator(), "Sair"]
            indefinir = False
        else:
            opcoes = ["Definir outra avaliação", "Gerenciar avaliação", "Atribuir nota à avaliação",
                       Separator(), "Voltar"]

def prepara_lista_notas(professor, turma, avaliacao):
    professor.buscar_avaliacoes(turma[1])
    qnt_indices = define_corte_indice(avaliacao, comeco=0)       
    pos = int(avaliacao[:qnt_indices])
    avl = Avalicao(id=professor.avaliacoes[pos-1][0])
    notas = avl.buscar_notas()
    
    turma_dict = {aluno[0]: {'nome': aluno[1], 'sobrenome': aluno[2]} for aluno in turma[0]}

    for codigo, nota in notas:
        if codigo in turma_dict:
            turma_dict[codigo]['nota'] = nota

    return ([[codigo, info['nome'], info['sobrenome'], info.get('nota', 'Sem nota')] for codigo, info in turma_dict.items()], professor.avaliacoes[pos-1][0])

def menu_atribuir_nota(professor, turma, avaliacao):
    while True:
        turma_lista = prepara_lista_notas(professor, turma, avaliacao)
        tabela = criarTabela(["Matricula", "Nome do Aluno", "Sobrenome do Aluno"], turma_lista[0])
        printarTabela(tabela)
        id_avl = turma_lista[1] 
        
        # Printa todos os alunos da turma, seria interessante se ele mostrasse as notas dos alunos dessa avaliação aqui
        print(f"Avaliação selecionada: {avaliacao}")
        escolhas = ["Atribuir Nota (SELEÇÂO)", "Atribuir Nota (TODOS)", "Editar Notas", "Voltar"]
        selecao = input_select("O que deseja fazer:", escolhas)
        
        match selecao:
            case "Atribuir Nota (TODOS)":
                atribuir_notas_turma(turma_lista, id_avl)
            case "Atribuir Nota (SELEÇÂO)":
                atribuir_nota_aluno(turma_lista, id_avl)
            case "Editar Notas":
                editar_notas(turma_lista, id_avl)
            case "Voltar":  
                break

def editar_notas(turma, avaliacao):
    alunos_com_nota = []
    for aluno in turma[0]:
        nota = aluno[3]
        if not isinstance(nota, str): # Arrumar isso
            alunos_com_nota.append([aluno[0], aluno[1], aluno[2]]) 

    try:
        escolhas = input_checkbox("Selecione os alunos: ", alunos_com_nota)
        escolhas = list(escolhas)
        for aluno in escolhas:
            atribuir_nota(aluno, avaliacao, ["Editando nota de:", "Digite a nova nota:"], True)
    except InvalidArgument:
        print("[!] Nenhuma nota foi atribuida, logo, não existem notas para editar.")
        print("--> Voltando <--")
        sleep(1.5)

def atribuir_nota(aluno, avaliacao, mensagens, atualizar): # aluno?
    mensagem_pre_input = mensagens[0]
    mensagem_input = mensagens[1]
    while True:
        try:
            print(f"\033[32m[!]\033[0m {mensagem_pre_input} \033[32m{aluno[1]} {aluno[2]}.\033[0m")
            nota = float(input(f"{mensagem_input} "))
            assert 0 <= nota <= 10, "A nota deve estar no intervalo de 0 a 10."
            nova_nota = Notas(nota, avaliacao, aluno[0], datetime.now().strftime("%Y-%m-%d"))
            nova_nota.publicar(atualizar)
            break
        except ValueError:
            print("\033[31m[!] Erro ao inserir nota! Certifique-se de digitar um número.\033[0m")
            sleep(1)
        except AssertionError as e:
            print(f"\033[31m[!] Erro ao inserir nota! {e} Tente novamente.\033[0m")
            sleep(1)

def atribuir_notas_turma(turma, avaliacao):
    for aluno in turma[0]:
        nota = aluno[3]
        if isinstance(nota, str): # Arrumar isso
            atribuir_nota(aluno, avaliacao, ["Atribuindo nota a(à):", "Digite a nova:"], False)
        else:
            print(f"\033[31m[!]\033[0m {aluno[1]} {aluno[2]} já possui nota!")
            sleep(0.20)
        
def atribuir_nota_aluno(turma, avaliacao):
    alunos_sem_nota = [] # Apenas nome e matricula, usarei avaliação turma para resgatar o correspondente
    for aluno in turma[0]:
        nota = aluno[3]
        if isinstance(nota, str): # Arrumar isso
            alunos_sem_nota.append([aluno[0], aluno[1], aluno[2]]) # Se fica vazia da erro, consertar isso

    try:
        escolhas = input_checkbox("Selecione os alunos: ", alunos_sem_nota)
        escolhas = list(escolhas)
        for aluno in escolhas:
            atribuir_nota(aluno, avaliacao, ["Atribuindo nota a(à):", "Digite a nova:"], False)
    except InvalidArgument:
        print("[!] Não há alunos para atribuir nota.")
        print("--> Voltando <--")
        sleep(1)
        
def menu_gerenciar_avaliacoes(professor, turma, avaliacao): 
    confirmar = False
    avaliacao_editada = None
    while True:
        professor.buscar_avaliacoes(turma)
        if avaliacao_editada == None:
            print(f"\033[32mGerenciando avaliação {avaliacao}\033[0m") # da turma: {turma}!\033[0m")
        else:
            print(f"\033[32mGerenciando avaliação {avaliacao} | Nome editado: {avaliacao_editada}\033[0m")

        escolhas = ["Editar Avaliação", "Deletar Avaliação", "Voltar"]
        acao = input_select("O que deseja fazer", escolhas)

        if acao == "Editar Avaliação":
            confirmar = input_confirm(f"Quer mesmo {acao.lower()}?")
        
        if not confirmar and acao not in ("Voltar", "Deletar Avaliação"):
            continue
        
        match acao:
            case "Editar Avaliação":
                avaliacao_editada = editar_avaliacao(professor, turma, avaliacao)
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
    return avl_atualizada[1] # nome

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

def selecionar_avaliacao(professor, turma): 
    acao = completer_aval(professor, turma, "Selecione:", "Pular")
    avl_existe = False
    corte_indice = 1 # Já contando com o travessão

    corte_indice = define_corte_indice(acao)  
    
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

def menu_administrador():
    adm = login(classe=Administrador())
    escolhas = ["Ver Perfil", "Gerenciar Alunos", "Gerenciar Turmas", "Gerenciar Notas", "Sair do Sistema"] # N tava aq
    while True:
        printarFiglet(f"{saudacoesTempo(getDataTempo())}, Admin!")
        print(f"Logado(a) como: {adm.getNome(completo=True)}")
        acao = input_select("O que deseja fazer", escolhas)

        match acao:
            case "Ver Perfil":
                ver_perfil(adm)
            case "Gerenciar Alunos":
                menu_gerenciar_alunos(adm)                
            case "Sair do Sistema":
                break
    
def menu_gerenciar_alunos(adm):
    escolhas = ["Matricular Estudante", "Buscar/Editar Estudante", "Voltar"]
    while True:
        acao = input_select("O que deseja fazer: ", escolhas)

        match acao:
            case "Matricular Estudante":
                matricular_estudante(adm)
                pass     
            case "Buscar/Editar Estudante":
                #buscar_aluno
                pass
            case "Voltar":
                break

def matricular_estudante(adm):
    pass

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