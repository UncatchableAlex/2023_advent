input = [[int(num) for num in line.split(' ')] for line in open('day9.txt').read().split('\n')]
part1 = 0
part2 = 0
for line in input:
    histories = [line]
    # build histories
    while any(digit != 0 for digit in histories[-1]):
        new_history = [histories[-1][i] - histories[-1][i - 1] for i in range(1, len(histories[-1]))]
        histories.append(new_history)
    # extrapolate new values in histories
    for i in range(len(histories) - 2, -1, -1):
        histories[i].append(histories[i][-1] + histories[i + 1][-1])
        histories[i].insert(0, histories[i][0] - histories[i+1][0])
    part1 += histories[0][-1]
    part2 += histories[0][0]

print(part1)
print(part2)