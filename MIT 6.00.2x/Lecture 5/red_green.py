def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here
    # perform odds of drawing three balls out of 6 for numTrials times.
    # cannot focus on just one color. Must focus on all red, or all green.
    import random
    # if all 3 draws are same color, add 1 to anyThreeOfSameColor
    anyThreeOfSameColor = 0
    numTimesRandomCalled = 0
    for trail in range(numTrials):
        # container gets created every trial
        ball_container = ['red', 'red', 'red', 'green', 'green', 'green']
        trialContainer = [] # accepts items popped from ballcontainer and collects them
        # shuffle ballcontainer for "true" randomness
        random.shuffle(ball_container)
        numTimesRandomCalled +=1
        for i in range(3):
            trialContainer.append(ball_container.pop())
        if ( (trialContainer[0]=='red'and trialContainer[1]=='red'and trialContainer[2]=='red') or (trialContainer[0]=='green' and trialContainer[1]=='green' and trialContainer[2]=='green') ):
            anyThreeOfSameColor +=1
    #print(anyThreeOfSameColor/float(numTrials))
    return anyThreeOfSameColor/float(numTrials), numTimesRandomCalled
