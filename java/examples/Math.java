import java.util.Scanner;
import java.io.*;

public class Math {

    public static void main(String[] args) {
        Math MathClass = new Math();
        BufferedReader read = new BufferedReader(new In 

        Scanner kbdIn = new Scanner(System.in);
        System.out.print("Press 1 to add, 2 to multiply, 3 to subtract, or 4 to divide: ");
        int input = kbdIn.nextInt();

        if (input == 1) {
            MathClass.add();
        } else {
            System.out.println("NIH");
        }
    }

    public void add() {
        String numbers = System.in.readline("Enter the numbers to be added: ");

        System.out.println(numbers);
    }
}
