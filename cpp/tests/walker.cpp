// Yes... walker.py written in C++....

#include <iostream>
#include <boost/filesystem.hpp>
#include <boost/algorithm/string.hpp>

using namespace boost::filesystem;
using namespace std;

vector<path> get_all_files_under_path(path path_to_search, const vector<string>& keywords)
{
  /* This is the function that has the actual search functionality
     It gets a list of all the files under the path_to_search (PWD by default),
     and matches them against all of the keywords passed to it.
     It then returns all the matches.
  */
  vector<path> files;
  recursive_directory_iterator dir(path_to_search);

 try_block:
  try
    {
      for (recursive_directory_iterator end; dir != end; dir++)
        {
          if (is_regular_file(*dir)) // So we don't check the folders
            {
              bool does_match = true;
              for (unsigned int i = 0; i < keywords.size(); i++)
                {
                  const char *keyword_char = keywords[i].c_str();
                  const char *filename_char = dir->path().filename().c_str();
                  if (!strcasestr(filename_char, keyword_char))
                    {
                      does_match = false;
                    }
                }
              if (does_match)
                {
                  files.push_back(*dir);
                }
            }
        }
    }
  catch (const filesystem_error& error)
    {
      cout << "skipped before " << dir->path() << endl;
      dir++;
      goto try_block;
    }
  return files;
}


int main(int argc, char *argv[])
{
  path path_to_search = current_path(); // Defaults to the PWD
  string option;
  string keywords_str;
  vector<string> keywords_vect;

  // Offer options to user and get keywords
  while (true)
    {
      cout << "Enter 1 to search, 2 to search and delete: ";
      cin >> option;
      cin.ignore();

      if (option == "1" || option == "2")
        {
          break;
        }
      else
        {
          cout << "Invalid option" << endl;
          continue;
        }
    }

  cout << "Enter keywords: ";
  getline(cin, keywords_str);

  // Convert the keyword string to a string vector
  boost::split(keywords_vect, keywords_str, boost::is_any_of("\t "));

  vector<path> file_list = get_all_files_under_path(path_to_search, keywords_vect);
  for (unsigned int i = 0; i < file_list.size(); i++)
    {
      cout << file_list[i].string() << endl;
    }

  if ("1" == option)
    {
      if (0 == file_list.size())
        {
          cout << "No matches found" << endl;
          return 0;
        }
      else
        {
          cout << "Found " << file_list.size() << " matches." << endl;
          return 0;
        }
    }
  else if ("2" == option)
    {
      string choice;

      if (file_list.size() > 0)
        {
          cout << "Found " << file_list.size() << " matches." << endl;
          cout << "Are you sure you wish to delete these " << file_list.size() << " files? [Y/n]: ";
          cin >> choice;

          if (choice == "y" || choice == "Y")
            {
              for (unsigned int i = 0; i < file_list.size(); i++)
                {
                  //remove(file_list[i]);
                  cout << "Deleted" << endl;
                }
              cout << file_list.size() << " files deleted" << endl;
              return 0;
            }
          else
            {
              cout << "No files deleted" << endl;
              return 0;
            }
        }
      else
        {
          cout << "No matches found" << endl;
          return 0;
        }
    }
}
