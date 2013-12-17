// A clone of walker.py, but written in Java

import java.io.*;

public class Walker {
    public static void main(String[] args) throws IOException {
        System.out.print("Press 1 if you want to search, 2 if you want to search and delete: ");
        BufferedReader read_keywords = new BufferedReader(new InputStreamReader(System.in));
        int choice = Integer.parseInt(read_keywords.readLine().trim());

        if (choice != 1 && choice != 2) {
            throw new Error("Unrecognised option \"" + choice + "\"");
        } else {
            System.out.print("Enter 1 or more keywords: ");
            String[] keywords = read_keywords.readLine().trim().split("\\s+");

            if (choice == 1) {
                search(keywords);
            } else {
                delete(keywords);
            }
        }
    }

    public static String[] search_base(String[] args) {
        String[] matches = args;
        return matches;
    }

    public static void search(String[] args) {
        String[] matches = search_base(args);
        for (int i = 0; i < matches.length; i++) {
            System.out.println(matches[i]);
        }
        System.out.println("Found " + matches.length + " matches");
    }

    public static void delete(String[] args) throws IOException {
        BufferedReader read_choice = new BufferedReader(new InputStreamReader(System.in));
        String[] matches = search_base(args);

        for (int i = 0; i < matches.length; i++) {
            System.out.println(matches[i]);
        }

        while (true) {
            System.out.print("Are you sure you want to delete these " + matches.length + " files? [y/N]: ");
            String choice = read_choice.readLine().trim();

            if ("yY".contains(choice)) {
                System.out.println("Deleted " + matches.length + " files");
                break;
            } else if ("nN".contains(choice)) {
                System.out.println("No files deleted");
                break;
            } else {
                System.out.println("Invalid option");
            }
        }
    }
}
