from InquirerPy import inquirer
import pyfiglet
from terminaltables import AsciiTable
from datetime import date, datetime


def printarLinha(tamanho=20) -> str:
    print("="*tamanho)

def printarFiglet(titulo) -> str:
    ascii_art = pyfiglet.figlet_format(titulo, font="slant")
    printarLinha(60)
    print(ascii_art)
    printarLinha(60)

def menuInicial() -> str:
    ascii_art = pyfiglet.figlet_format("Sistema Escolar", font="slant")
    
    print(ascii_art)
    printarLinha(79)

    usuario = inquirer.select(
        message="Qual tipo de usuário você é: ",
        choices=["Aluno", "Professor", "Administrador"]).execute()

    return usuario 

def criarTabela(header: list, colunas) -> AsciiTable:
    dados_tabela = []
    dados_tabela.append(header)

    for coluna in colunas:
        dados_tabela.append(coluna)
    
    return AsciiTable(dados_tabela)

def define_corte_indice(string, comeco = 1):
    corte_indice = comeco  
    for i in string:
            if i.isnumeric():
                corte_indice += 1
            else:
                break
    return corte_indice

def separa_nome_sobrenome(string):
    nome_separado = string.split()
    primeiro_nome = nome_separado[0]
    sobrenome = " ".join(nome_separado[1:])
    return (primeiro_nome, sobrenome)

def printarTabela(tabela:AsciiTable) -> None:
    print(tabela.table)

# Pega data e hora e bota num dicionario
def getDataTempo():
    data_tempo = {'dia':date.today(),'horario':datetime.today().time().hour}
    return data_tempo

# Retorna uma saudação baseada no horário
def saudacoesTempo(data_tempo:dict) -> str:
    horario = data_tempo['horario']
    if horario > 4 and horario < 12:
        return "Bom dia"
    elif horario > 12 and horario < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

# Confirma se o usuário realmente quer fazer login
def confirmar(usuario="Aluno") -> bool:
    confirmacao = inquirer.confirm(
        message=f"Deseja realizar login como: {usuario}",
        confirm_letter="s",
        reject_letter="n",
        transformer=lambda result: "Sim" if result else "Não").execute()
    return confirmacao

# Menu de login que retorna senha e usuário
def menu_login() -> dict:
    nome = inquirer.text(
        message="Qual o seu nome completo:").execute()
    
    while True:        
        senha = inquirer.secret(message="Qual a sua senha:").execute()
        if valida_senha(senha): 
            break
            
    credenciais = {'nome': nome, 'senha': senha}
    return credenciais  

# Retorna True se a senha possuir entre 8 a 20 caracteres e se possuir carácteres e núemeros.
# Se a senha for "sair", todas as duas regras citadas acima são ignoradas.
def valida_senha(senha):
    tamanho = len(senha)
    if senha.lower() == 'sair':
        exit("Programa encerrado.")
    
    if (tamanho < 8  or tamanho > 20):
        print("\033[91m[!]\033[0m O tamanho da senha deve ter entre 8 a 20 caracteres.")
        return False
    
    possui_char = any(char.isdigit() for char in senha)
    possui_num = any(char.isalpha() for char in senha)
    
    if (possui_char is False or possui_num is False):
        print("\033[91m[!]\033[0m A senha deve possuir números e carácteres.")
        return False
    return True

def valida_data(data:str) -> bool:
    meses_dias = {"01": 31, "02": 28, "03": 31, "04": 30, "05": 31, "06": 30,
                  "07": 31, "08": 31, "09": 30, "10": 31, "11": 30, "12": 31}
    try:
        dia = data[0] + data[1]
        mes = data[3] + data[4]
        ano = data[6] + data[7] + data[8] + data[9]
        if not dia.isnumeric() or not mes.isnumeric() or not ano.isnumeric():
            raise ValueError
    except Exception:
        return False
    
    if int(ano) > date.today().year:
        return False

    if mes in meses_dias:
        if int(dia) <= meses_dias[mes]:
            pass
        else:
            return False

    if data[2] != "/" or data[5] != "/":
        return False
    
    return True

