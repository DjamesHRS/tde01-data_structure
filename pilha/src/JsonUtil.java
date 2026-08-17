
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class JsonUtil {

    public static void salvarPilha(PilhaAnilhas pilha, String caminho) {
        try {
            Files.createDirectories(Paths.get("data"));
            Anilha[] elementos = pilha.getElementos();

            StringBuilder sb = new StringBuilder();
            sb.append("{\n");
            sb.append("  \"pilha\": [\n");
            for (int i = 0; i < elementos.length; i++) {
                sb.append("    { \"peso\": ").append(elementos[i].getPeso()).append(" }");
                if (i < elementos.length - 1) sb.append(",");
                sb.append("\n");
            }
            sb.append("  ]\n");
            sb.append("}\n");

            Files.write(Paths.get(caminho), sb.toString().getBytes());
            System.out.println("Pilha salva em " + caminho);
        } catch (IOException e) {
            System.out.println("Erro ao salvar pilha: " + e.getMessage());
        }
    }

    public static PilhaAnilhas carregarPilha(String caminho, int capacidade) {
        PilhaAnilhas pilha = new PilhaAnilhas(capacidade);
        File arquivo = new File(caminho);
        if (!arquivo.exists()) {
            System.out.println("Nenhum arquivo salvo encontrado em " + caminho);
            return pilha;
        }
        try {
            String conteudo = new String(Files.readAllBytes(Paths.get(caminho)));
            List<Double> pesos = new ArrayList<>();

            int idx = 0;
            while ((idx = conteudo.indexOf("\"peso\":", idx)) != -1) {
                int inicio = idx + "\"peso\":".length();
                int fim = conteudo.indexOf("}", inicio);
                String numero = conteudo.substring(inicio, fim).trim();
                pesos.add(Double.parseDouble(numero));
                idx = fim;
            }

            for (double peso : pesos) {
                pilha.empilhar(new Anilha(peso));
            }
            System.out.println("Pilha carregada de " + caminho);
        } catch (IOException e) {
            System.out.println("Erro ao carregar pilha: " + e.getMessage());
        }
        return pilha;
    }
}
