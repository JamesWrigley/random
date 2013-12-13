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

// Import neccessary libraries
import java.io.*;
import java.util.Arrays;

public class Math {

    // Every Java program must have a main method that takes in a string array and has the 'public static void' type
    // Note that it declares the same execptions thrown by other functions called in the body
    public static void main(String[] args) throws IOException {
        run();
    }
 
    public static void run() throws IOException {

        System.out.print("Press 1 to add, 2 to multiply, 3 to subtract, or 4 to divide: ");
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));  // Sets up console input
                
        int input = Integer.parseInt(read.readLine()); // Converts the string input from read to an integer

        if(input != 1 && input != 2 && input != 3 && input != 4) { //Validate input 
            System.out.println("Incorrect input"); 
            return;
        }

        // Gets the input, removes any whitespace, and puts all arguments into an array
        System.out.print("Enter numbers: ");
        String[] values = read.readLine().trim().split("\\s+");

        float total = 0;

        // Bulk of the work goes here
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
