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
from time import sleep
from InquirerPy.separator import Separator

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

def input_select(mensagem:str, escolhas):
    return inquirer.select(message=mensagem, choices=escolhas).execute()

def input_text(mensagem:str, autocomplete=None, simbolo="?"):
    if autocomplete != None:
        return inquirer.text(message=mensagem, completer=autocomplete, amark=simbolo).execute()
    return inquirer.text(message=mensagem, amark=simbolo).execute()

def input_confirm(mensagem:str):
    return inquirer.confirm(message=mensagem, default=True, confirm_letter="s", reject_letter="n",
                               transformer=lambda result: "SIm" if result else "Não",).execute()

def input_checkbox(mensagem:str, escolhas):
    return inquirer.checkbox(message=mensagem, choices=escolhas, 
                             validate=lambda result: len(result) >= 1,
                             invalid_message="Deve ter selecionado pelo menos 1",
                             instruction="[BARRA DE ESPAÇO] para selecionar e [ENTER] para confirmar ").execute()

            

