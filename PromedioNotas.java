import java.util.Scanner;

public class PromedioNotas {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Ingrese la cantidad de notas que va a registrar: ");
        int n = teclado.nextInt();

        double[] notas = new double[n];
        double suma = 0;

        for (int i = 0; i < n; i++) {
            System.out.print("Ingrese la nota " + (i + 1) + ": ");
            notas[i] = teclado.nextDouble();
            suma += notas[i];
        }


        double notaMasAlta = notas[0];
        for (int i = 1; i < n; i++) {
            if (notas[i] > notaMasAlta) {
                notaMasAlta = notas[i];
            }
        }

        double promedio = suma / n;


        System.out.println("\n--- Resultados ---");
        System.out.println("La nota más alta es: " + notaMasAlta);
        System.out.println("El promedio de las notas es: " + promedio);

        teclado.close();
    }
}
