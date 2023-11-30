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
    while True:
        try:
            nome_completo_aluno = input_text("Insira o nome completo", autocomplete=False) # Falta a validação se tem sobrenome ou não, nos responsáveis também
            senha = input_text("Insira a senha inicial do estudante:")

            if nome_completo_aluno == "" or len(senha) < 8 or len(senha) > 20:
                raise ValueError("[!] Certifique-se de inserir um nome válido e uma senha com tamanho entre 8 a 20.")
            break
        except ValueError as e:
            print(e)

    data_nascimento = input_data_nascimento()            
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    nome_aluno = separa_nome_sobrenome(nome_completo_aluno) # Precisa de validação ainda
    
    acao = input_select("Deseja: ", ["Atribuir à novos responsáveis", "Atribuir à responsáveis existentes"])
    match acao:
        case "Atribuir à novos responsáveis":
            responsaveis = input_responsáveis() # Precisa de validação também
        case "Atribuir à responsáveis existentes":
            pass

    turma = input_turma()
    novo_aluno = Aluno(nome_aluno[0], nome_aluno[1], data_nascimento, turma)

def input_responsáveis():
    while True:
        nomes_responsáveis = []
        try:
            nomes_responsáveis.append(input_text(f"Insira o nome do 1° responsável [OBRIGATÓRIO]"))
            nomes_responsáveis.append(input_text(f"Insira o nome do 2° responsável [FACULTATIVO]"))
            
            if nomes_responsáveis[0] == "": # Tem que garantir que tem um sobrenome também
                raise ValueError("[!] O primeiro responsável precisa ser válido.")
            break
        except ValueError as e:
            print(e)
    
    return nomes_responsáveis

def input_data_nascimento():
        while True:
            try:
                data_nascimento = input_text("Insira a data de nascimento [DIA/MES/ANO]: ")
                if not valida_data(data_nascimento):
                    raise ValueError
                break
            except ValueError:
                print("[!] Insira uma data válida!")
        
        return data_nascimento

def input_turma():
    turmas = Turma().buscar_todas_turmas() 
    turmas_escolha = {}

    for turma in turmas:
        turmas_escolha[turma[1]] = None
    turma_selecionada = input_text("Escolha a turma", autocomplete=turmas_escolha)

    for turma in turmas:
        if turma[1] == turma_selecionada:
            return turma[0]   