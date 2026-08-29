import numpy as np
import random as random



class blackjack:

    def __init__(self):
        self.kortstokk = [
            2, 2, 2, 2,
            3, 3, 3, 3,
            4, 4, 4, 4,
            5, 5, 5, 5,
            6, 6, 6, 6,
            7, 7, 7, 7,
            8, 8, 8, 8,
            9, 9, 9, 9,
            10, 10, 10, 10,  
            10, 10, 10, 10,  
            10, 10, 10, 10,  
            10, 10, 10, 10,  
            11, 11, 11, 11    
            ]
        
        self.dealer = []
        self.spiller = []
        self.spillerFerdig = False
        self.soft = False
        self.done = False
        self.dobble = False
        self.dealerSoft = False
        
        random.shuffle(self.kortstokk)
        self.spiller.append(self.kortstokk.pop())
        self.spiller.append(self.kortstokk.pop())
        self.dealer.append(self.kortstokk.pop())

        if self.spiller.count(11) >= 1:
            self.soft = True
        if sum(self.spiller) == 22:
            self.handtereSoft()

        if sum(self.dealer) == 22:
            self.dealer[0] = 1
        if sum(self.spiller) == 21:
            self.spillerFerdig = True

        

    def handtereSoft(self):
        if self.soft and sum(self.spiller) > 21:
            self.spiller[self.spiller.index(11)] = 1
        if self.spiller.count(11) >= 1:
            self.soft = True
        else:
            self.soft = False

    def step(self, action):

        # stand 
        if action == 0:
            self.spillerFerdig = True

        # Hit
        if action == 1:
            self.spiller.append(self.kortstokk.pop())
            if self.spiller.count(11) >= 1:
                self.soft = True

            if sum(self.spiller) > 21:
                if not self.soft:
                    reward = -1
                    self.done = True
                    return reward, sum(self.spiller), sum(self.dealer), self.soft, self.dealerSoft, self.done 
                else:
                    self.handtereSoft()
                    reward = 0 
                    return reward, sum(self.spiller), sum(self.dealer), self.soft, self.dealerSoft, self.done 
            
            if sum(self.spiller) == 21:
                self.spillerFerdig = True

            else:
                reward = 0
                return reward, sum(self.spiller), sum(self.dealer), self.soft, self.dealerSoft, self.done

        # double
        if action == 2:
            self.dobble = True
            self.spiller.append(self.kortstokk.pop())
            if self.spiller.count(11) >= 1:
                self.soft = True

            if self.soft and sum(self.spiller) > 21:
                self.handtereSoft()
                self.spillerFerdig = True

            elif sum(self.spiller) > 21:
                reward = -2
                self.done = True
                return reward, sum(self.spiller), sum(self.dealer), self.soft, self.dealerSoft, self.done
            else:
                self.spillerFerdig = True




        # Dealer
        if self.spillerFerdig:
            while sum(self.dealer) <= 16:
                self.dealer.append(self.kortstokk.pop())
                if self.dealer.count(11) >= 1:
                    self.dealerSoft = True
                if sum(self.dealer) > 21 and self.dealerSoft:
                    self.dealer[self.dealer.index(11)] = 1
                    if self.dealer.count(11) >= 1:
                        self.dealerSoft = True
                    else:
                        self.dealerSoft = False

            
            self.done = True
            
            if self.dobble:
                if sum(self.dealer) > 21:
                    reward = 2
                elif sum(self.dealer) > sum(self.spiller):
                    reward = -2
                elif sum(self.dealer) < sum(self.spiller):
                    reward = 2
                elif sum(self.dealer) == sum(self.spiller):
                    reward = 0
            else:
                if sum(self.dealer) > 21:
                    reward = 1
                elif sum(self.dealer) > sum(self.spiller):
                    reward = -1
                elif sum(self.dealer) < sum(self.spiller):
                    reward = 1
                elif sum(self.dealer) == sum(self.spiller):
                    reward = 0

            return reward, sum(self.spiller), sum(self.dealer), self.soft, self.dealerSoft, self.done 

                
                    



            
        




    



    





