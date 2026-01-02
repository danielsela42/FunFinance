# Arbitrage Calculator

This repository provides tools to explore **arbitrage opportunities in betting** using Python. It includes scripts to calculate standard (unbiased) and biased arbitrage for two outcomes, given odds from two different bookmakers.

---

## Theory

Arbitrage in betting is the practice of using differences in odds offered by multiple bookmakers to guarantee a profit, independent of the outcome.

Given odds (a) for an outcome (A), the **implied probability** is

[
p = \frac{1}{a}.
]

For multiple outcomes (A_1, \dots, A_n) with odds (a_1, \dots, a_n), the **total implied probability** is

[
p_I = \sum_{k=1}^{n} \frac{1}{a_k}.
]

* If (p_I > 1), the bookmaker has an edge (they make a profit).
* If (p_I < 1), a bettor can exploit the odds to create a guaranteed profit.

---

### Standard Arbitrage (Case a)

In standard arbitrage, the goal is to stake amounts so that **profit is the same regardless of the outcome**.

For **two outcomes**, (A_1) and (A_2), with total stake (S):

[
s_1 + s_2 = S, \quad a_1 s_1 - S = a_2 s_2 - S
]

Solving these gives

[
s_1 = \frac{p_1}{p_I} S, \quad s_2 = \frac{p_2}{p_I} S
]

where (p_1 = 1/a_1), (p_2 = 1/a_2), and (p_I = p_1 + p_2). The **profit** is then given by

[
\text{Profit} = \frac{1}{p_I} S - S = \left(\frac{1}{p_I} - 1\right) S,
]
which is positive if and only if (p_I < 1).

This readily generalizes to (n) outcomes:
[
s_k = \frac{p_k}{p_I} S, \quad k=1,\dots,n
]
with the same guaranteed profit.

---

### Biased Arbitrage (Case b)

In biased arbitrage, the bettor **maximizes profit for one outcome** while ensuring no loss if the other outcome occurs.

For two outcomes biased towards (A_1):

[
s_2 = \frac{S}{a_2}, \quad s_1 = S - s_2
]

This strategy gives a higher profit for the favored outcome but may be lower than standard arbitrage in terms of uniformity.

---

### Practical Notes

* Arbitrage opportunities are rare and quickly disappear as bookmakers adjust odds.
* When attempting real-world betting, rounding stakes to realistic increments (e.g., multiples of 5 or 10) is necessary to avoid suspicion.
* Sports betting is **illegal in some regions**, including Texas; this code is for **educational purposes only**.

---

## Code Overview

This repository includes three Python scripts:

1. **`argument_inputs.py`** – Collects user inputs for the number of bets, stake amount, and odds from two bookmakers.
2. **`unbiased_arb.py`** – Calculates **standard arbitrage** (Case a). Determines if a guaranteed profit exists and computes the optimal stakes.
3. **`biased_arb.py`** – Calculates **biased arbitrage** (Case b). Focuses on maximizing profit for a preferred outcome while avoiding loss on the other.

**Workflow:**

1. The user inputs the number of bets, stake, and odds for each bookmaker.
2. The scripts compute implied probabilities and identify if arbitrage is possible.
3. If arbitrage exists, the optimal stakes and guaranteed profit are displayed.

---

## Usage Example

```bash
python unbiased_arb.py
python biased_arb.py
```

The program will prompt for odds and stake values and output the calculated stakes and expected profit.
