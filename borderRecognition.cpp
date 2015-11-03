#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  std::ifstream fin("img/1.jpg", std::ios::in | std::ios::binary);
  std::ostringstream oss;
  oss << fin.rdbuf();
  std::string data(oss.str());
  return 0;
}
