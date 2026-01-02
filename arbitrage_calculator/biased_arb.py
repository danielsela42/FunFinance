import numpy as np
from arbitrage_calculator.argument_inputs import get_inputs_manual


def determine_arbitrage():
    ''' Determine if a biased arbitrage opportunity exists between two bookmakers' odds for two bets.
        If so, calculate the stakes to place on each bet to guarantee a profit.
    '''
    # Get two bookmakers' odds and stake amount from user
    odds_1, odds_2, stake = get_inputs_manual()
    assert(len(odds_1) == len(odds_2) == 2), "This function only supports two bets for biased arbitrage."

    # Biased towards first bet
    max_odds2 = np.max(odds_2, dtype=float)
    if max_odds2 <= 1:
        bias_1 = False
    else:
        bias_1 = True
        stake1_bias1 = (1 - max_odds2) * stake
        stake2_bias1 = max_odds2 * stake

    # Biased towards second bet
    max_odds1 = np.max(odds_1, dtype=float)
    if max_odds1 <= 1:
        bias_2 = False
    else:
        bias_2 = True
        stake1_bias2 = (1 - max_odds1) * stake
        stake2_bias2 = max_odds1 * stake

    if not bias_1 and not bias_2:
        print("No biased arbitrage opportunity available.")
    elif bias_1:
        print("Biased arbitrage opportunity detected towards bet 1!")
        returns = stake2_bias1 * max_odds2
        profit = returns - stake

        print(f"Stake on bookmaker 1 (bet 1): {stake1_bias1:.2f}")
        print(f"Stake on bookmaker 2 (bet 2): {stake2_bias1:.2f}")
        print(f"Guaranteed return: {returns:.2f}")
        print(f"Guaranteed profit: {profit:.2f}")
    else:  # bias_2
        print("Biased arbitrage opportunity detected towards bet 2!")
        returns = stake1_bias2 * max_odds1
        profit = returns - stake

        print(f"Stake on bookmaker 1 (bet 1): {stake1_bias2:.2f}")
        print(f"Stake on bookmaker 2 (bet 2): {stake2_bias2:.2f}")
        print(f"Guaranteed return: {returns:.2f}")
        print(f"Guaranteed profit: {profit:.2f}")

    return