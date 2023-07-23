#include <iostream>
#include <chrono>
#include <thread>

void critical(int sleep_ms)
{
  std::cout << "in critical\n";
  std::this_thread::sleep_for (std::chrono::milliseconds(sleep_ms));
}

int main(int argc, char* argv[])
{
  if (argc < 3) {
    std::cerr << "usage: progname <num_iterations> <sleep_ms_for_critical>\n";
    return 1;
  }

  auto n = std::stoi(argv[1]);
  auto sleep_ms = std::stoi(argv[2]);

  for (std::size_t i = 0; i < n; ++i)
    {
      auto start = std::chrono::high_resolution_clock::now();
      std::cout << "----\nentering critical\n";
      critical(sleep_ms);
      auto end = std::chrono::high_resolution_clock::now();
      auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
      std::cout << "out of critical : waited " << duration.count() << " ms\n";
    }
}
