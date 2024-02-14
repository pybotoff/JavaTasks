import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;
        do {
            System.out.println("Введите номер функции, которую вы хотите вызвать:");
            System.out.println("1. Вывести четные значения от 1 до 10");
            System.out.println("2. Провести операцию с двумя числами");
            System.out.println("3. Сравнить строки");
            System.out.println("4. Выход");
            choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    Numbers.goNumbers();
                    break;
                case 2:
                    Operations.performOperations(scanner);
                    break;
                case 3:
                    Strings.takeStrings(scanner);
                    break;
                case 4:
                    System.out.println("Выход из программы");
                    break;
                default:
                    System.out.println("Неверный выбор");
                    break;
            }
        } while (choice != 4);

        scanner.close();
    }
}
