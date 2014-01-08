// A little calculator test

#include <boost/algorithm/string.hpp>

using std::cout;
using std::cin;

int main()
{
  while (true)
    {
      cout << "Press 1 to add, 2 to multiply, 3 to subtract, 4 to divide, or 5 to exit: ";

      int input;
      cin >> input;
      std::cin.ignore();

      if (input < 5)
        {
          // Some variable declarations
          std::string numbers_str;
          std::vector<float> numbers_float;
          std::vector<std::string> numbers_vect;
          std::string op_names[] = {"added", "multiplied", "subtracted", "divided"};

          cout << "Enter 2 or more numbers to be " << op_names[input - 1] << ": ";
          std::getline(cin, numbers_str);

          // Split numbers_str by whitespace, then converts the string vector into an int vector
          boost::split(numbers_vect, numbers_str, boost::is_any_of("\t "));
          std::transform(begin(numbers_vect), end(numbers_vect), std::back_inserter(numbers_float), [](const std::string& val) { return std::stof(val); });

          // The math part
          if (1 == input)
            {
              float sum = std::accumulate(numbers_float.begin(), numbers_float.end(), 0.0);
              cout << sum << std::endl;
              continue;
            }
          else if (2 == input)
            {
              float multiply_ans = std::accumulate(numbers_float.begin(), numbers_float.end(), 1.0, std::multiplies<float>());
              cout << multiply_ans << std::endl;
              continue;
            }
          else if (3 == input)
            {
              float subtract_ans = std::accumulate(numbers_float.begin() + 1, numbers_float.end(), numbers_float[0], std::minus<float>());
              cout << subtract_ans << std::endl;
              continue;
            }
          else if (4 == input)
            {
              float division_ans = std::accumulate(numbers_float.begin() + 1, numbers_float.end(), numbers_float[0], std::divides<float>());
              cout << division_ans << std::endl;
              continue;
            }
        }
      if (5 == input)
        {
          return 0;
        }
      else
        {
          cout << "Invalid option \"" << input << "\"" << std::endl;
          continue;
        }
    }
}
