#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <cstddef>
#include <tuple>
#include <ctype.h>
#include "../utils/cpp_utils.h"
using namespace std;

vector<string> read_file(const string& input_path) {
    ifstream inputFile(input_path);
    vector<string> lines;

    if (!inputFile.is_open()) {
        cerr << "Error opening the file!" << endl;
        return lines;
    }

    string line;
    while (getline(inputFile, line)) {
        lines.push_back(line);
    }

    // Close the file
    inputFile.close();
    return lines;
}

vector<string> split(string s, string delimiter){
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    std::string token;
    std::vector<std::string> res;
    while ((pos_end = s.find(delimiter, pos_start)) != std::string::npos) {
        token = s.substr (pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back (token);
    }
    res.push_back (s.substr (pos_start));
    return res;
}

unordered_map<int, int> map_data(vector<string>input_data){
    tuple <int, int> grid(input_data.size(), input_data[0].size());
    int counter;
    int start_pos;
    bool is_obj = false;
    unordered_map<int, int> mapping;
    for (auto it : input_data) {
        for (char i: it){
            if (isdigit(i)){
                if (!is_obj){
                    is_obj = true;
                    start_pos = counter;
                    mapping[counter] = counter;
                }
                else {
                    mapping[start_pos] = counter;
                }
            }
            else {
                if (is_obj){
                    is_obj = false;
                }
            counter += 1;
            }
        }
    }
    return mapping;
}

int main(){
    string input_path = "test.txt";
    vector<string> data = read_file(input_path);
    tuple <int, int> grid(data.size(), data[0].size());
    unordered_map<int, int> positions = map_data(data);

}