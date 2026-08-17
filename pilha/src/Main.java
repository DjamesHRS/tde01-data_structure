import java.util.Scanner;

public class Main {
    static final String ARQUIVO = "data/pilha.json";
    static final int CAPACIDADE = 10;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        PilhaAnilhas pilha = JsonUtil.carregarPilha(ARQUIVO, CAPACIDADE);

        int opcao = -1;
        while (opcao != 0) {
            System.out.println("\n===== PILHA DE ANILHAS - MENU =====");
            System.out.println("1 - Colocar anilha na barra (empilhar)");
            System.out.println("2 - Retirar anilha da barra (desempilhar)");
            System.out.println("3 - Ver anilha do topo (sem remover)");
            System.out.println("4 - Buscar anilha por peso");
            System.out.println("5 - Mostrar status da pilha");
            System.out.println("6 - Salvar pilha em arquivo (JSON)");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");

            if (!scanner.hasNextInt()) {
                System.out.println("Opção inválida.");
                scanner.next();
                continue;
            }
            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    System.out.print("Peso da anilha (kg): ");
                    double peso = scanner.nextDouble();
                    pilha.empilhar(new Anilha(peso));
                    break;
                case 2:
                    pilha.desempilhar();
                    break;
                case 3:
                    Anilha t = pilha.topo();
                    if (t != null) System.out.println("Anilha no topo: " + t);
                    break;
                case 4:
                    System.out.print("Peso a buscar (kg): ");
                    double buscado = scanner.nextDouble();
                    boolean achou = pilha.contemAnilha(buscado);
                    System.out.println(achou
                            ? "Existe anilha de " + buscado + "kg na barra."
                            : "Não há anilha de " + buscado + "kg na barra.");
                    break;
                case 5:
                    pilha.mostrarStatus();
                    break;
                case 6:
                    JsonUtil.salvarPilha(pilha, ARQUIVO);
                    break;
                case 0:
                    JsonUtil.salvarPilha(pilha, ARQUIVO);
                    System.out.println("Saindo... pilha salva automaticamente.");
                    break;
                default:
                    System.out.println("Opção inválida.");
            }
        }
        scanner.close();
    }
}
