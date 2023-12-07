import re
import numpy as np
import functools
file = 'day6.txt'
part1_input = [[int(num) for num in re.findall(r'\d+', line)] for line in open(file).read().split('\n')]
part2_input = [int(re.sub(r'\D', '', line)) for line in open(file).read().split('\n')]

def race_winning_options(time, dist):
    lower = np.floor(((time - np.sqrt(time*time - 4*dist)) / 2) + 1) # quadratic formula magic
    upper = np.ceil(((time + np.sqrt(time*time - 4*dist)) / 2) - 1)
    return int(1 + upper - lower)

race_options_generator = (race_winning_options(time, dist) for time, dist in zip(part1_input[0], part1_input[1]))
part1 = functools.reduce(lambda a, b: a*b, race_options_generator)
part2 = race_winning_options(part2_input[0], part2_input[1])
print(part1)
print(part2)