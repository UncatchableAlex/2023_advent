import re
file = 'day3.txt'
syms = {sym for sym in open(file).read() if  not re.match(r'(\.|\d|\n)', sym)}
digits = {str(digit) for digit in range(0,10)}
input = open(file).read().split('\n')

def adjacent_to_sym(a,b):
    for i in range(max(0,a-1), min(a+2,len(input))):
        for j in range(max(0,b-1), min(b+2,len(input[i]))):
            if input[i][j] in syms:
                    return True
    return False

def get_num(a,b):
    lo,hi = b,b
    while lo > 0 and input[a][lo] in digits:
        lo -= 1
    if  input[a][lo] not in digits:
         lo += 1
    while hi < len(input[a]) and input[a][hi] in digits:
         hi += 1
    return int(input[a][lo:hi]), (a, lo, hi)

def gear_val(a,b):
    gear_ratios = []
    found_part_coordinates = set()
    for i in range(max(0,a-1), min(a+2,len(input))):
        for j in range(max(0,b-1), min(b+2,len(input[i]))):
            if input[i][j] in digits:
                    num = get_num(i,j)
                    if num[1] not in found_part_coordinates:
                        found_part_coordinates.add(num[1])
                        gear_ratios.append(num[0])
    total = 0
    for i in range(len(gear_ratios)):
         for j in range(i+1, len(gear_ratios)):
              total += gear_ratios[i] * gear_ratios[j]
    return total if len(gear_ratios) > 1 else 0

part1 = 0
part2 = 0
for i in range(len(input)):
    k = -1
    adj = False
    for j in range(len(input[i])):
        if input[i][j] in digits and k == -1:
            k = j
        if input[i][j] in digits and adjacent_to_sym(i,j):
            adj = True
        if input[i][j] not in digits and k != -1 and adj:
            part1 += int(input[i][k:j])
        elif j == len(input[i]) - 1 and k != -1 and adj:
            part1 += int(input[i][k:])
        if input[i][j] not in digits:
            k = -1
            adj = False
        if input[i][j] == '*':
             part2 += gear_val(i,j)

print(part1)
print(part2)
