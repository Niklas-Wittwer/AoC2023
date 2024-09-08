#include "cpp_utils.h" 
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