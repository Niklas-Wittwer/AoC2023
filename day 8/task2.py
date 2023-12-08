import re
from math import gcd
from functools import reduce

def read_data(datapath):
    input_data = [x.strip() for x in open(datapath, "r").readlines() if x.strip()]
    map_dict = {}
    pathing = input_data.pop(0)
    return map_dict, pathing, input_data


def fill_map(map_dict, nodes):
    pos_list = []
    for node in nodes:
        pos = node.split("=")[0].strip()
        instruction = [re.sub(r'[()]', "", n).strip() for n in node.split("=")[1].strip().split(",")]
        map_dict[pos] = instruction
        if pos.endswith("A"):
            pos_list.append(pos)
    return map_dict, pos_list

def find_path(map_dict, pathing, pos="AAA", step_counter=0):
    path_dict = {
        "R": 1,
        "L": 0,
    }
    for n in pathing:
        step = path_dict[n]
        pos = map_dict[pos][step]
        step_counter += 1
        if pos.endswith("Z"):
            return step_counter
    return find_path(map_dict, pathing, pos, step_counter)
    
    
def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)    


if __name__ == "__main__":
    path = "day 8/input.txt"
    map_dict, pathing, input_data = read_data(path)
    map_dict, pos_list = fill_map(map_dict, input_data)
    n_steps = []
    for pos in pos_list:
        n_steps.append(find_path(map_dict, pathing, pos))
    print(lcm(n_steps))