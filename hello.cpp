#include <iostream>
#include <chrono>
#include <thread>

void critical()
{
  std::cout << "in critical\n";
  std::this_thread::sleep_for (std::chrono::seconds(3));
}

int main()
{
  std::cout << "hi\n";
  
  int n = 20;
  for (std::size_t i = 0; i < n; ++i)
    {
      auto start = std::chrono::high_resolution_clock::now();
      std::cout << "entering critical\n";
      critical();
      std::cout << "out of critical\n\n";
      auto end = std::chrono::high_resolution_clock::now();
      auto duration = duration_cast<microseconds>(stop - start);
      std::cout << "Waited " << duration.count() << '\n';
    }
}
