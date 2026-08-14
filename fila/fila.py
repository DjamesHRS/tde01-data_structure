import exercicio

class Fila:
    def __init__(self):
        self.elementos = []
        
    def adicionar(self, elemento):
        self.elementos.append(elemento)
    
    def remover(self):
        if not self.elementos:
            raise Exception("A fila está vazia.")
        return self.elementos.pop(0)

    def proximo(self):
        if not self.elementos:
            raise Exception("A fila está vazia.")
        return self.elementos[0]
    
    def consultar(self, id):
        for elemento in self.elementos:
            if elemento.id == id:
                return elemento
        raise Exception(f"Elemento com ID {id} não encontrado na fila.")
    
    def atualizar(self, id, nome=None, aluno=None, aparelho=None, tempo_execucao=None):
        elemento = self.consultar(id)
        elemento.atualizar(nome, aluno, aparelho, tempo_execucao)
        
    def listar(self):
        return self.elementos
    
    def tamanho(self):
        return len(self.elementos)
    
    def status(self):
        status_list = []
        for elemento in self.elementos:
            status_list.append((elemento.id, elemento.status))
        return status_list
    
    