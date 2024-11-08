# Proyect Game Theory
# Board Game: Love Letter
# Main file
# Andres Restrepo, Camila Barrera y Santiago

from love_letter_game import Player, initialize_deck, shuffle_deck, game_flow
if __name__ == "__main__":
    deck, discard_pile = initialize_deck()
    shuffle_deck(deck)
    
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Play one round of the game
    print(f"\nStarting a new round! Current scores:")
    print(f"{player1.name}: {player1.victory_points} points")
    print(f"{player2.name}: {player2.victory_points} points")
    
    game_flow(player1, player2, deck, discard_pile)

    # Print the results of the single round
    print("\nGame Over!")
    if player1.victory_points > player2.victory_points:
        print(f"{player1.name} wins the game with {player1.victory_points} points!")
    elif player2.victory_points > player1.victory_points:
        print(f"{player2.name} wins the game with {player2.victory_points} points!")
    else:
        print("It's a tie!")
