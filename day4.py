import re
input = [line.split(': ')[1].split(' | ') for line in open('day4.txt').read().split('\n')]
part1 = 0
card_scores = []
for game in input:
    # This next line exploits the fact that there aren't any duplicate numbers.
    # The set intersection trick does NOT work in the case of duplicates.
    overlapping_nums = set(re.findall(r'\d+', game[0])) & set(re.findall(r'\d+', game[1]))
    part1 += int(2**(len(overlapping_nums) - 1))
    card_scores.append([len(overlapping_nums), 1])

print(part1)
for i in range(len(card_scores)):
    for j in range(i + 1, i + card_scores[i][0] + 1):
        card_scores[j][1] += card_scores[i][1]

part2 = sum(card_score[1] for card_score in card_scores) 
print(part2)
