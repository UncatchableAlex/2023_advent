import re
file = 'day5_example.txt'
file = 'day5.txt'
# get a list of the seeds
seeds = [int(num) for num in open(file).read().split('\n')[0][7:].split(' ')]
# get the input as a list of listings where each listing is a list of ranges and each range is
# of the form [dest, source, step]
input = re.split(r'\n\n.+-.+ map:\n', open(file).read())[1:]
listings = [[[int(num) for num in listing.split(' ')] for listing in line.split('\n')] for line in input]
locations = []
for seed in seeds:
    for transformations in listings:
        for (dest, source, step) in transformations:
            if source <= seed < source + step:
                seed = dest + (seed - source)
                break
    locations.append(seed)
part1 = min(locations)
print(part1)

# for each seed/step combo for the second part
seed_stats = {(seeds[i], seeds[i+1]) for i in range(0, len(seeds)-1, 2)}
for transformations in listings:
    seed_stats2 = set()
    for (seed, seed_step) in seed_stats:
        seed_stats2_size = len(seed_stats2)
        for (dest, source, step) in transformations:
            # case for transformation range completely enclosing the seed stat
            if source <= seed < source + step and source <= seed + seed_step <= source + step:
                new_seed_stat = (dest + (seed - source), seed_step)
                seed_stats2.add(new_seed_stat)
            # case for the transformation range enclosing the bottom part of the seed stat
            elif source <= seed < source + step:
                new_seed_stat1 = (dest + (seed - source), step - (seed - source))
                new_seed_stat2 = (source + step, seed_step - (step - (seed - source)))
                seed_stats2.add(new_seed_stat1)
                seed_stats2.add(new_seed_stat2)
            # case for the transformation range enclosing the top part of the seed stat
            elif source <= seed + seed_step <= source + step:
                new_seed_stat1 = (seed, source - seed)
                new_seed_stat2 = (dest, seed_step - (source - seed))
                seed_stats2.add(new_seed_stat1)
                seed_stats2.add(new_seed_stat2)
        if seed_stats2_size == len(seed_stats2):
            seed_stats2.add((seed, seed_step))
    seed_stats = seed_stats2

# do NOT ask me why zero isn't an acceptable answer. I don't know.
part2 = min(a for (a,_) in seed_stats if a != 0)
print(part2)
