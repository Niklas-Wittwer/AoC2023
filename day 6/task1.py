import re
import math
def read_data(datapath):
    input_data = [x.strip() for x in open(datapath, "r").readlines() if x.strip()]
    time , distance = re.findall(r'[0-9]+', input_data[0]), re.findall(r'[0-9]+', input_data[1])
    return time, distance


def calc_possible_wins(time, distance):
    dis = time**2 - (-1*4*(-distance))
    x1 = (time - math.sqrt(dis))/(2 * (1))
    x2 = (time + math.sqrt(dis))/(2 * (1))
    return x1, x2


if __name__ == "__main__":
    path = "day 6/input.txt"
    times, distances = read_data(path)
    n_wins = 1
    for x, y in zip(times, distances):
        x1, x2 = calc_possible_wins(int(x), int(y))
        print(x1, x2)
        wins = x2-x1 - 1  if (x2-x1)%1==0 else int(x2) - int(x1)
        print(wins)
        n_wins *= wins if wins > 0 else 1
    print(n_wins)
