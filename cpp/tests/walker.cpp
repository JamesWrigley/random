// Yes... walker.py written in C++...

#include <iostream>
#include <boost/filesystem.hpp>

using namespace boost::filesystem;
using namespace std;

vector<path> get_all_files_under_pwd(path path)
{
  vector<path> files;
  for (recursive_directory_iterator end, dir(path); dir != end; ++dir)
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
      cout << get_all_files_under_path(path_to_search) << endl;
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
