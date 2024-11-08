# Proyect Game Theory
# Board Game: Love Letter
# Funtions file
# Andres Restrepo, Camila Barrera y Santiago

# Imports
import random 

# Initialize Deck
def initialize_deck():
    deck = [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9]
    discard_pile = []
    return deck,discard_pile

# Shuffle deck
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def reset_handmaid(player):
    player.handmaid = 0


# Initialize players
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = [-1, -1]  
        self.spy_played = 0
        self.handmaid = 0
        self.eliminated = False  
        self.victory_points = 0  

    def player_eliminated(player):
        return player.eliminated

    def assign_card(self, index, value):
        # Check index within the valid range
        if index in [0, 1]:
            self.cards[index] = value
        else:
            print("Invalid card given, Please choose 0 or 1.")
            
    def draw_card(self, deck):
        if len(deck) == 0:
            print("The deck is empty. Cannot draw a card.")
            return
        drawn_card = deck.pop(0)  
        self.assign_card(0,drawn_card)  

    def initial_draw(self, deck):
        if len(deck) == 0:
            print("The deck is empty. Cannot draw a card.")
            return
        drawn_card = deck.pop(0)  
        self.assign_card(1,drawn_card) 

    def discard_card(self, played_card, discard_pile):
        if played_card == 9:
            print(f"The Princess has been played! {self.name} is eliminated.")
            self.eliminated = True
        elif self.cards[0] == played_card:
            discard_pile.append(played_card)
            self.cards[0] = 0
        elif self.cards[1] == played_card:
            discard_pile.append(played_card)
            self.cards[1] = 0
            self.cards[0], self.cards[1] = self.cards[1], self.cards[0]


    def play_card(self, index, opponent, deck, discard_pile):
    # Check index within the valid range
        if index not in [0, 1]:
            print("Invalid index. Please choose 0 or 1.")
            return

        # Check for Countess restriction
        if 8 in self.cards and (5 in self.cards or 7 in self.cards):
            countess_index = self.cards.index(8)
            print(f"Countess restriction: {self.name} must play the Countess (8) because of Prince (5) or King (7) in hand.")
            index = countess_index 

        card_value = self.cards[index]
        if index == 1:
            self.cards[0], self.cards[1] = self.cards[1], self.cards[0]
        self.discard_card(card_value, discard_pile)  

        # Actions based on the card value

        # Spy 
        if card_value == 0:  
            if self.spy_played == 0:  
                self.spy_played = 1   
            print(f"{self.name} played the spy card")
            return
        
        # Guard
        if card_value == 1: 
            if opponent.handmaid == 0:
                guess = int(input(f"{self.name}, guess the opponent's card (2-9): "))
                if guess == opponent.cards[1]:
                    print(f"Correct! {self.name} eliminates {opponent.name}.")
                    opponent.eliminated = True
                else:
                    print(f"Wrong guess! {opponent.name} stays in the game.")
            else:
                print(f"{opponent.name} is protected by the Handmaid.")

        # Priest
        elif card_value == 2: 
            if opponent.handmaid == 0:
                print(f"{self.name} played the priest card and sees {opponent.name}'s card: {opponent.cards[1]}")
            else : 
                print(f"{opponent.name} is protected by the Handmaid, no effect takes place.")
            
        # Baron
        elif card_value == 3:  
            if opponent.handmaid == 0:
                if self.cards[1] > opponent.cards[1]:
                    print(f"{self.name} wins the comparison! {opponent.name} is eliminated.")
                    opponent.eliminated = True
                elif self.cards[1] < opponent.cards[1]:
                    print(f"{opponent.name} wins the comparison! {self.name} is eliminated.")
                    self.eliminated = True
                else:
                    print("It's a tie! No one is eliminated.")
                    
            else:
                print(f"{opponent.name} is protected by the Handmaid.")

        # Handmaid
        elif card_value == 4:
            self.handmaid = 1
            print(f"{self.name} played the handmaid card. They are now protected from effects until the next turn.")
            
        # Prince
        elif card_value == 5:  
            if opponent.handmaid == 0:
                discarded_card = opponent.cards[1]
                discard_pile.append(discarded_card)
                print(f"{opponent.name} discards their card {discarded_card}.")
                if discarded_card == 9:  # Princess discarded
                    print(f"{opponent.name} discarded the Princess and is eliminated.")
                    opponent.eliminated = True
                else:
                    opponent.draw_card(deck)
            else:
                print(f"{opponent.name} is protected by the Handmaid.")

        # Chancellor
        elif card_value == 6:
            if  len(deck) < 2:
                print("Not enough cards in the deck to draw two cards.")   
            else:
                # Draw two cards from the deck
                drawn_cards = [deck.pop(0), deck.pop(0)]
                # Show options
                print(f"{self.name}, you drew the following cards: {drawn_cards}")
                print(f"Your current card is: {self.cards[1]}")
                
                # Cards to choose from
                options = drawn_cards + [self.cards[1]]
                print("Your choices are:", options)
                
                # Choose one of the three cards
                choice = int(input("Choose one of the cards (enter 0, 1, or 2): "))

                while choice not in [0, 1, 2]:
                    choice = int(input("Invalid choice. Please enter 0, 1, or 2: "))
                
                # Update player's second card 
                self.cards[1] = options[choice]
            
                # Place the unselected cards back to the bottom of the deck
                unselected_cards = [card for i, card in enumerate(options) if i != choice]
                deck.extend(unselected_cards)

        # King
        elif card_value == 7:  
            if opponent.handmaid == 0:
                print(f"{self.name} swaps their hand with {opponent.name}.")
                self.cards[1], opponent.cards[1] = opponent.cards[1], self.cards[1]
                print(f"After swapping, {self.name}'s hand: {self.cards}")
                print(f"After swapping, {opponent.name}'s hand: {opponent.cards}")
            else:
                print(f"{opponent.name} is protected by the Handmaid. The King has no effect.")
            
        # Countess
        elif card_value == 8:
            return
        # Princess
        elif card_value == 9:  
            print(f"{self.name} played the Princess and is eliminated.")
            self.eliminated = True
        else:
            print("Invalid card value.")

      



def game_flow(player1, player2, deck, discard_pile):
    # Each player draws an initial card to start with
    print(f"{player1.name} draws their initial card.")
    player1.initial_draw(deck)
    print(f"{player1.name}'s current hand: {player1.cards}")
    
    print(f"{player2.name} draws their initial card.")
    player2.initial_draw(deck)
    print(f"{player2.name}'s current hand: {player2.cards}")

    # Randomly decide who goes first
    current_player = player1 if random.choice([0, 1]) == 0 else player2
    opponent = player2 if current_player == player1 else player1
    print(f"{current_player.name} goes first!")

    # Game loop for a single round
    while deck and not player1.eliminated and not player2.eliminated:
        print(f"\nCurrent Deck: {deck}")
        print(f"\n{current_player.name}'s turn.")
        
        # Reset handmaid protection at the start of the turn
        reset_handmaid(current_player)
        
        # Current player draws a card at the start of their turn
        current_player.draw_card(deck)
        print(f"{current_player.name}'s current hand after drawing: {current_player.cards}")
        
        # Player chooses which card to play
        while True:
            try:
                card_to_play = int(input(f"{current_player.name}, choose a card to play (0 for {current_player.cards[0]}, 1 for {current_player.cards[1]}): "))
                if card_to_play in [0, 1]:
                    break
                else:
                    print("Invalid choice. Please choose 0 or 1.")
            except ValueError:
                print("Invalid input. Please enter 0 or 1.")
        
        current_player.play_card(card_to_play, opponent, deck, discard_pile)

        # Check if opponent is eliminated
        if opponent.eliminated:
            print(f"{current_player.name} wins this round!")
            current_player.victory_points += 1
            break  # End round

        # Swap turns
        current_player, opponent = opponent, current_player

    # Decide the winner by highest card if deck runs out
    if not player1.eliminated and not player2.eliminated:
        print("Deck is empty! Deciding winner by card values.")
        if player1.cards[1] > player2.cards[1]:
            print(f"{player1.name} wins with a higher card!")
            player1.victory_points += 1
        elif player2.cards[1] > player1.cards[1]:
            print(f"{player2.name} wins with a higher card!")
            player2.victory_points += 1
        else:
            print("It's a tie!")

    # Spy bonus points
    if player1.spy_played == 1 and player2.spy_played == 0:
        print(f"{player1.name} earns a Spy bonus point!")
        player1.victory_points += 1
    elif player2.spy_played == 1 and player1.spy_played == 0:
        print(f"{player2.name} earns a Spy bonus point!")
        player2.victory_points += 1

    # Reset spy for the next round
    player1.spy_played = 0
    player2.spy_played = 0

    # Print Victory points
    print(f"\nVictory Points:")
    print(f"{player1.name}: {player1.victory_points}")
    print(f"{player2.name}: {player2.victory_points}")

