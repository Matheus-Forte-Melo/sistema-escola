from gui_users import * 

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
    # Validar esses dados, de forma mais organizada, em pequenos blocos de codigo para ficar mais legível
    nomes_responsáveis = []
    for i in range(2):
        nomes_responsáveis.append(input_text(f"Insira o nome do {i+1}° responsável"))
    nome_completo = input_text("Insira o nome completo", autocomplete=False)
    senha = input_text("Insira a senha inicial do estudante:")
    assert len(nome_completo) > 0, "Não deixe o nome nulo!"
    data_nascimento = input_text("Insira a data de nascimento: ") 
    data_atual = getDataTempo()
    data_atual = data_atual['dia']

    
    nome_aluno = separa_nome_sobrenome(nome_completo)
    # Pensando em separar métodos dos professores dos admiistradores em gui_adm e gui_prof, vejo isso dps
    acao = input_select("Deseja: ", ["Atribuir à novos responsáveis", "Atribuir à responsáveis existentes"])
    novo_aluno = Aluno(nome_aluno[0], nome_aluno[1], data_nascimento)