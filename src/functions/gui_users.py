# Modular classes mais tarde e importar elas por aqui, fica mais limpo
from sys import path
path.append("src"), path.append("src\\classes")
#from InquirerPy import inquirer

from classes.Aluno import Aluno 
from gui_funcs import *

# Faz o login e instancia o aluno
def login_aluno():
    while True: 
        credenciais = menu_login() 
        try: 
            aluno = Aluno().realizarLogin(credenciais['nome'], credenciais['senha'])
            break
        except IndexError:
            print("\033[91m[!]\033[0m Seu nome ou senha estão incorretos")

def menu_aluno():
    login_aluno()
    printarFiglet(f"{saudacoesTempo(getDataTempo())}, Estudante!")
    acao = inquirer.select(
        message="O que deseja fazer:",
        choices=["Ver Notas", "Listar Turmas", "Deslogar","Sair do Sistema",]
    ).execute()

    

        # Enquanto as credenciais não estiverem corretas nao deixar logar
        # O usuário terá a opção de tentar novamente e sair.
        # Permitir que os usuarios desloguem e saiam do sistema aqui e no menu incial.
        # Permitir que os usuarios voltem para o menu inicial? (precisaria transformar numa função para chama-la novamente)


def menu_professor():
    menu_login("Professor")

def menu_administrador():
    menu_login("Administrador")