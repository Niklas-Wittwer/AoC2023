def process_data(path):
    input_data = [x.strip() for x in open(path, 'r').readlines() if x.strip()]
    hands = []
    for n in input_data:
        hands.append(n.split())
    return hands

def compute_type(hand):
    types = []
    for n in hand:
        if len(types) == 0:
            types.append([n])
        else:
            for i, l in enumerate(types):
                if n in l:
                    types[i].extend(n)
                    break
                elif i == len(types)-1:
                    types.append([n])
                    break
                    
    n = len(types)
    if n == 1:
        return 7
    elif n == 2:
        if len(types[0]) == 1 or len(types[0]) == 4:
            return 6
        else:
            return 5
    elif n == 3:
        if len(types[0]) == 2 or len(types[1]) == 2:
            return 3
        else:
            return 4
    elif n == 4:
        return 2
    else:
        return 1

def compute_rank(hand):
    mapping = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
    }
    rank = ""
    rank += str(compute_type(hand[0]))
    for elem in hand[0]:
        n = mapping.get(elem, 0)
        if n == 0:
            n = "0"+str(elem)
        rank += str(n)
    hand[0] = int(rank)
    hand[1] = int(hand[1])
    return hand
    


def compute_score(hands):
    n = 0
    for i, hand in enumerate(hands):
        n += (i + 1)*hand[1]
    return n

if __name__ == "__main__":
    datapath = "test.txt"
    hands = process_data(datapath)
    for i, hand in enumerate(hands):
        hands[i] = compute_rank(hand)
    hands.sort(key = lambda x: x[0])
    print(compute_score(hands))
    

