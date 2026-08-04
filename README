# Black-Scholes and Binomial Model Option Pricer

A small quantitative finance project built to develop Python skills, comparing two ways of pricing a European vanilla call option: the closed-form Black-Scholes solution, and a numerical N-step binomial tree. The project demonstrates that the binomial method converges to the Black-Scholes price as the number of steps increases, and includes interactive tools for exploring both models.

![Convergence plot](plots/convergence.png)

## Contents

| File | Description |
|---|---|
| `pricing/black_scholes.py` | Closed-form Black-Scholes pricer |
| `pricing/binomial_method.py` | N-step binomial tree pricer |
| `convergence_plot.py` | Interactive tool — input share price, strike, rate, volatility, expiry; computes both prices and plots the binomial method's absolute error against Black-Scholes as N increases |
| `black_scholes_interactive.py` | Slider-based tool for visualising how Black-Scholes call/put price changes with strike, rate, volatility, and expiry |
| `requirements.txt` | Dependencies |

## Models

### Black-Scholes

Prices a European call in closed form:

d1 = [ln(S/E) + (r + sigma²/2) * tau] / (sigma * sqrt(tau))
d2 = d1 - sigma * sqrt(tau)
Call = S * N(d1) - E * e^(-r*tau) * N(d2)

where `tau = T - t_0` and `N(.)` is the standard normal CDF. The put price follows from put-call parity.


![Interactive tool](plots/convergence_results.png)

### Binomial Tree

Discretises time into N steps, builds up-and-down jump sizes `u`, `d` and a risk-neutral probability `p`, computes terminal payoffs across the tree's N+1 final nodes, and works backward to today's price via risk-neutral discounting.

## Convergence Results

As N increases, the binomial price converges to the Black-Scholes price as expected:

![Convergence results](plots/convergence_results.png)







