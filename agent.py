import random as random 
import pickle

class Agent:

    def __init__(self):
        self.qTable = {}

        self.alpha = 0.1
        self.gamma = 0.99

        self.epsilon = 1
        self.minEpislon = 0.05
        self.decayEpsilon = 0.99999


    def getQValues(self, state):

        if state not in self.qTable:
            self.qTable[state] = [0.0, 0.0, 0.0]

        return self.qTable[state]


    def chooseAction(self, state):
        qValues = self.getQValues(state)

        if random.random() < self.epsilon:
            return random.randrange(len(qValues))

        return int(qValues.index(max(qValues)))
        


    def learn(self, state, action, reward, nextState, done):

        qValues = self.getQValues(state)

        if done:
            target = reward

        else:
            nesteQ = max(self.getQValues(nextState))

            target = reward + nesteQ * self.gamma

        qValues[action] += self.alpha * (target - qValues[action])


        


    def epsilonDecay(self):
        if self.epsilon > self.minEpislon:
            self.epsilon = self.epsilon * self.decayEpsilon

    def saveModel(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.qTable, f)

    def loadModel(self, filename):
        with open(filename, "rb") as f:
            self.qTable = pickle.load(f)
        
    