// A clone of walker.py, but written in Java

import java.io.*;
import java.util.*;
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;

public class Walker { // Prompts user to search or delete, gets keywords and passes them to the correct method
    public static void main(String[] args) throws IOException {
        while (true) {
            System.out.print("Press 1 if you want to search, 2 if you want to search and delete: ");
            BufferedReader read_keywords = new BufferedReader(new InputStreamReader(System.in));
            int choice;
            try {
                choice = Integer.parseInt(read_keywords.readLine().trim());
            } catch (NumberFormatException ex) {
                System.out.println("Invalid option");
                continue;
            }
 
            if (choice == 1 || choice == 2) {
                System.out.print("Enter one or more keywords: ");
                String[] keywords = read_keywords.readLine().trim().split("\\s+");
                
                if (choice == 1) {
                    search(keywords);
                    break;
                } else {
                    delete(keywords);
                    break;
                }
            } else {
                System.out.println("Invalid option \"" + choice + "\"");
                continue;
            }
        }
    }

    // The actual search functionality, search() and delete() call this method
    public static String[] search_base(String[] args) {
        final ArrayList<String> file_list = new ArrayList<String>();

        try { // Get all files in CWD and under and appends them to file_list
            Path startPath = Paths.get(System.getProperty("user.dir"));
            Files.walkFileTree(startPath, new SimpleFileVisitor<Path>() {
                    @Override
                        public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) {
                        file_list.add(file.toString());
                        return FileVisitResult.CONTINUE;
                    }
                    @Override
                        public FileVisitResult visitFileFailed(Path file, IOException e) {
                        return FileVisitResult.CONTINUE;
                    }
                });
        } catch (IOException e) {
            e.printStackTrace();
        }
        // ArrayList to store the matches
        ArrayList<String> matches_arrylst = new ArrayList<String>();
        boolean isMatch;

        for (String i : file_list) { // Match against all keywords
            isMatch = true;
            for (String e : args) {
                if (i.substring(i.lastIndexOf(File.separator) + 1).contains(e)) {
                    continue;
                } else {
                    isMatch = false;
                    break;
                }
            }
            if (isMatch) {
                matches_arrylst.add(i);
            }
        }

        // Convert to String[] to send back to the caller
        String[] matches = matches_arrylst.toArray(new String[0]);
        return matches;
    }

    public static void search(String[] args) {
        String[] matches = search_base(args);

        if (matches.length == 0) {
            System.out.println("No matches found");
            System.exit(0);
        }
        for (int i = 0; i < matches.length; i++) {
            System.out.println(matches[i]);
        }

        if (matches.length == 1) {
            System.out.println("Found 1 match");
        } else {
            System.out.println("Found " + matches.length + " matches");
        }
    }

    public static void delete(String[] args) throws IOException {
        BufferedReader read_choice = new BufferedReader(new InputStreamReader(System.in));
        String[] matches = search_base(args);

        if (matches.length == 0) {
            System.out.println("No matches found");
            System.exit(0);
        }

        for (int i = 0; i < matches.length; i++) {
            System.out.println(matches[i]);
        }

        while (true) {
            if (matches.length == 1) {
                System.out.print("Are you sure you want to delete this file? [y/N]: ");
            } else {
                System.out.print("Are you sure you want to delete these " + matches.length + " files? [y/N]: ");
            }
            String choice = read_choice.readLine().trim();

            if ("yY".contains(choice)) {
                for (String i : matches) {
                    File file = new File(i);
                    file.delete();
                }
                System.out.println("Deleted " + matches.length + " files");
                System.exit(0);
            } else if ("nN".contains(choice)) {
                System.out.println("No files deleted");
                System.exit(0);
            } else {
                System.out.println("Invalid option");
            }
        }
    }
}
