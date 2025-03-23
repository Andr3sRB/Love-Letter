# Love Letter: Game Simulation

This project implements a simplified computational version of the popular card game **Love Letter**, using **Python**. The simulation models the game's mechanics, allowing players to experience the strategic depth of Love Letter without needing the physical game.

## Author
**Andrés Restrepo Botero**  
**Universidad EAFIT**  
**Mathematical Engineering**  

## Features
- **Full Game Simulation**: Simulates the core mechanics of Love Letter, including drawing, playing, and discarding cards.
- **Simplified Rules**: Adjustments made for computational simplicity:
  - The **Prince** only targets the opponent.
  - The **Spy** grants points only when played, not discarded.
  - The initial card discard rule has been removed.
- **Two Players**: The game is set up for two players, with rounds continuing until a winner is declared.

## Structure
- **love_letter_game.py**: Contains all the game logic, including player classes, card actions, and game flow.
- **main.py**: Runs a single round of the game and tracks scores.

## How to Run
1. Ensure you have the latest version of **Python** installed.
2. Run `main.py` to simulate a single round:
   ```bash
   python main.py

Example Output: 

Starting a new round! Current scores:
Player 1: 0 points
Player 2: 0 points

Player 1 draws their initial card.
Player 2 draws their initial card.
Player 1 goes first!

Player 1's turn.
Current Deck: [1, 2, 5, 7, ...]
Player 1 plays Handmaid (4).

Player 2's turn.
Player 2 plays Guard (1), guesses Princess.





[Online toolbox user guide example](./UserGuide_ABM-EpiVector.html)

