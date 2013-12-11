import java.io.*;
import java.util.Arrays;

public class Math {

    public static void main(String[] args)
        throws Exception
    {
        Math mathClass = new Math();

        System.out.print("Press 1 to add, 2 to multiply, 3 to subtract, or 4 to divide: ");

        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int input = Integer.parseInt(read.readLine());

        if (input == 1) {
            add();
        } else {
            System.out.println("NIH");
        }
    }


    public static void add() 
        throws Exception
    {
        System.out.print("Enter the numbers to be added: ");

        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        String[] values = read.readLine().split("\\s+");
        int[] int_values = new int[values.length];

        for (int i = 0; i < values.length; ++i) {
            int_values[i] = Integer.parseInt(values[i]);
        }

        int sum = 0;
        for (int i : int_values)
            sum += i;

        System.out.println(values);

    }
}
