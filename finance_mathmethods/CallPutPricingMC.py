import numpy as np
from scipy.stats import norm


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
    rt = (mu - 0.5 * sigma**2) * dt + zt * sigma * np.sqrt(dt)

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
    for _ in range(Np):
        S = MC_path(Nt, mu, sigma, S0, dt)
        terminals.append(S[-1])

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
        
    return np.mean(returns_to_origins)


def MC_calls(K, Np, Nt, r, sigma, S0, dt):
    ''' Monte Carlo simulation to estimate European call option price
    
    Inputs: K - strike price
            Np - number of simulated paths
            Nt - number of time steps
            r - risk-free interest rate
            sigma - volatility
            S0 - initial stock price
            dt - time step size
    '''
    Cs = list()
    for _ in range(Np):
        S = MC_path(Nt, r, sigma, S0, dt)
        Cs.append(np.max([S[-1] - K, 0]))

    T = Nt * dt
    discount = np.exp(-r * T)
    discounted_payoffs = discount * np.array(Cs)

    standard_error = np.std(discounted_payoffs, ddof=1) / np.sqrt(Np)
        
    return np.mean(discounted_payoffs), standard_error

def MC_puts(K, Np, Nt, r, sigma, S0, dt):
    ''' Monte Carlo simulation to estimate European put option price
    
    Inputs: K - strike price
            Np - number of simulated paths
            Nt - number of time steps
            r - risk-free interest rate
            sigma - volatility
            S0 - initial stock price
            dt - time step size
    '''
    Ps = list()
    for _ in range(Np):
        S = MC_path(Nt, r, sigma, S0, dt)
        Ps.append(np.max([K - S[-1], 0]))

    T = Nt * dt
    discount = np.exp(-r * T)
    discounted_payoffs = discount * np.array(Ps)

    standard_error = np.std(discounted_payoffs, ddof=1) / np.sqrt(Np)
        
    return np.mean(discounted_payoffs), standard_error

def black_scholes_call(S0, K, T, r, sigma):
    ''' Black-Scholes formula for European call option price

    Inputs: S0 - initial stock price
            K - strike price
            T - time to maturity (in years)
            r - risk-free interest rate
            sigma - volatility
    '''
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    call_price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

def black_scholes_put(S0, K, T, r, sigma):
    ''' Black-Scholes formula for European put option price

    Inputs: S0 - initial stock price
            K - strike price
            T - time to maturity (in years)
            r - risk-free interest rate
            sigma - volatility
    '''
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    return put_price

if __name__=="__main__":
    Np = 100000
    Nt = 252

    sigma = 0.4
    S0 = 100
    dt = 1/Nt
    r = 0.05

    K = 100

    price, se = MC_puts(K, Np, Nt, r, sigma, S0, dt)
    print("Expected put price:", price)
    print("Confidence interval (95%):", f"[{price - 1.96 * se:.2f}", f"{price + 1.96 * se:.2f}]")
    print("Black-Scholes put price:", black_scholes_put(S0, K, Nt * dt, r, sigma))

    price, se = MC_calls(K, Np, Nt, r, sigma, S0, dt)
    print("Expected call price:", price)
    print("Confidence interval (95%):", f"[{price - 1.96 * se:.2f}", f"{price + 1.96 * se:.2f}]")
    print("Black-Scholes call price:", black_scholes_call(S0, K, Nt * dt, r, sigma))