/* Exercise 4 from LCTHW, note that it the following code is wrong on purpose

int main()
{
  int age = 16;
  int height;

  printf("I be %d years old.\n");
  printf("I am %d inches tall.\n", height);

  return 0;
}
*/

// Correct code

#include <stdio.h>

int main()
{
  int age = 16;
  int height = 528491;

  printf("I be %d years old.\n", age);
  printf("I am %d inches tall.\n", height);

  return 0;
}
