from bisect import bisect
input = open('day11.txt').read().split('\n')
galaxies = [(i,j) for i in range(len(input)) for j in range(len(input[i])) if input[i][j] == '#']
empty_cols = [i for i in range(len(input[0])) if all(input[j][i] == '.' for j in range(len(input)))]
empty_rows = [i for i in range(len(input)) if all(input[i][j] == '.' for j in range(len(input[i])))]
part1 = 0
part2 = 0
for i in range(len(galaxies)):
    for j in range(i):
        num_empty_cols = abs(bisect(empty_cols, galaxies[i][1]) - bisect(empty_cols, galaxies[j][1]))
        num_empty_rows = abs(bisect(empty_rows, galaxies[i][0]) - bisect(empty_rows, galaxies[j][0]))
        raw_dist = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
        part1 += num_empty_cols + num_empty_rows + raw_dist
        part2 += 999999 * (num_empty_cols + num_empty_rows) + raw_dist
print(part1)
print(part2)
