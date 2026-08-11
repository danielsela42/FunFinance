# Call & Put Option Pricing via Monte Carlo Simulation

This script implements a **Monte Carlo simulation** of stock price dynamics and uses it to estimate the prices of **European call and put options**. It also includes routines for analyzing basic statistical properties of simulated price paths.

The code is intended as **educational and exploratory work**, demonstrating how option pricing and path statistics can be estimated numerically from stochastic models.

---

## Model Overview

The stock price $` S_t `$ is modeled using a binomial approximation of **geometric Brownian motion**. For a stock with expected return $`\mu`$ and volatility $`\sigma`$, we have

```math
d \log S_t = \left( \mu - \frac{1}{2}\sigma^2 \right) d t + \sigma \, d W_t.
```

The Brownian motion increment can be approximated using a symmetric binomial random variable:
```math
z_t = \begin{cases}
+1 & \text{with probability } 1/2, \\
-1 & \text{with probability } 1/2
\end{cases}
```
so that
```math
d W_t \approx \sqrt{d t}\, z_t
```

Hence, in discrete-time, we have

```math
\log S_{t+ \Delta t} = \log S_t + \left( \mu - \frac{1}{2}\sigma^2 \right) \Delta t + \sigma \sqrt{\Delta t}, z_t
```

---

## Risk-Neutral Pricing

European option prices are calculated using **risk-neutral pricing**. Under the risk-netural measure, the drift is equal to the risk-free interest rate $`r`$. Therefore, the Monte Carlo paths used for option pricing have log-price dynamics

```math
d \log S_t = \left( r - \frac{1}{2} \sigma^2 \right) d t + \sigma\, d z_t
```

The option price is discounted:
```math
V_0 = e^{-r T} &Eopf;[\text{payoff}].
```

---

## Features

* Simulates individual stock price paths
* Estimates terminal price statistics
* Counts returns/crossings of the initial price
* Prices European call options using risk-neutral measure
* Prices European put options using risk-nutral measure
* Discounts payoffs using risk-neutral interest rate
* Estimates Monte Carlo standard error
* Includes analytical Black-Scholes call and put pricing
---

## Functions

### `MC_path`

```python
MC_path(Nt, mu, sigma, S0, dt)
```

Simulates a single stock price path over `Nt` time steps using log returns.

---

### `MC_terminal_mean_std`

```python
MC_terminal_mean_std(Np, Nt, mu, sigma, S0, dt)
```

Estimates the **mean** and **standard deviation** of the terminal stock price using `Np` Monte Carlo paths.

---

### `MC_mean_orig_returns`

```python
MC_mean_orig_returns(Np, Nt, mu, sigma, S0, dt)
```

Estimates the average number of times a price path:

* Returns exactly to the initial price, or
* Crosses the initial price level

---

### `MC_calls`

```python
MC_calls(K, Np, Nt, r, sigma, S0, dt)
```

Estimates the price of a **European call option** with strike price `K` using Monte Carlo simulation:

```math
C = e^{-r T} &Eopf;[\max(S_T - K, 0)]
```

---

### `MC_puts`

```python
MC_puts(K, Np, Nt, mu, sigma, S0, dt)
```

Estimates the price of a **European put option** with strike price `K`:

```math
P = e^{-r T} &Eopf;[\max(K - S_T, 0)]
```

---

### `black_scholes_call`

```python
black_scholes_call(S0, K, T, r, sigma)
```

Calculates the analytical Black-Scholes price of a European call option.

---

### `black_scholes_put`

```python
black_scholes_put(S0, K, T, r, sigma)
```

Calculates the analytical Black-Scholes price of a European put option.


---

## How to Run

Run the script directly:

```bash
python CallPutPricingMC.py
```

### Example Parameters

```python CallPutPricingMC.py
Np = 10000     # number of Monte Carlo paths
Nt = 252       # number of time steps (trading days)
r = 0.05      # expected annual return
sigma = 0.4    # volatility
S0 = 100       # initial stock price
dt = 1/Nt     # time step
K = 100        # strike price
```

The script prints the estimated European put and call options price with $`95\%`$ confidence interval, together with the Black-Scholes pricing.

---

## Notes & Limitations

* The random increments use a **±1 binomial model**, not Gaussian noise
* This is not a production-grade pricing engine
* Intended for learning and experimentation

---

## Possible Extensions

* Add risk-neutral drift $` \mu = r `$
* Include discounting $` e^{-rT} `$
* Replace binomial noise with Gaussian noise
* Compare against Black–Scholes formula
* Plot path ensembles and payoff distributions

---

## Requirements

```bash
pip install numpy scipy

---

## Disclaimer

This code is provided for **educational purposes only** and should not be used for real financial decision-making.
