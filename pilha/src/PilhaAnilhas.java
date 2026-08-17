public class PilhaAnilhas {
    private Anilha[] pilha;
    private int topo;
    private int capacidade;

    public PilhaAnilhas(int capacidade) {
        this.capacidade = capacidade;
        this.pilha = new Anilha[capacidade];
        this.topo = -1;
    }


    public boolean empilhar(Anilha anilha) {
        if (estaCheia()) {
            System.out.println("A barra está cheia! Não é possível colocar mais anilhas.");
            return false;
        }
        topo++;
        pilha[topo] = anilha;
        System.out.println("Anilha " + anilha + " colocada na barra.");
        return true;
    }


    public Anilha desempilhar() {
        if (estaVazia()) {
            System.out.println("A barra está vazia! Nenhuma anilha para retirar.");
            return null;
        }
        Anilha removida = pilha[topo];
        pilha[topo] = null;
        topo--;
        System.out.println("Anilha " + removida + " retirada da barra.");
        return removida;
    }

    public Anilha topo() {
        if (estaVazia()) {
            System.out.println("A barra está vazia!");
            return null;
        }
        return pilha[topo];
    }

    public boolean contemAnilha(double peso) {
        for (int i = 0; i <= topo; i++) {
            if (pilha[i].getPeso() == peso) {
                return true;
            }
        }
        return false;
    }

    public boolean estaVazia() {
        return topo == -1;
    }

    public boolean estaCheia() {
        return topo == capacidade - 1;
    }

    public int quantidade() {
        return topo + 1;
    }

    public void mostrarStatus() {
        System.out.println("----- STATUS DA BARRA (topo -> fundo) -----");
        if (estaVazia()) {
            System.out.println("Barra vazia.");
        } else {
            double pesoTotal = 0;
            for (int i = topo; i >= 0; i--) {
                System.out.println((i == topo ? "[TOPO] " : "       ") + pilha[i]);
                pesoTotal += pilha[i].getPeso();
            }
            System.out.println("Total de anilhas: " + quantidade());
            System.out.println("Peso total na barra: " + pesoTotal + "kg");
        }
        System.out.println("--------------------------------------------");
    }

    public Anilha[] getElementos() {
        Anilha[] copia = new Anilha[quantidade()];
        for (int i = 0; i <= topo; i++) {
            copia[i] = pilha[i];
        }
        return copia;
    }
}
