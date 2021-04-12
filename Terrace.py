##############################################
# implement a Terrace class here that supports:
#  - constructor that accepts terrace capacity as parameter
#  - processEnter(n) function to model arrival of n people
#  - processLeave(n) function to model departure of n people
#  - getNumDenied() function that returns total number of GROUPS
#                   thus far denied during the simulation
##############################################
class Terrace:
    def __init__(self, capacity):
        self._spaceRemaining = capacity
        self._numDenied = 0

    def processEnter(self, numP):
        self._spaceRemaining -= numP
        if self._spaceRemaining >= 0:
            return True
        else:
            self._spaceRemaining += numP
            self._numDenied += 1
            return False

    def processLeave(self, numP):
        # Note: contest promises that numP <= self._current
        self._spaceRemaining += numP

    def getNumDenied(self):
        return self._numDenied
        

##############################################
# Do not change anything below this line
##############################################

if __name__ == '__main__':
    limit,n = [int(k) for k in input().split()]
    terrace = Terrace(limit)
    for _ in range(n):
        pieces = input().split()
        j = int(pieces[1])
        if pieces[0] == 'enter':
            terrace.processEnter(j)
        else:
            terrace.processLeave(j)

    print(terrace.getNumDenied())
