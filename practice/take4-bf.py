problem = open('c_medium.in').read().splitlines()

M, K = problem[0].split(' ')
M = int(M); K = int(K)

pool = [int(_) for _ in problem[1].split(' ')]
pool = list(enumerate(pool))

tally = 0
chosen = []

while True:
    diff = M - tally
    bath = list(filter(lambda x: tally + x[1] <= M, pool))
    if len(bath) > 0:
        hold = []
        for c in bath:
            pos, val = c
            dist = M - (tally + val)
            hold.append((pos, val, dist))
        
        choice = sorted(hold, key=lambda x: x[2])[0]
        tally += choice[1]
        chosen.append(choice[0])
        hold = []
        pool.pop(pool.index((choice[0], choice[1])))

    else:
        break

# this should give largely the same result as take2
# as the script essentially performs a downward search from greatest to lowest

# the 
print(sorted(chosen))