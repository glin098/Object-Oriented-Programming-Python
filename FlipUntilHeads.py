#Consider a single experiment of flipping a fair coin until an outcome
#of “heads” and counting the number of flips that occur.
#Write a for loop that repeats 10,000 trials of this experiment

from random import randrange

clist = []
count = 0

for x in range(1,10000+1):
    flip = randrange(2)
    if (flip == 0): #tails
        count+=1
    elif (flip == 1): #heads
        if count != 0:
            clist.append(count)
            count = 0
            tails = False
print('Average number of flips: ', sum(clist)/len(clist))
print('Maximum number of flips: ', max(clist))
