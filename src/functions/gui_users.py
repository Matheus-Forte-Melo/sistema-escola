#importar classes
from gui_funcs import *

def menu_aluno():
    # Se a seleção for confirmada ele abre o menu de login
    menu_login()
   
    # aluno = Aluno()
    # aluno.realizarLogin()
    # print(f"{saudacoesTempo} {aluno.getNome()}")
    

def menu_professor():
    menu_login("Professor")

def menu_administrador():
    menu_login("Administrador")