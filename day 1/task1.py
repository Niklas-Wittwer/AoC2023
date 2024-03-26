def process_data(path):
    input_data = [x.strip() for x in open(path, 'r').readlines() if x.strip()]
    return input_data

def add_numbers(data):
    """
    function to find numbers in the text string and add them together
    """
    num_holder = []
    for line in data:
        numbers = [n for n in line if n.isdigit()]
        num_holder.append(int(numbers[0]+numbers[-1]))
    return sum(num_holder)
if __name__ == "__main__":
    path = "day 1/test.txt"
    data = process_data(path)
    n_sum = add_numbers(data)
    print(n_sum)