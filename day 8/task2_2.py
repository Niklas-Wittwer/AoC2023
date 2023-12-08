import re
import numba

def read_data(datapath):
    input_data = [x.strip() for x in open(datapath, "r").readlines() if x.strip()]
    map_list = []
    pathing = input_data.pop(0)
    return map_list, pathing, input_data

def fill_map(map_list, nodes):
    pos_list = []
    for node in nodes:
        pos = node.split("=")[0].strip()
        instruction = [re.sub(r'[()]', "", n).strip() for n in node.split("=")[1].strip().split(",")]
        map_list.append([pos, instruction])
        if pos.endswith("A"):
            pos_list.append(pos)
    return map_list, pos_list

@numba.jit(nopython=True)
def find_path(map_list, pathing, pos_list, step_counter=0):
    path_dict = {
        "R": 1,
        "L": 0,
    }
    stop = False
    while not stop:
        for n in pathing:
            step = path_dict[n]
            for i, pos_info in enumerate(map_list):
                pos = pos_info[1][step]
                pos_list[i] = pos
                step_counter += 1
            for i, pos in enumerate(pos_list):
                if not pos.endswith("Z"):
                    break
                if i == len(pos_list) - 1:
                    return step_counter
            print(step_counter)

if __name__ == "__main__":
    path = "day 8/input.txt"
    map_list, pathing, input_data = read_data(path)
    map_list, pos_list = fill_map(map_list, input_data)
    n_steps = find_path(map_list, pathing, pos_list)
    print(n_steps)
