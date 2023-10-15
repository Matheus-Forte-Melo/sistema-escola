from InquirerPy import inquirer
from InquirerPy import validator
import pyfiglet
from terminaltables import AsciiTable
from datetime import date, datetime


def printarLinha(tamanho=20) -> str:
    print("="*tamanho)

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


def pegarDataTempo():
    data_tempo = (date.today(), datetime.today().time())
    return data_tempo

def saudacoesTempo():
    pass

# Confirma se o usuário realmente quer fazer login
def confirmar(usuario="Aluno") -> bool:
    confirmacao = inquirer.confirm(
        message=f"Deseja realizar login como: {usuario}",
        confirm_letter="s",
        reject_letter="n",
        transformer=lambda result: "Sim" if result else "Não").execute()
    return confirmacao

# Menu de login que retorna senha e usuário
def menu_login(usuario="Aluno") -> dict:
    if not confirmar(usuario):
        pass

    nome = inquirer.text(message="Qual o seu nome completo:").execute()
    while True:        
        senha = inquirer.secret(message="Qual a sua senha:").execute()
        if valida_senha(senha):
            break
            
    credenciais = {'nome': nome, 'senha': senha}
    return credenciais  

def valida_senha(senha):
    
    tamanho = len(senha)
    if tamanho < 8  or tamanho > 20:
        print("\033[91m[!]\033[0m O tamanho da senha deve ter entre 8 a 20 caracteres.")
        return False
    
    possui_char = any(char.isdigit() for char in senha)
    possui_num = any(char.isalpha() for char in senha)
    
    if possui_char is False or possui_num is False:
        print("\033[91m[!]\033[0m A senha deve possuir números e carácteres.")
        return False
    return True
        

    
    
    
    


