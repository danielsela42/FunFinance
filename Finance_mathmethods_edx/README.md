# Call & Put Option Pricing via Monte Carlo Simulation

This script implements a **Monte Carlo simulation** of stock price dynamics and uses it to estimate the prices of **European call and put options**. It also includes routines for analyzing basic statistical properties of simulated price paths.

The code is intended as **educational and exploratory work**, demonstrating how option pricing and path statistics can be estimated numerically from stochastic models.

---

## Model Overview

The stock price $` S_t `$ is modeled using a **discrete-time log-price process**:

```math
\log S_{t+1} = \log S_t + \mu \Delta t + \sigma \sqrt{\Delta t}, z_t
```

where:

* $` \mu `$ is the expected return
* $` \sigma `$ is the volatility
* $` \Delta t `$ is the time step
* $` z_t \in \{ -1, +1 \} `$ is a symmetric random variable

This corresponds to a **binomial approximation** of geometric Brownian motion.

---

## Features

* Simulates individual stock price paths
* Estimates terminal price statistics
* Counts returns to the initial price
* Prices European call options
* Prices European put options

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

This provides a simple diagnostic of path fluctuation behavior.

---

### `MC_calls`

```python
MC_calls(K, Np, Nt, mu, sigma, S0, dt)
```

Estimates the price of a **European call option** with strike price `K` using Monte Carlo simulation:

```math
C = \mathbb{E}[\max(S_T - K, 0)]
```

---

### `MC_puts`

```python
MC_puts(K, Np, Nt, mu, sigma, S0, dt)
```

Estimates the price of a **European put option** with strike price `K`:

```math
P = \mathbb{E}[\max(K - S_T, 0)]
```

---

## How to Run

Run the script directly:

```bash
python CallPutPricingMC.py
```

### Default Parameters

```python
Np = 10000     # number of Monte Carlo paths
Nt = 252       # number of time steps (trading days)
mu = 0.06      # expected annual return
sigma = 0.4    # volatility
S0 = 100       # initial stock price
dt = 1/252     # time step
K = 100        # strike price
```

The script prints the estimated **European put option price**.

---

## Notes & Limitations

* No discounting factor is applied (risk-neutral pricing is not enforced)
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
pip install numpy matplotlib
```

---

## Disclaimer

This code is provided for **educational purposes only** and should not be used for real financial decision-making.
