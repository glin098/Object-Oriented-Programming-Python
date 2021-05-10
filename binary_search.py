#########################################################
# Don't bother reading this first part. It simply provides
# a debug() function that will help us trace our code.
###########################################################
import inspect

def debug():
    info = inspect.stack()[1]
    name = info[3]
    f = globals()[name]
    signature = inspect.signature(f)
    local = info[0].f_locals
    param = []
    for formal in signature.parameters:
        actual = local[formal]
        if isinstance(actual,list):
            param.append(formal)
        else:
            param.append(str(actual))
    print("%s(%s)" % (name, ', '.join(param)))


###########################################################
# Okay...time to start reading, and writing code.
###########################################################


def contains(data, target, start, stop):
    debug()
    if start >= stop:# empty range
        return stop
        return False
        
    else:
        midIndex = (start + stop) // 2                     # look here
        if target == data[midIndex]:# found it
            if target==data[midIndex-1]:
                return midIndex-1
            return midIndex
            return True
        elif target < data[midIndex]:                      # check left side
            return contains(data, target, start, midIndex)
        else:                                              # check right side
            return contains(data, target, midIndex+1, stop)

def find(data, target, start, stop):
    debug()
    if start >= stop:# empty range
        return stop
        return False
        
    else:
        midIndex = (start + stop) // 2                     # look here
        if target == data[midIndex]:# found it
            #if target==data[midIndex-1]:
                #return midIndex-1
            return midIndex
            return True
        elif target < data[midIndex]:                      # check left side
            return contains(data, target, start, midIndex)
        else:                                              # check right side
            return contains(data, target, midIndex+1, stop)

def location(data, target, start, stop):
    debug()
    if start >= stop:# empty range
        return stop
        return False
        
    else:
        midIndex = (start + stop) // 2                     # look here
        if target == data[midIndex]:# found it
            #if target==data[midIndex-1]:
                #return midIndex-1
            return midIndex
            return True
        elif target < data[midIndex]:                      # check left side
            return contains(data, target, start, midIndex)
        else:                                              # check right side
            return contains(data, target, midIndex+1, stop)

def index(data, target, start, stop):
    debug()
    if start >= stop:# empty range
        return stop
        return False
        
    else:
        midIndex = (start + stop) // 2                     # look here
        if target == data[midIndex]:# found it
            j = 0 
            while True:
                if len(data) == midIndex-j:
                    return midIndex-j+1
                if target != data[midIndex-j]:
                    return midIndex-j+1
                else:
                    j += 1
        elif target < data[midIndex]:                      # check left side
            return index(data, target, start, midIndex)
        else:                                              # check right side
            return index(data, target, midIndex+1, stop)


        """while True: #not sure if this is right
        midIndex=(start+stop)//2
        if target==data[midIndex+1]:
            return midIndex+1
        else:
            return False"""

def rindex(data, target, start, stop): #doesn't work right
    debug()
    #print(start)
    #print(stop)
    if start >= stop:# empty range
        return stop
        return False
        
    else:
        midIndex = (start + stop) // 2                     # look here
        if target == data[midIndex]:# found it
            j = 0 
            while True:
                if len(data) == midIndex+j:
                    return midIndex+j-1
                if target != data[midIndex+j]:
                    return midIndex+j-1
                else:
                    j += 1
            return True
        elif target < data[midIndex]:                      # check left side
            return rindex(data, target, start, midIndex)
        else:                                              # check right side
            return rindex(data, target, midIndex+1, stop)
        

    
def count(data,target):
    x=index(data,target,0,len(data))
    print(x)
    y=rindex(data,target,0,len(data))
    print(y)
    if y != x:
        count=(y-x) + 1
        return count
    else:
        return 0







###########################################################
# Finally, a place for tests. We've started you out, but you
# should add more as you work through the exploration
###########################################################

if __name__ == '__main__':

    sample = sorted('FIRSTPROBLEM')   # our first example list
    duplicates = sorted(3*'HELLO')    # our second example list

    
    """print(rindex(duplicates, 'O', 0, len(duplicates)))

    print()
    print(rindex(duplicates, 'L', 0, len(duplicates)))"""

    print(count(duplicates, 'O'))


#    print()
#    print(find(sample, '', 0, len(sample)))

#    print()
#    print(find(sample, 'Q', 0, len(sample)))
        







###########################################################
# Finally, a place for tests. We've started you out, but you
# should add more as you work through the exploration
###########################################################

if __name__ == '__main__':

    sample = sorted('FIRSTPROBLEM')   # our first example list
    duplicates = sorted(3*'HELLO')    # our second example list

    
    """print(rindex(duplicates, 'O', 0, len(duplicates)))

    print()
    print(rindex(duplicates, 'L', 0, len(duplicates)))"""

    print(count(duplicates, 'O'))


#    print()
#    print(find(sample, '', 0, len(sample)))

#    print()
#    print(find(sample, 'Q', 0, len(sample)))
