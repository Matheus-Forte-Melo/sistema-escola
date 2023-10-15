# Modular classes mais tarde e importar elas por aqui, fica mais limpo
from sys import path
path.append("src"), path.append("src\\classes")
#from InquirerPy import inquirer

from classes.Aluno import Aluno
from classes.Professor import Professor 
from gui_funcs import *

# Tenta fazer login com o argumento classe recebido. Se sucedido, retorna uma instância dessa classe
def login(classe):
    while True: 
        credenciais = menu_login() 
        try: 
            instancia = classe.realizarLogin(credenciais['nome'], credenciais['senha'])
            break
        except IndexError:
            print("\033[91m[!]\033[0m Seu nome ou senha estão incorretos")
    return instancia

def menu_aluno():
    aluno = login(classe=Aluno())
    printarFiglet(f"{saudacoesTempo(getDataTempo())}, Estudante!")
    print(f"Logado como: {aluno.getNome(completo=True)}")
    acao = inquirer.select(
        message="O que deseja fazer:",
        choices=["Ver perfil", "Listar Notas", "Listar Turma", "Deslogar", "Sair do Sistema",]
    ).execute()
        # Enquanto as credenciais não estiverem corretas nao deixar logar
        # O usuário terá a opção de tentar novamente e sair.
        # Permitir que os usuarios desloguem e saiam do sistema aqui e no menu incial.
        # Permitir que os usuarios voltem para o menu inicial? (precisaria transformar numa função para chama-la novamente)


def menu_professor():
    professor = login(classe=Professor())
    printarFiglet(f"{saudacoesTempo(getDataTempo())}, Professor(a)!")
    print(f"Logado(a) como: {professor.getNome(completo=True)}")
    inquirer.select(
        message="O que deseja fazer",
        choices=["Ver Perfil", "Listar Alunos", "Listar Turmas", "Listar/Atribuir Notas", "Deslogar"]).execute()

def menu_administrador():
    menu_login("Administrador")

