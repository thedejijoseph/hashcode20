problem = open('a_example.in').read().splitlines()

M, K = problem[0].split(' ')
M = int(M); K = int(K)

pool = [int(_) for _ in problem[1].split(' ')]
pool = list(enumerate(pool))

import random

tally = 0
chosen = []

for _ in range(len(pool)):
    c = pool.pop(random.choice(range(len(pool))))
    pos, val = c

    if tally + val <= M:
        tally += val
        chosen.append(pos)
    else:
        pool.append(c)

print(chosen)