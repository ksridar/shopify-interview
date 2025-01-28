### Holiday Gift Exchange
# Input: list of people, list of partners / relationships
# A, B, C
# Output: {"A" : "B", [B, C], [C, A]}

# Constraint: Partners cannot give gifts to each other

import random


class GiftExchange:

    def __init__(self):
        self.participants = []
        self.relationships = {}
    
    def add_participant(self, name, partner):
        self.participants.append(name)
        self.participants.append(partner)
        self.relationships[name] = partner
        self.relationships[partner] = name
    
    def draw_names(self):
        output = {}
        available_participants = self.participants.copy()
        random.shuffle(available_participants)

        for p in self.participants:
            resulting_partner = None
            for a in available_participants:
                  if a != p and self.relationships[p] != a:
                      resulting_partner = a
                      available_participants.remove(a)
            
            if resulting_partner:
                output[p] = resulting_partner
            else:
                 print("No match found")
                 self.draw_names()
        
        return output
            

def testBasic():
    game = GiftExchange()
    game.add_participant("A", "B")
    print(game.participants)
    print(game.relationships)

def testDraw():
    game = GiftExchange()
    game.add_participant("A", "B")
    game.add_participant("C", "D")
    output = game.draw_names()
    print(output)


def main():
    testDraw()




if __name__ == "__main__":
        main()