// Yes... walker.py written in C++...

#include <iostream>
#include <boost/filesystem.hpp>
#include <boost/algorithm/string.hpp>

using namespace boost::filesystem;
using namespace std;


vector<path> get_all_files_under_path(path path_to_search, const vector<string>& keywords)
{
  /* This is the function that has the actual search functionality
     It first gets a list of all the files under the path_to_search (PWD by default),
     then matches them against all of the keywords passed to it.
     It then returns all the matches.
  */
  vector<path> files;

  for (recursive_directory_iterator end, dir(path_to_search); dir != end; ++dir)
    {
      if (is_regular_file(*dir)) // So we don't print the folders
        {
          bool does_match = true;
          for (unsigned int i = 0; i < keywords.size(); i++)
            {
              const char *keywords_char = keywords[i].c_str();
              const char *dir_char = dir->path().c_str();
              if (!strcasestr(dir_char, keywords_char))
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
  return files;
}

int main(int argc, char *argv[])
{
  path path_to_search = current_path(); // Defaults to the PWD
  int option;
  string keywords_str;
  vector<string> keywords_vect;

  // Offer options to user and get keywords
  cout << "Enter 1 to search, 2 to search and delete: ";
  cin >> option;
  cin.ignore();
  cout << "Enter keywords: ";
  getline(cin, keywords_str);

  // Convert the keyword string to a string vector
  boost::split(keywords_vect, keywords_str, boost::is_any_of("\t "));

  vector<path> file_list = get_all_files_under_path(path_to_search, keywords_vect);
  for (unsigned int i = 0; i < file_list.size(); i++)
    {
      cout << file_list[i].string() << endl;
    }

  if (1 == option)
    {
      cout << "Found " << file_list.size() << " matches." << endl;
      return 0;
    }
  else if (2 == option)
    {
      string choice;
      cout << "Found " << file_list.size() << " matches." << endl;
      cout << "Are you sure you wish to delete these " << file_list.size() << " files? [Y/n]: ";
      cin >> choice;

      if (choice == "y" || "Y")
        {
          for (unsigned int i = 0; i < file_list.size(); i++)
            {
              //  remove(file_list[i]);
              cout << "Deleted" << endl;
            }
          cout << file_list.size() << " files deleted" << endl;
        }
      else
        {
          cout << "No files deleted" << endl;
        }

    }
  else
    {
      cout << "Unrecognised option \"" << option << "\"" << endl;
    }
}
