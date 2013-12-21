import java.io.*;

public class Backwards {
    public static void main(String[] args) throws IOException {
        System.out.print("Enter string: ");
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(new StringBuilder(read.readLine()).reverse().toString());
    }
}
