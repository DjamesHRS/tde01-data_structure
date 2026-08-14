import json
from exercicio import Exercicio
from fila import Fila

with open('fila.json', 'r') as fila:
    data = json.load(fila)

def carregar_fila():
    fila = Fila()
    for elemento in data:
        exercicio = Exercicio(elemento['id'], elemento['nome'], elemento['aluno'], elemento['aparelho'], elemento['tempo_execucao'], elemento['status'])
        fila.adicionar(exercicio)
    return fila

def salvar_fila(fila):
    data = []
    for elemento in fila.listar():
        data.append({
            'id': elemento.id,
            'nome': elemento.nome,
            'aluno': elemento.aluno,
            'aparelho': elemento.aparelho,
            'tempo_execucao': elemento.tempo_execucao,
            'status': elemento.status
        })
    with open('fila.json', 'w') as fila_file:
        json.dump(data, fila_file, indent=4)
    