import numpy as np
from arbitrage_calculator.argument_inputs import get_inputs_manual


def determine_arbitrage():
    ''' Determine if an arbitrage opportunity exists between two bookmakers' odds for two bets.
        If so, calculate the stakes to place on each bet to guarantee a profit.
    '''
    # Get two bookmakers' odds and stake amount from user
    odds_1, odds_2, stake = get_inputs_manual()

    # Initialize odds matrix and calculate implied probabilities
    odds_matrix = np.array([odds_1, odds_2], dtype=float)
    max_odds = np.max(odds_matrix, axis=1) # Minimize implied probability by taking max odds
    pI = np.sum(1 / max_odds)
    
    if pI > 1:
        print("No arbitrage opportunity available.")
    else:
        print("Arbitrage opportunity detected!")
        stakes = (stake / max_odds) / pI
        returns = stakes * max_odds
        profit = returns[0] - stake  # Since returns are the same for both bets

        print(f"Stake on bookmaker 1: {stakes[0]:.2f}")
        print(f"Stake on bookmaker 2: {stakes[1]:.2f}")
        print(f"Guaranteed return: {returns[0]:.2f}")
        print(f"Guaranteed profit: {profit:.2f}")
    return
