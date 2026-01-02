def get_inputs_manual():
    ''' Collects user inputs for number of bets, stake amount, and odds from two bookmakers.
    '''
    num_bets = input("How many bets are available? ")
    stake = input("What are you staking? ")

    odds_1 = list()
    odds_2 = list()
    for i in range(num_bets):
        odd_1 = input(f"Odds for bet \# {i + 1} with bookmaker 1: ")
        odd_2 = input(f"Odds for bet \# {i + 1} with bookmaker 2: ")
        odds_1.append(odd_1)
        odds_2.append(odd_2)

    return odds_1, odds_2, stake