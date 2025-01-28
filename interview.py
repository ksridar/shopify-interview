### Holiday Gift Exchange
# Input: list of people, list of partners / relationships
# A, B, C
# Output: [A, B], [B, C], [C, A]

# Constraint: Partners cannot give gifts to each other

class GiftExchange:

    def __init__(self):
        self.participants = []
        self.relationships = {}
    
    def add_participant(self, name, partner):
        self.participants.append(name)
        self.participants.append(partner)
        self.relationships[name] = partner
        self.relationships[partner] = name
    
    




def testBasic():
    game = GiftExchange()
    game.add_participant("A", "B")
    print(game.participants)
    print(game.relationships)



def main():
    testBasic()



if __name__ == "__main__":
        main()