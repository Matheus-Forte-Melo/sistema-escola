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
        exit("Perai")

    nome = inquirer.text(message="Digite seu nome completo:").execute()
    senha = inquirer.secret(message="Digite sua senha:").execute()
        
        
    
    credenciais = {'nome': nome, 'senha': senha}
    return credenciais  

def valida_senha(senha):
    assert len(senha) > 8, "Senha muito curta"

    
    
    
    


