import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO

    pylab.hist(values,numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # TODO
    trials = []

    for trial in range(numTrials):
        rolls = []
        for throw in range(numRolls):
            rolls.append(die.roll())
        #accum is a list of same length as rolls containing 1's
        accum = [1]*len(rolls)
        index = 0
        prev = rolls[0]
        for e in rolls[1:]:
            if e == prev:
                accum[index] += 1
                prev = e
            else:
                prev = e
                index += 1

        #append the max value from accum into trials list
        trials.append( max(accum) )
        #print(rolls) # find out of the rolls agree with trials results
        #print(accum) # print the accumulated value of runs
    #print(trials)
    

    ylabel = 'Number of Trials'
    xlabel = 'Value of longest run in Trial'
    pylab.hist(trials)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.show()

    return sum(trials)/float(len(trials))
        
        
        
            
    
# One test case
#print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)

# code for going through a  list and finding the longest run

        
    
