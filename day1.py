import re
input = open('day1.txt').read()
line_to_num = lambda line: re.sub('\D', '', line)
line_sum = lambda line_num: int(line_num[0] + line_num[-1])
part1 = sum(map(line_sum, map(line_to_num, input.split('\n'))))
print(part1)


nums = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
match_str = r'(?=(nine|eight|seven|six|five|four|three|two|one|\d))'
match_handler = lambda match: str(nums.index(match)) if match in nums else match

# imperatively:
part2 = 0
for input_line in input.split('\n'):
    num_list = list(map(match_handler, re.findall(match_str, input_line)))
    part2 += int(num_list[0] + num_list[-1])
print(part2)


# functionally: 
part2 = sum(map(
    lambda num_list: int(num_list[0] + num_list[-1]),
    [list(map(match_handler, re.findall(match_str, input_line))) for input_line in input.split('\n')]
))
print(part2)