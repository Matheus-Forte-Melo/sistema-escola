# Modular classes mais tarde e importar elas por aqui, fica mais limpo
from sys import path
path.append("src"), path.append("src\\classes")

from classes.Aluno import Aluno
from classes.Professor import Professor 
from classes.Administrador import Administrador
from classes.Turma import Turma
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

#================================================= GUIs PRINCIPAIS ==========================================================
#====================================================== Alunos ==============================================================
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
                ver_perfil(aluno)                
            case "Listar Turma":
                listar_turma_aluno(aluno)
            case "Sair do Sistema":
                break

def listar_turma_aluno(aluno):
    turma_atual = Turma().buscarTurma(aluno.getTurma(False)) # Não é uma instância, por enquanto?
    print(turma_atual)
    acao = inquirer.select(message="O que deseja fazer:",choices=["Voltar"]).execute()

def menu_professor():
    professor = login(classe=Professor())
    while True:
        printarFiglet(f"{saudacoesTempo(getDataTempo())}, Professor(a)!")
        print(f"Logado(a) como: {professor.getNome(completo=True)}")
        acao = inquirer.select(
        message="O que deseja fazer", choices=["Ver Perfil", "Listar Alunos", "Listar Turmas", "Gerenciar Notas", "Sair do Sistema"]).execute()

        match acao:
            case "Ver Perfil":
                ver_perfil(professor)                
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
                ver_perfil(adm)                
            case "Sair do Sistema":
                break

# ===================================================== GUI "VER PEFIL" ====================================================

def ver_perfil(instancia) -> None:
        nome_classe = instancia.__class__.__name__
        printarLinha(40)
        if nome_classe == "Aluno":
            exibir_perfil_aluno(instancia)
        elif nome_classe == "Professor" or nome_classe == "Administrador":
            exibir_perfil_staff(instancia, nome_classe)
        printarLinha(40)
        acao = inquirer.select(message="O que deseja fazer:",
                               choices=["Voltar"]).execute()
        
def exibir_perfil_aluno(aluno):
    print(f"Matricula: {aluno.getMatricula()}\n"
            f"Nome: {aluno.getNome(True)}\n"
            f"Nascimento: {aluno.getNascimento()}\n"
            f"Você estuda na turma: {aluno.getTurma()}\n"
            f"Responsáveis:\n", end="" 
            f"{aluno.getResponsaveis()[0]} e {aluno.getResponsaveis()[1]}\n")
    
def exibir_perfil_staff(staff, nome_classe):
    print(f"Id: {staff.getId()} \n", end=""
          f"Nome: {staff.getNome(True)}\n")
    if nome_classe == "Professor":
        print(f"Você leciona para {staff.getTurmas()} Turmas!")
        print(f"Você leciona {len(staff.getDisciplinas())} disciplinas: sendo elas {staff.getDisciplinas()}")
    
# ================================== Visualizar Tabelas ===========================================


