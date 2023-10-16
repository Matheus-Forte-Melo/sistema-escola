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

def criarTabela(header: list, *colunas) -> AsciiTable:
    dados_tabela = []
    dados_tabela.append(header)
    for coluna in colunas:
        dados_tabela.append(coluna)
    
    return AsciiTable(dados_tabela)

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

