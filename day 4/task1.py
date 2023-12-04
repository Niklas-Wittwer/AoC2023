# preprocess data
def read_data():
    input_data = [x.strip() for x in open("input.txt", "r").readlines()]
    guesses = []
    winners = []
    cards = {}
    for n in input_data:
        cards[n.split(":")[0]] = 0
        guesses.append(n.split("|")[0].split()[2:])
        winners.append(n.split("|")[1].split())
    return guesses, winners


def count_points(guesses, winners):
    n_correct = 0
    for n in guesses:
        if n in winners:
            n_correct += 1
    points = 2**(n_correct-1) if n_correct>=3 else n_correct
    return points

if __name__ == "__main__":
    guesses, winners = read_data()
    total_points = 0
    for guess,winner in zip(guesses, winners):
        pts = count_points(guess, winner)
        total_points += pts
    print(total_points)
