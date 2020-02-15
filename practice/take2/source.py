filename = 'e_also_big.in'
problem = open(filename).read().splitlines()

M, K = problem[0].split(' ')
M = int(M); K = int(K)

pool = [int(_) for _ in problem[1].split(' ')]
pool = list(enumerate(pool))

chosen = []
tally = 0

for c in sorted(pool, key=lambda x: x[1], reverse=True):
    pos, val = c
    if tally + val <= M:
        tally += val
        chosen.append(pos)
    else:
        pass

chosen = sorted(chosen)
submission = f'take2\{filename}'
with open(submission, 'w') as f:
    f.write(f'{len(chosen)}\n')
    f.write(' '.join([str(_) for _ in chosen]))