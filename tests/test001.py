from sys import path
path.append("D:\\GitHub\\sistema-escola")
path.append("D:\\GitHub\\sistema-escola\\src\\classes")
path.append("D:\\GitHub\\sistema-escola\\src\\functions")

from src.classes.Administrador import Administrador
from src.classes.Turma import Turma
from src.functions import gui_adm
from src.functions.gui_users import input_text

adm = Administrador().realizarLogin(nome="Nivaldo Rosbevino", senha="lgbtq12345")
gui_adm.matricular_estudante(adm)

     



