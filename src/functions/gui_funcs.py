from InquirerPy import inquirer
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

def confirmar(usuario="aluno") -> bool:
    confirmacao = inquirer.confirm(
        message=f"Deseja realizar login como: {usuario}",
        confirm_letter="s",
        reject_letter="n",
        transformer=lambda result: "Sim" if result else "Não").execute()
    return confirmacao
    
def menu_login(usuario="Aluno"):
    if confirmar(usuario):
        print("MENU DE LOGIN")
    else:
        print("RETORNANDO")

