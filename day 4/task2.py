import copy
# preprocess data
def read_data():
    input_data = [x.strip() for x in open("input.txt", "r").readlines()]
    guesses = []
    winners = []
    cards = {}
    for n in input_data:
        cards[n.split(":")[0].replace(" ", "")] = 1
        guesses.append(n.split("|")[0].split()[2:])
        winners.append(n.split("|")[1].split())
    card_wins = copy.deepcopy(cards)
    return guesses, winners, cards, card_wins


def count_points(guesses, winners):
    n_correct = 0
    for n in guesses:
        if n in winners:
            n_correct += 1
    return n_correct

if __name__ == "__main__":
    guesses, winners, cards, card_wins = read_data()
    for i,(guess,winner) in enumerate(zip(guesses, winners)):
        card_wins["Card" + str(i + 1)] = count_points(guess, winner)
        for n in range(card_wins.get("Card" + str(i + 1))):
            cards["Card" + str(n + 2 + i)] += cards.get("Card" + str(1 + i))
    print(cards)
    tot_scrapecards = 0
    for n in cards.values():
        tot_scrapecards+= n
    print(tot_scrapecards)