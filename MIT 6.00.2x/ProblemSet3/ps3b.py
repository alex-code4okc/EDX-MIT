# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import numpy
import random
import pylab

# random.seed(0)
'''
Begin helper code
'''


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """


'''
End helper code
'''


#
# PROBLEM 2
#
class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """

    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.maxBirthProb = float(maxBirthProb)
        self.clearProb = float(clearProb)

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """

        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        :rtype: float
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """

        if random.random() <= self.getClearProb():
            return True
        else:
            return False

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        if random.random() <= self.getMaxBirthProb() * (1 - popDensity):
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        else:
            raise NoChildException


class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        :type maxPop: int
        :type viruses: list
        """
        self.viruses = viruses
        self.maxViralCapacity = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        :rtype: list[SimpleVirus]
        """
        return self.viruses

    def getMaxPop(self):
        """
        Returns the max population.
        :rtype: int
        """
        return self.maxViralCapacity

    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        :rtype: int
        """
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)

        :rtype: int
        """

        for virion in list(self.viruses):
            if virion.doesClear():
                self.viruses.remove(virion)

        currentPopDensity = self.getTotalPop() / float(self.getMaxPop())
        # print("current population ", self.getTotalPop())
        # print("current population density ", currentPopDensity)

        replicants = []

        for virus in self.viruses:
            try:
                tempVirus = virus.reproduce(currentPopDensity)
                if tempVirus:
                    replicants.append(tempVirus)
            except NoChildException:
                pass

        for newVirus in replicants:
            self.viruses.append(newVirus)

        return self.getTotalPop()


#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """

    # array holding numTrial patients, 1 for every trial
    patients = []

    numTimeSteps = 300
    timeSteps = list(range(numTimeSteps))  # list containing 1...300 time steps

    # initializes viralPop with initial zeroes
    viralPop = []
    for x in range(numTimeSteps):
        viralPop.append(0)

    # list initially containing zeroes will eventually the average of numTrial patients' viral populations at time step 1...300

    for trial in range(numTrials):
        # create the initial virus population of length numViruses
        initialVirusPop = []
        for virus in range(numViruses):
            initialVirusPop.append(SimpleVirus(maxBirthProb, clearProb))

        patients.append(Patient(initialVirusPop, maxPop))

        for time_step in range(numTimeSteps):
            patients[trial].update()  # update the patient at current trail: 1...numTrials
            viralPop[time_step] += float(
                patients[trial].getTotalPop())  # add the current viral population to the corresponding time step

    # averageViralPop = [x/numTimeSteps for x in viralPop]
    # the average should be every item in viralPop divided by the trial number i.e. number of patients
    pylab.plot(timeSteps, viralPop)
    pylab.title('Average viral population of ' + str(numTrials) + ' patients with 300 time steps each')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Viral Population')
    pylab.legend('Average')
    pylab.show()


#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = float(mutProb)

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        '''try:
            if self.resistances[drug]:
                return True
            else:
                return False
        except:
            pass'''
        try:
            return self.resistances[drug]
        except:
            raise KeyError

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        offSpringResistances = {}

        resistantToAll = True

        for drug in activeDrugs:
            resistantToAll = resistantToAll and self.isResistantTo(drug)

        if resistantToAll:
            for drug in self.resistances:
                if random.random() <= (1 - self.getMutProb()):
                    offSpringResistances[drug] = self.resistances[drug]
                else:
                    offSpringResistances[drug] = not self.resistances[drug]

            if random.random() <= self.getMaxBirthProb() * (1 - popDensity):
                return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(), offSpringResistances,
                                      self.getMutProb())
            else:
                raise NoChildException
        else:
            raise NoChildException


class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        Patient.__init__(self,viruses, maxPop)
        # a that will contain strings of drug names the patient has been prescribed
        self.prescriptions = []

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """

        # appends newDrug to prescriptions property ( a list of strings)
        if newDrug in self.prescriptions:
            pass
        else:
            self.prescriptions.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        # could return an empty list if no prescriptions have been added
        return self.prescriptions

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """

        resistantPopulation = 0

        for virion in self.viruses:
            resistant = True
            for drug in drugResist:
                resistant = resistant and virion.isResistantTo(drug)
            if resistant:
                resistantPopulation += 1

        return resistantPopulation

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        for virion in list(self.viruses):
            if virion.doesClear():
                self.viruses.remove(virion)

        currentPopDensity = self.getTotalPop() / float(self.getMaxPop())
        # print("current population ", self.getTotalPop())
        # print("current population density ", currentPopDensity)

        replicants = []

        for virus in self.viruses:
            try:
                resistant = True
                for drug in self.getPrescriptions():
                    resistant = resistant and virus.isResistantTo(drug)
                if resistant:
                    tempVirus = virus.reproduce(currentPopDensity, self.getPrescriptions())
                    if tempVirus:
                        replicants.append(tempVirus)
            except NoChildException:
                pass

        for newVirus in replicants:
            self.viruses.append(newVirus)

        return self.getTotalPop()
#
# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    # array holding numTrial patients, 1 for every trial
    patients = []

    numTimeSteps = 150
    timeSteps = list(range(numTimeSteps))  # list containing 1...300 time steps

    # initializes viralPop count with initial zeroes ( creating a list of 0's of length numTimeSteps
    viralPop = [0]*numTimeSteps
    resistantViralPop = [0]*numTimeSteps # population count of viruses that are resistant to antibiotic

    # list initially containing zeroes will eventually be the average of numTrial patients' viral populations at time step 1...300

    for trial in range(numTrials):
        # create the initial virus population of length numViruses
        initialVirusPop = []
        for virus in range(numViruses):
            initialVirusPop.append(ResistantVirus(maxBirthProb, clearProb,resistances,mutProb))

        patients.append(TreatedPatient(initialVirusPop, maxPop))

        for time_step in range(numTimeSteps):
            if time_step == 0:
                for patient in patients:
                    patient.addPrescription('guttagonol')

            patients[trial].update()  # update the patient at current trail: 1...numTrials

            # add the current viral population to the corresponding time step
            viralPop[time_step] += float(patients[trial].getTotalPop())
            resistantViralPop[time_step] += float(patients[trial].getResistPop(['guttagonol']))

    # averageViralPop = [x/numTimeSteps for x in viralPop]
    # the average should be every item in viralPop divided by the trial number i.e. number of patients
    pylab.plot(timeSteps, viralPop)
    pylab.plot(timeSteps, resistantViralPop)
    pylab.title('Average viral population of ' + str(numTrials) + ' patients with 300 time steps each')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Viral Population')
    pylab.legend(('Total', 'R'))
    pylab.show()