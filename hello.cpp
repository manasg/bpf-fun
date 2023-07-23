#include <iostream>


void critical()
{
  std::cout << "in critical\n";
}

int main()
{
  std::cout << "hi\n";
  
  int n = 20;
  for (std::size_t i = 0; i < n; ++i)
    {
      std::cout << "entering critical\n";
      critical();
      std::cout << "out of critical\n\n";
    }
}
