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

def translate_ranges(oldranges, newranges):
    newranges = []
    for newrange in newranges:
        rangeholder = [None, None]
        for oldrange in oldranges:
            if newrange[0] > sum(oldrange) or newrange[0] + newrange[2] < oldrange[0]:
                continue
            else:
                if not rangeholder[0]:
                    rangeholder = [max(sum(newrange[1:]), oldrange[0])-newrange[1]]
                else:
                    rangeholder = [max, min]
    newranges.extend(oldranges)
    return newranges


if __name__=="__main__":
    path = "day 5/input.txt"
    seeds, maps, data = read_data(path)
    seeds = [eval(n) for n in seeds]
    maps = create_maps(data, maps)
    print(seeds)
    ranges = translate_ranges(maps, seeds)
