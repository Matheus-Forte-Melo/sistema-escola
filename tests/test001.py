from sys import path
path.append('src')
import datetime
from functions.gui_funcs import criarTabela, printarTabela

dados = [('Matheus', 'Forte de Melo', datetime.date(2006, 2, 15)), ('Kauã', 'Nazário', datetime.date(2006, 7, 12))]
header = ["Primeiro Nome"," Sobrenome", "Nascimento"]


tabela = criarTabela(header, dados)
printarTabela(tabela)