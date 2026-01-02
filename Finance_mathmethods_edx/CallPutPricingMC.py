import numpy as np
from matplotlib import pyplot as plt

def MC_path(Nt, mu, sigma, S0, dt):
    ''' Monte Carlo simulation of a single stock price path over Nt time steps

    Inputs: Nt - number of time steps
            mu - expected return
            sigma - volatility
            S0 - initial stock price
            dt - time step size
    '''

    # Generate random returns
    zt = 2 * np.random.randint(2, size=Nt) - 1
    rt = mu * dt + zt * sigma * np.sqrt(dt)

    # Use log pricing
    logS = [np.log(S0)]
    for j in range(Nt):
        logS.append(rt[j] + logS[-1])
    
    return np.exp(np.array(logS))


def MC_terminal_mean_std(Np, Nt, mu, sigma, S0, dt):
    ''' Monte Carlo simulation to estimate mean and standard deviation of terminal stock price

    Inputs: Np - number of simulated paths
            Nt - number of time steps
            mu - expected return
            sigma - volatility
            S0 - initial stock price
            dt - time step size
    '''
    terminals = list()
    # plt.figure()
    for _ in range(Np):
        S = MC_path(Nt, mu, sigma, S0, dt)
        # plt.plot(S)
        terminals.append(S[-1])

    # plt.show()
    
    return np.mean(terminals), np.std(terminals, ddof=1)

def MC_mean_orig_returns(Np, Nt, mu, sigma, S0, dt):
    ''' Monte Carlo simulation to estimate mean number of returns to origin

    Inputs: Np - number of simulated paths
            Nt - number of time steps
            mu - expected return
            sigma - volatility
            S0 - initial stock price
            dt - time step size
    '''
    returns_to_origins = list()
    for _ in range(Np):
        S = MC_path(Nt, mu, sigma, S0, dt)
        count = 0
        for t in range(1, Nt):
            if S[t] == S0 or (S[t-1] < S0 and S[t] > S0) or (S[t - 1] > S0 and S[t] < S0):
                count += 1
        returns_to_origins.append(count)
        
    # print(returns_to_origins)
    return np.mean(returns_to_origins)


def MC_calls(K, Np, Nt, mu, sigma, S0, dt):
    ''' Monte Carlo simulation to estimate European call option price
    
    Inputs: K - strike price
            Np - number of simulated paths
            Nt - number of time steps
            mu - expected return
            sigma - volatility
            S0 - initial stock price
            dt - time step size
    '''
    Cs = list()
    for _ in range(Np):
        S = MC_path(Nt, mu, sigma, S0, dt)
        Cs.append(np.max([S[-1] - K, 0]))
        
    return np.mean(Cs)

def MC_puts(K, Np, Nt, mu, sigma, S0, dt):
    ''' Monte Carlo simulation to estimate European put option price
    
    Inputs: K - strike price
            Np - number of simulated paths
            Nt - number of time steps
            mu - expected return
            sigma - volatility
            S0 - initial stock price
            dt - time step size
    '''
    Ps = list()
    for _ in range(Np):
        S = MC_path(Nt, mu, sigma, S0, dt)
        Ps.append(np.max([K - S[-1], 0]))
        
    return np.mean(Ps)

if __name__=="__main__":
    Np = 10000
    Nt = 252
    mu = 0.06
    sigma = 0.4
    S0 = 100
    dt = 1/252

    K = 100

    print(MC_puts(K, Np, Nt, mu, sigma, S0, dt))
        