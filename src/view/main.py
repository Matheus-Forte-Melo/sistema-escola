from sys import path
path.append("src")
path.append("src\\functions") # Por enquanto vai funcionar, mas creio que isso não seja a melhor solução. Empacotarei as funcões depois

from functions import gui_adm
from functions import gui_aluno
from functions import gui_staff
from functions import gui_funcs

# Confirmação, talvez mude de lugar mais tarde e transforme numa função

confirmado = False
while not confirmado:
    usuario = gui_funcs.menuInicial()
    confirmado = gui_funcs.confirmar(usuario)

match usuario:
    case "Aluno":
        gui_aluno.menu_aluno()
    case "Professor":
        gui_staff.menu_professor()
    case "Administrador":
        gui_adm.menu_administrador()

