class Exercicio:
    def __init__(self, id, nome, aluno, aparelho, tempo_execucao, status):
        self.id = str(id)
        self.nome = nome
        self.aluno = aluno
        self.aparelho = aparelho
        self.tempo_execucao = tempo_execucao
        self.status = status
    
    def iniciar(self):
        self.status = "Em execução"
        
    def concluir(self):
        self.status = "Concluído"
        
    def atualizar(self, nome=None, aluno=None, aparelho=None, tempo_execucao=None):
        if nome:
            self.nome = nome
        if aluno:
            self.aluno = aluno
        if aparelho:
            self.aparelho = aparelho
        if tempo_execucao:
            self.tempo_execucao = tempo_execucao