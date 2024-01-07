pipes = open('day10.txt').read().split('\n')
def get_next_p1(curr,visited,include_start=False):
    pipe = pipes[curr[0]][curr[1]]
    a,b = (),()
    north = (curr[0] - 1, curr[1])
    south = (curr[0] + 1, curr[1])
    east = (curr[0], curr[1] + 1)
    west = (curr[0], curr[1] - 1)
    if pipe == '|':
        a,b = north,south
    elif pipe == '-':
        a,b = east,west
    elif pipe == 'L':
        a,b = north, east
    elif pipe == 'J':
        a,b = north, west
    elif pipe == '7':
        a,b = south, west
    elif pipe == 'F':
        a,b = south, east
    in_bounds = lambda c: c[0] >= 0 and c[0] < len(pipes) and c[1] >= 0 and c[1] < len(pipes[c[0]])
    char = lambda c: pipes[c[0]][c[1]]
    if include_start:
        return [next for next in (a,b) if next and in_bounds(next) and char(next) != '.' and next not in visited.keys()]
    return [next for next in (a,b) if next and in_bounds(next) and char(next) != '.' and char(next) != 'S' and next not in visited.keys()]

def bfs(start, get_next):
    bfs = list(start)
    visited = {pos: 0 for pos in start}
    while bfs:
        size = len(bfs)
        for _ in range(size):
            curr = bfs.pop(0)
            for next in get_next(curr, visited):
                bfs.append(next)
                visited[next] = visited[curr] + 1
    return max(visited.values()), visited


# find the start (marked 'S') in our input
start = ()
for i in range(len(pipes)):
    try:
        j = pipes[i].index('S')
        start = (i,j)
        break
    except:
        continue
# find the starting positions for our p1 bfs:
starting_positions = []
for pos in [(start[0] - 1, start[1]), (start[0] + 1, start[1]), (start[0], start[1] - 1), (start[0], start[1] + 1)]:
    for node in get_next_p1(pos, {}, True):
        if node == start:
            starting_positions.append(pos)

res = bfs(starting_positions, get_next_p1)
part1 = res[0] + 1
print(part1)

visited = set(res[1].keys())
# replace the start with the corresponding pipe.
a,b = starting_positions[0], starting_positions[1]
rep = ''
if a[0] > b[0] and a[1] > b[1]:
    rep = 'L' if a[0] == start[0] else '7'
elif a[0] < b[0] and a[1] < b[1]:
    rep = 'L' if b[0] == start[0] else '7'
elif a[0] > b[0] and a[1] < b[1]:
    rep = 'J' if a[0] == start[0] else 'F'
elif a[0] < b[0] and a[1] > b[1]:
    rep = 'J' if b[0] == start[0] else 'F'
elif a[0] == b[0]:
    rep = '-'
elif a[1] == b[1]:
    rep = '|'
pipes[start[0]] = pipes[start[0]][:start[1]] + rep + pipes[start[0]][start[1] + 1:]
visited.add(start)

inside_points = []
for i in range(len(pipes)):
    for j in range(len(pipes[i])):
        count = 0
        if (i,j) in visited:
            continue
        prev = ''
        crossings = 0
        for k in range(i):
            if (k,j) in visited:
                if pipes[k][j] == '-':
                    crossings += 1
                    prev = ''
                if pipes[k][j] in ['F', '7']:
                    prev = pipes[k][j]
                curr = pipes[k][j]
                if (curr == 'J' and prev == 'F') or (curr == 'L' and prev == '7'):
                    crossings += 1
            else:
                prev = ''
        if crossings % 2 != 0:
            inside_points.append((i,j))

print(len(inside_points))
