import functools
import collections
import re
input = [(line.split(' ')[0], int(line.split(' ')[1])) for line in open('day7.txt').read().split('\n')]

def hand_type(hand):
    mc = collections.Counter(hand).most_common(5)
    if mc[0][1] == 5:
        return 0
    # four of a kind
    elif mc[0][1] == 4:
        return 1
    # full house
    elif mc[0][1] == 3 and mc[1][1] == 2 :
        return 2
    # 3 of a kind
    elif mc[0][1] == 3:
        return 3
    # two pair
    elif mc[0][1] == 2 and mc[1][1] == 2:
        return 4
    # one pair
    elif mc[0][1] == 2:
        return 5
    else:
        return 6
    
def hand_type_joker(hand):
    counter = collections.Counter(re.sub('J', '', hand))
    jokers = collections.Counter(hand)['J']
    mc = counter.most_common(5)
    if len(mc) == 0 or mc[0][1] + jokers == 5:
        return 0
    # four of a kind
    elif mc[0][1] + jokers == 4:
        return 1
    # full house
    elif (3 - mc[0][1]) + (2 - mc[1][1]) <= jokers:
        return 2
    # 3 of a kind
    elif mc[0][1] + jokers == 3:
        return 3
    # two pair
    elif (2 - mc[0][1]) + (2 - mc[1][1]) <= jokers:
        return 4
    # one pair
    elif 2 - mc[0][1] <= jokers:
        return 5
    else:
        return 6
    
    
        
def hand_comparator(a, b, joker):
    if joker:
        typea = hand_type_joker(a[0])
        typeb = hand_type_joker(b[0])
    else:
        typea = hand_type(a[0])
        typeb = hand_type(b[0])
    if typea < typeb:
        return 1
    if typea > typeb:
        return -1
    else:
        card_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
        numberified_cards = [(tuple(map(lambda letter: card_order.index(letter), card)), card) for card in [a[0],b[0]]]
        ordered_hands = sorted(numberified_cards, key=lambda numberified_card: numberified_card[0])
        if ordered_hands[0][1] == a[0]:
            return 1
        else:
            return -1
    
        

ordered_hand_1 = sorted(input, key=functools.cmp_to_key(lambda a, b: hand_comparator(a,b,joker=False)))
part1 = sum((i+1) * ordered_hand_1[i][1] for i in range(len(ordered_hand_1)))
print(part1)

ordered_hand_2 = sorted(input, key=functools.cmp_to_key(lambda a, b: hand_comparator(a,b,joker=True)))
part2 = sum((i+1) * ordered_hand_2[i][1] for i in range(len(ordered_hand_2)))
print(part2)
