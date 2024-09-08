#ifndef  UTILS_CPP_H
#define UTILS_CPP_H

#include <string>
#include <vector>
#include <cstddef>
#include <fstream>
#include <iostream>

std::vector<std::string>read_file(const std::string& input_path);
std::vector<std::string> split(std::string s, std::string delimiter);
#endif