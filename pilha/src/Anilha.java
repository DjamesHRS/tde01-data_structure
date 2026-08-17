
public class Anilha {
    private double peso;

    public Anilha(double peso) {
        this.peso = peso;
    }

    public double getPeso() {
        return peso;
    }

    @Override
    public String toString() {
        return peso + "kg";
    }
}
