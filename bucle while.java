import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        int precio = 1;
        int totalsuma = 0;

        while (precio != 0) {
            System.out.print("Ingrese el precio del producto: ");
            precio = scanner.nextInt();
            totalsuma = totalsuma + precio;
        }
        System.out.println("El total es: $" + totalsuma);
    }
}