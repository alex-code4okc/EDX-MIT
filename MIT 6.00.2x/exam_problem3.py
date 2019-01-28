import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 1000
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO

    # do not allow the population of rabbits to increase beyond 1000
    if CURRENTRABBITPOP>MAXRABBITPOP:
        CURRENTRABBITPOP = MAXRABBITPOP
    if CURRENTRABBITPOP<10:
        CURRENTRABBITPOP = 10

    rabbit_reproduction_probability = (1 - float(CURRENTRABBITPOP/MAXRABBITPOP))

    if (random.random()<=rabbit_reproduction_probability):
        CURRENTRABBITPOP+=1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO

    #if CURRENTFOXPOP<10:
    #    CURRENTFOXPOP=10

    for fox in range(CURRENTFOXPOP):
        if(random.random()<= float(CURRENTRABBITPOP/MAXRABBITPOP)):
            if(CURRENTRABBITPOP>10):
                CURRENTRABBITPOP-=1
                # fox gets to eat rabbit if population is greater than 10
                if(random.random()<=float(1/3)): #since it ate a rabbit, it has 1/3 chance of generating offspring
                    CURRENTFOXPOP+=1
        else:
            if(random.random()<=float(1/10)):
                CURRENTFOXPOP-=1

    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_populations = [0]*numSteps
    fox_populations = [0]*numSteps


    for timeStep in range(numSteps):
        if CURRENTFOXPOP<10:
            rabbitGrowth()
            rabbit_populations[timeStep] = CURRENTRABBITPOP
        else:
            rabbitGrowth()
            rabbit_populations[timeStep] = CURRENTRABBITPOP
            foxGrowth()
            fox_populations[timeStep] = CURRENTFOXPOP

    pylab.plot(rabbit_populations)
    pylab.plot(fox_populations)
    pylab.show()
    return (rabbit_populations, fox_populations)

    '''else:
        for timeStep in range(numSteps):
            rabbitGrowth()
            rabbit_populations[timeStep] = CURRENTRABBITPOP
            foxGrowth()
            fox_populations[timeStep] = CURRENTFOXPOP

        pylab.plot(rabbit_populations)
        pylab.plot(fox_populations)
        pylab.show()
        return (rabbit_populations, fox_populations)'''
