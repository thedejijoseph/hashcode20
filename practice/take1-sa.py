problem = open('a_example.in').read().splitlines()

M, K = problem[0].split(' ')
M = int(M); K = int(K)

pool = [int(_) for _ in problem[1].split(' ')]

chosen = []
tally = 0

for _ in range(len(pool)):
    c = pool[_]
    if tally + c <= M:
        tally += c
        chosen.append(_)
    else:
        pass

print(chosen)