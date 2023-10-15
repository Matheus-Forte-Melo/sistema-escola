# Modular classes mais tarde e importar elas por aqui, fica mais limpo
from sys import path
path.append("src"), path.append("src\\classes")

from classes import Aluno
from gui_funcs import *

def menu_aluno():
    while True: # Isso é um loop
        credenciais = menu_login("Aluno") 


def menu_professor():
    menu_login("Professor")

def menu_administrador():
    menu_login("Administrador")