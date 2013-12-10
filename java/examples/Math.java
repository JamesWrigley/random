import java.util.Scanner;

public class Math {

    public static void main(String[] args) {
	Math MathClass = new Math();

	Scanner kbdIn = new Scanner(System.in);
	System.out.print("Press 1 to add, 2 to multiply, 3 to subtract, or 4 to divide: ");

    if (kbdIn.nextLine() == "1") {
	MathClass.add(args);
	    } else {
	System.out.println(kbdIn.nextLine());
    }
    }

    public void add(String[] args) {
	System.out.println("Foo bar");
    }
}
