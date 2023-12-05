import functools
input = [line.split(': ')[1].split('; ') for line in open('day2.txt').read().split('\n')]
game_to_test = {'red': 12, 'green': 13, 'blue': 14}
part1, part2 = 0,0
for i in range(len(input)):
    game = input[i]
    dice_seen = {'red': 0, 'green': 0, 'blue': 0}
    for round in game:
        for draw in round.split(', '):
            quant, color = draw.split(' ')
            dice_seen[color] = max(int(quant), dice_seen[color])
    if all(game_to_test[color] >= dice_seen[color] for color in game_to_test.keys()):
        part1 += i + 1
    part2 += functools.reduce(lambda a, b: a*b, list(dice_seen.values()))

print(part1)
print(part2)