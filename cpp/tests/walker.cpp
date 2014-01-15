// Yes... walker.py written in C++...

#include <iostream>
#include <boost/filesystem.hpp>
#include <boost/algorithm/string.hpp>

using namespace boost::filesystem;
using namespace std;


vector<path> get_all_files_under_path(path path_to_search, const vector<string>& keywords)
{
  /* This is the function that has the actual search functionality
     It first gets a list of all the files under the path_to_search (PWD by default)
     then matches them against all of the keywords passed to it.
     It then returns all the matches.
  */
  vector<path> files;
  for (recursive_directory_iterator end, dir(path_to_search); dir != end; ++dir)
    {
      if (is_regular_file(*dir))
        {
          files.push_back(*dir);
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

  if (1 == option)
    {
      vector<path> file_list = get_all_files_under_path(path_to_search, keywords_vect);
      for (unsigned int i = 0; i < file_list.size(); i++)
        {
          cout << file_list[i].string() << endl;
        }
    }
  else if (2 == option)
    {
      cout << "Delete" << endl;
    }
  else
    {
      cout << "Unrecognised option \"" << option << "\"" << endl;
    }
}
