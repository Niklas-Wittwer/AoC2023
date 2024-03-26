import re

def process_data(path):
    input_data = [x.strip() for x in open(path, 'r').readlines() if x.strip()]
    return input_data

def translate(data):
    sum_holder = 0
    for line in data:
        digit_holder = []
        for i, char in enumerate(line):
            if str(char).isdigit():
                digit_holder.append(str(char))
            for j, val in enumerate(["one", "two", "three", "four", "five","six", "seven", "eight", "nine"]):
                if line[i:].startswith(val):
                    digit_holder.append(str(j+1))
        sum_holder += int(digit_holder[0]+digit_holder[-1])
    return sum_holder


if __name__ == "__main__":
    path = "day 1/test2.txt"
    data = process_data(path)
    print(data)
    n_sum = translate(data)
    print(n_sum)
