# Modular classes mais tarde e importar elas por aqui, fica mais limpo
from sys import path
path.append("src"), path.append("src\\classes")

from classes.Nota import Notas
from classes.Aluno import Aluno
from classes.Professor import Professor 
from classes.Administrador import Administrador
from classes.Turma import Turma
from classes.Avaliacao import Avalicao
from gui_funcs import *

# Tenta fazer login com o argumento classe recebido. Se sucedido, retorna uma instância dessa classe
def login(classe):
    print('\033[32m[!]\033[0m Caso queira cancelar e sair, digite APENAS "sair" no campo de senha.')
    while True: 
        credenciais = menu_login() 
        try:            
            instancia = classe.realizarLogin(credenciais['nome'], credenciais['senha'])
            break
        except IndexError:
            print("\033[91m[!]\033[0m Seu nome ou senha estão incorretos")
    return instancia


