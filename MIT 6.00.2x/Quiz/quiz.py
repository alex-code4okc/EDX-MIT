import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here

    trials = []

    def drawingFromBucket():
        '''returns True or False depending on whether three draws form bucket \
    are the same'''
        bucket = [0,0,0,0,1,1,1,1]
        capture = []

        for i in range(3):
            random.shuffle(bucket)
            capture.append(bucket.pop())
        
        if ( (capture[0]==0 and capture[1]==0 and capture[2]==0) or (capture[0]==1 and capture[1]==1 and capture[2]==1)):
            return True
        else:
            return False

    for x in range(numTrials):
        trials.append(drawingFromBucket())

    print(trials)

    return trials.count(True)/float(len(trials))
