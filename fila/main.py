from .exercicio import Exercicio
from .persistencia import carregar_fila, salvar_fila

def mostrar_menu():
    print("")
    print("=== Menu da Fila ===")
    print("1. Adicionar exercício")
    print("2. Remover exercício")
    print("3. Consultar exercício por ID")
    print("4. Atualizar exercício por ID")
    print("5. Listar exercícios")
    print("6. Ver tamanho da fila")
    print("7. Ver status da fila")
    print("8. Iniciar próximo exercício")
    print("9. Concluir exercício em execução")
    print("0. Sair")
    print("")
    
def cadastrar_exercicio(fila):
    id = input("Digite o ID do exercício: ").strip()
    nome = input("Digite o nome do exercício: ")
    aluno = input("Digite o nome do aluno: ")
    aparelho = input("Digite o aparelho utilizado: ")
    tempo_execucao = input("Digite o tempo de execução (em minutos): ")
    status = "Pendente"
    
    exercicio = Exercicio(id, nome, aluno, aparelho, tempo_execucao, status)
    fila.adicionar(exercicio)
    print(f"Exercício {nome} adicionado à fila.")
    
def listar_fila(fila):
    elementos = fila.listar()
    if not elementos:
        print("A fila está vazia.")
    else:
        print("=== Exercícios na Fila ===")
        for elemento in elementos:
            print(
                f"ID: {elemento.id}, Nome: {elemento.nome}, "
                f"Aluno: {elemento.aluno}, Aparelho: {elemento.aparelho}, "
                f"Tempo de Execução: {elemento.tempo_execucao} minutos, "
                f"Status: {elemento.status}"
            )
            
def consultar_exercicio(fila):
    id = input("Digite o ID do exercício a ser consultado: ").strip()
    try:
        exercicio = fila.consultar(id)
        print(
            f"ID: {exercicio.id}, Nome: {exercicio.nome}, Aluno: {exercicio.aluno}, "
            f"Aparelho: {exercicio.aparelho}, Tempo de Execução: {exercicio.tempo_execucao} minutos, "
            f"Status: {exercicio.status}"
        )
    except Exception as e:
        print(e)
        
def atualizar_exercicio(fila):
    id = input("Digite o ID do exercício a ser atualizado: ").strip()
    nome = input("Digite o novo nome do exercício (ou pressione Enter para manter o atual): ")
    aluno = input("Digite o novo nome do aluno (ou pressione Enter para manter o atual): ")
    aparelho = input("Digite o novo aparelho utilizado (ou pressione Enter para manter o atual): ")
    tempo_execucao = input("Digite o novo tempo de execução (em minutos) (ou pressione Enter para manter o atual): ")
    
    try:
        fila.atualizar(
            id,
            nome if nome else None,
            aluno if aluno else None,
            aparelho if aparelho else None,
            tempo_execucao if tempo_execucao else None,
        )
        print(f"Exercício com ID {id} atualizado com sucesso.")
    except Exception as e:
        print(e)
               
def remover_exercicio(fila):
    try:
        exercicio = fila.remover()
        print(f"Exercício {exercicio.nome} removido da fila.")
    except Exception as e:
        print(e)

def iniciar_proximo(fila):
    try:
        exercicio = fila.iniciar()
        print(f"Exercício {exercicio.nome} iniciado (aluno: {exercicio.aluno}).")
    except Exception as e:
        print(e)

def concluir_atual(fila):
    try:
        exercicio = fila.concluir()
        print(f"Exercício {exercicio.nome} concluído e removido da fila.")
    except Exception as e:
        print(e)
        

def main():
    fila_exercicios = carregar_fila()
    
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        print("")
        
        if opcao == "1":
            cadastrar_exercicio(fila_exercicios)
            salvar_fila(fila_exercicios)
        elif opcao == "2":
            remover_exercicio(fila_exercicios)
            salvar_fila(fila_exercicios)
        elif opcao == "3":
            consultar_exercicio(fila_exercicios)
        elif opcao == "4":
            atualizar_exercicio(fila_exercicios)
            salvar_fila(fila_exercicios)
        elif opcao == "5":
            listar_fila(fila_exercicios)
        elif opcao == "6":
            print(f"Tamanho da fila: {fila_exercicios.tamanho()}")
        elif opcao == "7":
            status_list = fila_exercicios.status()
            if not status_list:
                print("A fila está vazia.")
            else:
                print("=== Status da Fila ===")
                for id, status in status_list:
                    print(f"ID: {id}, Status: {status}")
        elif opcao == "8":
            iniciar_proximo(fila_exercicios)
            salvar_fila(fila_exercicios)
        elif opcao == "9":
            concluir_atual(fila_exercicios)
            salvar_fila(fila_exercicios)
        elif opcao == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
                                    
if __name__ == "__main__":
    main()