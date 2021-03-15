from random import *

trials = 1000
k = 20
totalsteps = 0
minsteps = 0
maxsteps = 0

for i in range(trials):
    count = 0
    pos = 0
    while abs(pos) < k:
        count += 1
        pos += randrange(2)*2 -1
    totalsteps += count
    if i == 1:
        minsteps = count
        maxsteps = count
    else:
        minsteps = min(count, minsteps)
        maxsteps = max(count, maxsteps)
    
print('Average number of steps', totalsteps/trials)
print('Min number of steps', minsteps)
print('Max number of steps', maxsteps)
