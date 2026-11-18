# Compares the binomial tree price with the Black-Scholes price
# to check that the binomial price gets closer as the number of steps N goes up

import matplotlib.pyplot as plt
from pricing.black_scholes import black_scholes
from pricing.binomial_method import binomial_method

# ask the user for the inputs
S = float(input("Share price: "))
E = float(input("Strike price: "))
r = float(input("Interest rate (e.g. 0.05 for 5%): "))
sigma = float(input("Volatility (e.g. 0.2 for 20%): "))
T = float(input("Time to expiry in years: "))
t_0 = 0   # buying the option today

# Black-Scholes price (the exact answer)
bs_price, put_price = black_scholes(S, E, r, sigma, T, t_0)
print("Black-Scholes call price:", round(bs_price, 4))

# numbers of steps to try in the binomial tree
N_values = [3, 10, 25, 50, 100, 250, 500, 1000, 2000]

# list to store the error for each N
errors = []

for N in N_values:
    # binomial price with N steps
    binomial_price = binomial_method(S, E, r, sigma, T, t_0, N)
    # how far it is from the Black-Scholes price
    error = abs(binomial_price - bs_price)
    errors.append(error)
    print("N =", N, "  binomial price:", round(binomial_price, 4), "  error:", round(error, 5))

# plot the error against N
# log scales on both axes because N and the error both change by a lot
plt.plot(N_values, errors, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of steps, N')
plt.ylabel('|Binomial - Black-Scholes|')
plt.title('Convergence of the binomial tree to Black-Scholes')
plt.grid(True)
plt.show()
