# Plots the Black-Scholes call price against the share price
# for a few different volatilities, to see how volatility changes the price

import matplotlib.pyplot as plt
from pricing.black_scholes import black_scholes

# Parameters
E = 105      # strike price
r = 0.05     # interest rate
T = 3        # expiry date (years)
t_0 = 0      # purchase date (years)

# volatilities to compare
sigma_values = [0.1, 0.3, 0.5]

# share prices from 50 to 150
S_values = []
for S in range(50, 151):
    S_values.append(S)

# for each volatility, work out the call price at every share price and plot it
for sigma in sigma_values:
    call_prices = []
    for S in S_values:
        call_price, put_price = black_scholes(S, E, r, sigma, T, t_0)
        call_prices.append(call_price)
    plt.plot(S_values, call_prices, label="volatility = " + str(sigma))

# what the option would be worth if it expired today: max(S - E, 0)
payoff = []
for S in S_values:
    payoff.append(max(S - E, 0))
plt.plot(S_values, payoff, 'k--', label="payoff at expiry")

plt.xlabel("Share price")
plt.ylabel("Call option price")
plt.title("Black-Scholes call price (strike 105, 3 years to expiry)")
plt.legend()
plt.grid(True)
plt.show()
