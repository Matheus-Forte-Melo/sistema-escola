from sys import path
path.append("src")
path.append("src\\functions") # Por enquanto vai funcionar, mas creio que isso não seja a melhor solução. Empacotarei as funcões depois

from functions import gui_users
from functions import gui_funcs

# Confirmação, talvez mude de lugar mais tarde e transforme numa função

confirmado = False
while not confirmado:
    usuario = gui_funcs.menuInicial()
    confirmado = gui_funcs.confirmar(usuario)

match usuario:
    case "Aluno":
        gui_users.menu_aluno()
    case "Professor":
        gui_users.menu_professor()
    case "Administrador":
        gui_users.menu_administrador()

