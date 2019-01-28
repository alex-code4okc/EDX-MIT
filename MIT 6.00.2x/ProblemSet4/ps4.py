# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#
#from ProblemSet4.ps3b import simulationWithDrug


def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    :type numTrials: int
    """

    firstAddition = 150
    secondAddition = 0
    initialViruses = 100
    maxViralCapacity = 1000
    birthProb = .1
    clearProb = .05
    antibiotics = {'guttagonol': False, 'grimpex': False}
    mutRate = .005


    delay150 = simulationWithDrug(initialViruses, maxViralCapacity, birthProb, clearProb, antibiotics, mutRate, numTrials, firstAddition,secondAddition)
    pylab.hist(delay150)
    pylab.title('Final viral population after drug addition at '+str(firstAddition)+' steps and 2nd at '+str(secondAddition))
    pylab.xlabel('Final Viral Population')
    pylab.ylabel('Total Number of Trials')
    pylab.show()
    '''
    #delay150 = ps3b.simulationWithDrugs()
    #delay75 = ps3b.simulationWithDrugs()
    #delay0 = ps3b.simulationWithDrugs()'''






#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
