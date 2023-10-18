# Modular classes mais tarde e importar elas por aqui, fica mais limpo
from sys import path
path.append("src"), path.append("src\\classes")

from classes.Aluno import Aluno
from classes.Professor import Professor 
from classes.Administrador import Administrador
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

#================================================= GUI DOS ALUNOS ==========================================================
def menu_aluno():
    aluno = login(classe=Aluno())
    while True:
        printarFiglet(f"{saudacoesTempo(getDataTempo())}, Estudante!")
        print(f"Logado como: {aluno.getNome(completo=True)}")
        acao = inquirer.select(
            message="O que deseja fazer:",
            choices=["Ver Perfil", "Listar Notas", "Listar Turma", "Sair do Sistema",]
        ).execute()
        match acao:
            case "Ver Perfil":
                ver_perfil_aluno(aluno)                
            case "Sair do Sistema":
                break

#========================================================================================

def ver_perfil_aluno(aluno):
        printarLinha(40)
        print(f"Matricula: {aluno.getMatricula()}\n"
            f"Nome: {aluno.getNome(True)}\n"
            f"Nascimento: {aluno.getNascimento()}\n"
            f"Você estuda na turma: {aluno.getTurma()}\n"
            f"Responsáveis:\n", end="" 
            f"{aluno.getResponsaveis()[0]} e {aluno.getResponsaveis()[1]}\n")
        printarLinha(40)
        acao = inquirer.select(message="O que deseja fazer?", choices=["Voltar"]).execute()

#=========================== MENU DA EQUIPE DA ESCOLA ======================================================
def menu_professor():
    professor = login(classe=Professor())
    while True:
        printarFiglet(f"{saudacoesTempo(getDataTempo())}, Professor(a)!")
        print(f"Logado(a) como: {professor.getNome(completo=True)}")
        acao = inquirer.select(
        message="O que deseja fazer",
        choices=["Ver Perfil", "Listar Alunos", "Listar Turmas", "Gerenciar Notas", "Sair do Sistema"]).execute()

        match acao:
            case "Ver Perfil":
                ver_perfil_staff(professor)                
            case "Sair do Sistema":
                break

def menu_administrador():
    adm = login(classe=Administrador())
    while True:
        printarFiglet(f"{saudacoesTempo(getDataTempo())}, Admin!")
        print(f"Logado(a) como: {adm.getNome(completo=True)}")
        acao = inquirer.select(
            message="O que deseja fazer",
            choices=["Ver Perfil", "Gerenciar Alunos", "Gerenciar Turmas", "Gerenciar Notas", "Sair do Sistema"]).execute()

        match acao:
            case "Ver Perfil":
                ver_perfil_staff(adm)                
            case "Sair do Sistema":
                break

def ver_perfil_staff(instancia):
    printarLinha(40)
    print(f"Id: {instancia.getId()}\n"
        f"Nome: {instancia.getNome(True)}\n")
    if instancia.__class.__name == "Professor":
        choices = ["Voltar", "Ver Turmas que Leciniona", "iVer Disciplinas que Lescona"]
    acao = inquirer.select(message="O que deseja fazer?", choices=["Voltar"]).execute()