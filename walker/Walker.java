// A clone of walker.py, but written in Java

import java.io.*;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.FileSystems;
import java.nio.file.Path;

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
        File[] files = new File(System.getProperty("user.dir")).listFiles();
        Path cwd = FileSystems.getDefault().getPath(System.getProperty("user.dir"));
        DirectoryStream<Path> stream = Files.newDirectoryStream(cwd);
        
        for (Path path : stream) {
            System.out.println(path.getFileName());

        }
            return matches.toArray();
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
