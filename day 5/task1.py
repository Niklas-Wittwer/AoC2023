import re

def read_data(datapath):
    input_data = [x.strip() for x in open(datapath, "r").readlines() if x.strip()]
    seeds = re.findall(r'[0-9]+', input_data[0])
    input_data = input_data[1:]
    mapping = {
        "seed" : [],
        "soil" : [],
        "fertilizer" : [],
        "water" : [],
        "light" : [],
        "temperature" : [],
        "humidity" : [],
    }
    return seeds, mapping, input_data


def create_maps(data, maps):
    keys = [key for key in maps.keys()]
    iterator = 0
    for elem in data[1:]:
        if re.search("\D", elem.replace(" ", "")):
            iterator +=1
            continue
        n = [int(n) for n in elem.split()]
        maps[keys[iterator]].append(n)
    return maps

def calculate_mapping(maps, seed):
    locations = []
    for seed in seeds:
        for key in maps.keys():
            for ranges in maps[key]:
                if ranges[1] <= seed <sum(ranges[1:]):
                    seed = ranges[0] + seed - ranges[1]
                    break
        locations.append(seed)
    return locations


if __name__=="__main__":
    path = "day 5/input.txt"
    seeds, maps, data = read_data(path)
    seeds = [eval(n) for n in seeds]
    maps = create_maps(data, maps)
    print(seeds)
    locations = calculate_mapping(maps, seeds)
    print(maps, locations)
    print(min(locations))
