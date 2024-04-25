package daily_tasks;

import java.util.Scanner;

public class First {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Wprowadź liczbę: ");
        if (scanner.hasNextInt()) {
            System.out.println("Wprowadzono liczbę całkowitą (int).");
        } else if (scanner.hasNextDouble()) {
            System.out.println("Wprowadzono liczbę rzeczywistą (double).");
        } else if (scanner.hasNextLong()) {
            System.out.println("Wprowadzono liczbę całkowitą (long).");
        } else if (scanner.hasNextFloat()) {
            System.out.println("Wprowadzono liczbę rzeczywistą (float).");
        } else {
            System.out.println("Wprowadzono coś innego.");
        }

        scanner.close();
    }
}
