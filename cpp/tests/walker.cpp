// Yes... walker.py written in C++...

#include <iostream>
#include <boost/filesystem.hpp>

using namespace boost::filesystem;
using namespace std;

vector<path> get_all_files_under_path(path path_to_search)
{
  vector<path> files;
  for (recursive_directory_iterator end, dir(path_to_search); dir != end; ++dir)
    {
      files.push_back(*dir);
    }
  return files;
}


int main(int argc, char *argv[])
{
  path path_to_search = current_path();
  int option;

  cout << "Enter 1 to search, 2 to search and delete: ";
  cin >> option;

  if (1 == option)
    {
      cout << "Search" << endl;
      vector<path> file_list = get_all_files_under_path(path_to_search);
      for (unsigned int i = 0; i < file_list.size(); i++)
        {
          cout << file_list[i] << endl;
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
