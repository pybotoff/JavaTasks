import java.util.Scanner;

public class Strings {
    public static void takeStrings(Scanner scanner) {
        System.out.println("Первая строка:");
        String a = scanner.nextLine();
        System.out.println("Вторая строка:");
        String b = scanner.nextLine();

        if (a.equals(b)) {
            System.out.println("Строки идентичны");
        } else {
            System.out.println("Строки неидентичны");
        }
    }
}
