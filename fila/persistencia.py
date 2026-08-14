import json
from pathlib import Path
from .exercicio import Exercicio
from .fila import Fila

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "fila.json"


def carregar_fila():
    fila = Fila()
    if not DATA_FILE.exists():
        return fila

    with open(DATA_FILE, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read().strip()

    if not conteudo:
        return fila

    data = json.loads(conteudo)

    for elemento in data:
        exercicio = Exercicio(
            elemento['id'],
            elemento['nome'],
            elemento['aluno'],
            elemento['aparelho'],
            elemento['tempo_execucao'],
            elemento['status'],
        )
        fila.adicionar(exercicio)
    return fila

def salvar_fila(fila):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    data = []
    for elemento in fila.listar():
        data.append({
            'id': elemento.id,
            'nome': elemento.nome,
            'aluno': elemento.aluno,
            'aparelho': elemento.aparelho,
            'tempo_execucao': elemento.tempo_execucao,
            'status': elemento.status,
        })
        
    with open(DATA_FILE, 'w', encoding='utf-8') as fila_file:
        json.dump(data, fila_file, indent=4)
    