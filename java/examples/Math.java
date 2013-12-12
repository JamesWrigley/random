/* 
 * 
 * Issues: 
 * Your code looked fairly tidy. 
 * 
 * 1) You have to watch out with integers and math operations. For example 1 / 2 = 0 with integers. I've changed the code to a float but you need to also beaware that floats are not suitable for operations that require accuracy. 
 * 2) There is a lot of duplication of code. e.g. 4 * read integer code. You should put the duplicate / common code into a single method. 
 * 3) You had a line of unused code ... Math mathClass = new Math();x 
 * Here is a simplified version of the code 
 */

import java.io.*;
import java.util.Arrays;

public class Math {

    public static void main(String[] args) throws IOException {
        run();
    }
 
    public static void run() throws IOException {

        System.out.print("Press 1 to add, 2 to multiply, 3 to subtract, or 4 to divide: ");
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
                
        int input = Integer.parseInt(read.readLine()); //Ideally you should display an error rather than throw an exception

        if(input != 1 && input != 2 && input != 3 && input != 4) { //Validate input 
            System.out.println("Incorrect input"); 
            return;
        }

        System.out.print("Enter numbers: ");
        String[] values = read.readLine().trim().split("\\s+");

        float total = 0;

        for (int index = 0; index < values.length; index++) {

            float floatValue = Float.parseFloat(values[index]); 

            if(index == 0) { //Set value on first iteration 
                total = floatValue;
            }
            else if (input == 1) {
                total += floatValue;
            } else if (input == 2) {
                total *= floatValue;
            } else if (input == 3) {
                total -= floatValue;
            }
            else if (input == 4) {
                total /= floatValue;
            } else { //You should never hide a bug so throw exceptions for invalid states (Notice I throw an Error which doesn't have to be handled with a try catch statement)
                throw new Error("Unknown input type: " + input);
            }
        }
        System.out.println(total);
    }
}
