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
            nome_aluno = input_text("Insira o nome completo", autocomplete=False)
            nome_aluno = separa_nome_sobrenome(nome_aluno)

            if nome_aluno[1].strip() == '':
                raise ValueError("[!] Certifique-se de inserir o nome completo")
            senha = input_text("Insira a senha inicial do estudante:")

            if nome_aluno == "" or len(senha) < 8 or len(senha) > 20:
                raise ValueError("[!] Certifique-se de inserir um nome válido e uma senha com tamanho entre 8 a 20.")
            break
        except ValueError as e:
            print(e)
        except IndexError as e:
            print("[!] Certifique-se de inserir o nome completo.")

    data_nascimento = input_data_nascimento()            
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    
    acao = input_select("Deseja: ", ["Atribuir à novos responsáveis", "Atribuir à responsáveis existentes"])
    match acao:
        case "Atribuir à novos responsáveis":
            responsaveis = input_responsáveis() # Precisa de validação também
        case "Atribuir à responsáveis existentes":
            responsaveis = atribui_resposáveis()

    turma = input_turma()
    novo_aluno = Aluno(nome_aluno[0], nome_aluno[1], data_nascimento, turma, responsaveis, senha)
    adm.matricular_estudante(novo_aluno)

def atribui_resposáveis():
    responsaveis_escolha = {}
    responsaveis = Responsaveis().buscar_todos()
    
    for responsavel in responsaveis:
            responsaveis_escolha[f"{responsavel[0]} - {responsavel[1]}"] = None

    while True:
        responsaveis_selecionados = input_text("Digite o nome do responsável principal: ", autocomplete=responsaveis_escolha)

        for responsavel in responsaveis:
            if f"{responsavel[0]} - {responsavel[1]}" == responsaveis_selecionados:
                return f"{responsavel[0]} - {responsavel[1]}"   
            else: 
                print("[!] Responsáveis não encontrados, certifique-se de usar o AUTOCOMPLETE.")

print(atribui_resposáveis())

def input_responsáveis(): # Retorna o ID do responsável criado
    while True:
        nomes_responsáveis = []
        try:
            nomes_responsáveis.append(input_text(f"Insira o nome do 1° responsável [OBRIGATÓRIO]"))
            nomes_responsáveis.append(input_text(f"Insira o nome do 2° responsável [FACULTATIVO]"))
            responsavel_1 = separa_nome_sobrenome(nomes_responsáveis[0])
            responsavel_2 = separa_nome_sobrenome(nomes_responsáveis[1])
            
            if responsavel_1[1].strip() == '':
                raise ValueError("[!] Certifique-se de inserir o nome completo")
            if nomes_responsáveis[0] == "": 
                raise ValueError("[!] O primeiro responsável precisa ser válido.")
            break
        except ValueError as e:
            print(e)
        except IndexError as e:
            print("[!] Certifique-se de inserir o nome completo.")
    
    novos_responsaveis = Responsaveis(responsavel_1[0], responsavel_1[1], responsavel_2[0], responsavel_2[1])
    return novos_responsaveis.cadastrar() # Isso aqui retorna o ID do responsável que fora cadastrado

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

    while True: # Isso aqui pode ser otimizado, vou deixar assim por enquanto, lá em cima tem outra parada q usa uma função igual (input_responsavel, o primeiro)
        turma_selecionada = input_text("Escolha a turma", autocomplete=turmas_escolha)

        for turma in turmas:
            if turma[1] == turma_selecionada:
                return turma[0]   
            else: 
                print("[!] Turma não encontrada, certifique-se de usar o AUTOCOMPLETE.")
            