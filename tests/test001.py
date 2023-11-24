turma = [('20231015', 'Kauã', 'Nazário'), ('20231022000', 'Maria', 'Eduarda'), ('20231014', 'Matheus', 'Forte de Melo'), ('20231018', 'Thiago', 'Alessandro Batista')]
notas = [('20231015', '9.00'), ('20231014', '10.00')]

turma_dict = {}
turma_dict = {aluno[0]: {'nome': aluno[1], 'sobrenome': aluno[2]} for aluno in turma}

for codigo, nota in notas:
    if codigo in turma_dict:
        turma_dict[codigo]['nota'] = nota


turma_lista = [[codigo, info['nome'], info['sobrenome'], info.get('nota', 0.0)] for codigo, info in turma_dict.items()]
print(turma_lista)
