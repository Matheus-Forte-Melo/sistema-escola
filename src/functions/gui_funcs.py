from InquirerPy import inquirer
import pyfiglet
from terminaltables import AsciiTable

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





