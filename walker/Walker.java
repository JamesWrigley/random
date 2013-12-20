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

            try {
                int choice = Integer.parseInt(read_keywords.readLine().trim());
                if (choice != 1 && choice != 2) {
                    continue;
                }
                System.out.print("Enter one or more keywords: ");
                String[] keywords = read_keywords.readLine().trim().split("\\s+");
                
                if (choice == 1) {
                    search(keywords);
                    break;
                } else if (choice ==2) {
                    delete(keywords);
                    break;
                } 
            } catch (NumberFormatException e) {
                System.out.println("Invalid option \"" + e + "\"");
                continue;
            }
         }
    }

    public static String[] getAllFilePathsInCWD() throws IOException {
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
            throw new IOException("File walk failed");
        }
        return file_list.toArray(new String[0]);
    }

    public static String[] getMatchingFilePaths(String[] pFilePaths, String[] pMatchList) {
        // ArrayList to store the matches
        ArrayList<String> matchingFilePaths = new ArrayList<String>();

        for (String filePath : pFilePaths) { // Match against all keywords
            boolean isMatch = true;
            String fileNameWithoutExtn = filePath.substring(filePath.lastIndexOf(File.separator) + 1);

            for (String stringToMatch : pMatchList) {
                if (!fileNameWithoutExtn.contains(stringToMatch)) {
                    isMatch = false;
                    break;
                }
            }
            if (isMatch) {
                matchingFilePaths.add(filePath);
            }
        }
        return matchingFilePaths.toArray(new String[0]);
    }

    public static void search(String[] pMatchList) throws IOException {
        String[] matches = getMatchingFilePaths(getAllFilePathsInCWD(), pMatchList);

        if (matches.length == 0) {
            System.out.println("No matches found");
            System.exit(0);
        }
        for (String i : matches) {
            System.out.println(i);
        }

        if (matches.length == 1) {
            System.out.println("Found 1 match");
        } else {
            System.out.println("Found " + matches.length + " matches");
        }
    }

    public static void delete(String[] pMatchList) throws IOException {
        BufferedReader read_choice = new BufferedReader(new InputStreamReader(System.in));
        String[] matchedFilePaths = getMatchingFilePaths(getAllFilePathsInCWD(), pMatchList);

        if (matchedFilePaths.length == 0) {
            System.out.println("No matches found");
            System.exit(0);
        }

        for (String i : matchedFilePaths) {
            System.out.println(i);
        }

        while (true) {
            if (matchedFilePaths.length == 1) {
                System.out.print("Are you sure you want to delete this file? [y/N]: ");
            } else {
                System.out.print("Are you sure you want to delete these " + matchedFilePaths.length + " files? [y/N]: ");
            }
            String choice = read_choice.readLine().trim();

            if ("yY".contains(choice)) {
                for (String filePath : matchedFilePaths) {
                    File file = new File(filePath);
                    file.delete();
                }
                System.out.println("Deleted " + matchedFilePaths.length + " files");
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
