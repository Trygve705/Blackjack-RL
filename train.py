from blackjackGame import blackjack
from agent import Agent

modell = Agent()
modell.loadModel("tabell.pkl")
antall = 100000000

for runder in range(antall):
    game = blackjack()


    while not game.done:

        state = (sum(game.spiller), sum(game.dealer), game.soft, game.dealerSoft)

        action = modell.chooseAction(state)
       

        reward, spillerSum, dealerSum, spillerSoft, dealerSoft, done =  game.step(action)

        nextState = (spillerSum, dealerSum, spillerSoft, dealerSoft)

        modell.learn(state, action, reward, nextState, done)

    modell.epsilonDecay()

    

modell.saveModel("tabell.pkl")

