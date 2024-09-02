#include <cstddef>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map> 

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

int is_possible(string game, unordered_map<string, int> ans){
    string game_id = split(game, ":")[0];
    int cube_value = 1;
    int game_id_value = stoi(game_id.substr(4));
    unordered_map<string, int> max_map = {
        {"red", 0},
        {"blue", 0},
        {"green", 0}
    };
    for (auto color=max_map.begin(); color != max_map.end(); ++color){
        if (game.find(color->first) == std::string::npos) {
            continue;
        }
        vector<string> appearances = split(game, color->first);
        appearances.pop_back();
        int idx = 0;
        for (auto appearance: appearances){
        vector<string> m = split(appearance, " ");
        int n = stoi(m[m.size() -2]);
        if (n > max_map[color->first]){
            max_map[color->first] = n;
        }
        }
        cube_value *= max_map[color->first];
    }
    return cube_value;
}

int main(){
    unordered_map<string, int> ans_map;
    ans_map["red"] = 12;
    ans_map["green"] = 13;
    ans_map["blue"] = 14;
    string input_file = "input.txt";
    int sum = 0;
    vector content = read_file(input_file);
    for (const string& line:content){
        sum += is_possible(line, ans_map);
    }
    cout << sum << endl;
}