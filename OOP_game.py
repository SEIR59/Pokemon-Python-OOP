from data import pokeData 
import random

class Player:

    def __init__(self, deck, name):
        self.deck = deck[:]
        self.name = name
        self.played = []
        self.hand = []
        self.points = 0
        self.wins = 0
        self.playable = True
    
    def draw_cards(self):
        for i in range(3):
            self.hand.append(self.deck.pop(random.randint(0,len(self.deck)-1)))
        pass

    def select_card(self,rand):

        if rand:
            return self.play_card(random.randint(0,len(self.hand)-1))

        else:
            p_sel = 'Invalid'
            while isinstance(p_sel, int) == False: 

                [print(f"{idx+1} : {card}") for idx, card in enumerate(self.hand)]
                p_sel = input("Please select your card by typing which number you want to pick. Or 'quit' to exit.")

                if p_sel == 'quit':
                    return False

                else:

                    try:
                        p_sel = int(p_sel)
                        if p_sel < 1:
                            p_sel = 'Invalid'
                        #This print throws an error if selection outside of hand range
                        print(f"Your choice was {self.hand[p_sel-1]}.")
                        return self.play_card(p_sel-1)
                    except:
                        p_sel = 'Invalid selection.'
                        print(p_sel)

    def play_card(self, idx):
        self.played.append(self.hand.pop(idx))
        return self.played[-1]

    def win_round(self):
        print(f"I, {self.name}, am the GREATEST POKEMON DUELIST OF ALLL TIME.")

class Game:

    def __init__(self , deck ):
        self.p = Player(deck, input('Please type your name here: '))
        self.c = Player(deck, 'Hyperadvanced intergalatic pokemon duelist AI')
        self.round = 1
        self.p.draw_cards()
        self.c.draw_cards()
        self.wait()
    
    def wait(self):
        helpPlayer = """Type a command: 
            'hand' to view your available cards,
            'play' to play a card against the computer,
            'deck' to view your remaining deck, 
            'played' to view your played cards,
            'points' to view the score for this round,
            'score' to view the number of rounds won,
            or add 'computer' before or after any of the commands above to view the computer's versions of that command."""

        while self.p.playable or self.p.hand:

            inp = input(f"Type 'help' to review available commands. or 'quit' to exist the game.")

            if inp == 'help':
                print(helpPlayer)
            elif inp == 'quit':
                break
            elif 'computer' in inp:
                if 'hand' in inp:
                    print(self.c.hand)
                elif 'deck' in inp:
                    print(self.c.deck)
                elif 'played' in inp:
                    print(self.c.played)
                elif 'points' in inp:
                    print(f"Player: {self.p.points} | Computer: {self.c.points}")
                elif 'score' in inp:
                    print(f"Player: {self.p.wins} | Computer: {self.c.wins}")
            else:
                if 'hand' in inp:
                    print(self.p.hand)
                elif 'played' in inp:
                    print(self.p.played)
                elif 'play' in inp:
                    self.game_round()
                elif 'deck' in inp:
                    print(self.p.deck)
                elif 'points' in inp:
                    print(f"Points this round: Player: {self.p.points} | Computer: {self.c.points}")
                elif 'score' in inp:
                    print(f"Round wins: Player: {self.p.wins} | Computer: {self.c.wins}")
    
    def game_round(self):

        result = self.compare_cards( self.p.select_card(False), self.c.select_card(True)) 
        if result == 1:
            self.p.points += 1
            print(f"'You really decided to play THAT?!?!' -Hyperadvanced intergalatic pokemon duelist AIactic AI")
        elif result == 2:
            print(f"'Calculated. Alllll calculated... I've seen all 45,296,713 variations. You stand no chance' -Hyperadvanced intergalatic pokemon duelist AIactic AI")
            self.c.points += 1
        
        if not self.p.hand:
            winner = 'Nobody, tie game.'
            if self.p.points > self.c.points:
                winner = self.p.name
                self.p.win_round()
                self.p.wins += 1
            elif self.c.points > self.p.points:
                winner = self.c.name
                self.c.win_round()
                self.c.wins += 1

            self.p.points = 0
            self.c.points = 0

            print(f"ROUND {self.round} complete. Winner is... {winner}")
            self.round += 1

            if not self.p.playable:
                self.end_game()
            else:
                self.p.draw_cards()
                self.c.draw_cards()
                if len(self.p.deck) < 3:
                    self.p.playable = False
        else:
            self.wait()

    def compare_cards(self , c1 , c2 ):
        #print(f'comparing {c1} and {c2}')
        if c1['damage'] > c2['damage']:
            print(f"Player wins this round! {c1} vs {c2}.")
            return 1
        elif c1['damage'] == c2['damage']:
            print(f"Tie this round! {c1} vs {c2}.")
            return 0
        else:
            print(f"Computer wins this round! {c1} vs {c2}.")
            return 2

    def end_game(self):

        if self.p.wins > self.c.wins:
            print(f"AAAAAAAAAND THE WINNER OF THIS MAGNIFICENT POKEMON DUEL ISSSSSSSSSSSS.......................... {self.p.name.upper()}, WITH A SCORE OF {self.p.wins} AGAINST {self.c.name.upper()}'S {self.c.wins}!")
            print(f"'I must be having bugs from all the space travel. Or maybe you cheated. Either way, not a loss for me.' -Hyperadvanced intergalatic pokemon duelist AI")

        elif self.c.wins > self.p.wins:
            print(f"AAAAAAAAAND THE WINNER OF THIS MAGNIFICENT POKEMON DUEL ISSSSSSSSSSSS.......................... {self.c.name.upper()}, WITH A SCORE OF {self.c.wins} AGAINST {self.p.name.upper()}'S {self.p.wins}!")
            print(f"'HAHAHA YOU LOSE! PATHETIC HUMAN YOU STOOD NO CHANCE AT ALL!' -Hyperadvanced intergalatic pokemon duelist AI")
            
        else:
            print(f"AAAAAAAAAND THE WINNER OF THIS MAGNIFICENT POKEMON DUEL ISSSSSSSSSSSS.......................... Nobody. It's a tie.")

game = Game(pokeData)