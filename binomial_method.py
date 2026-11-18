# Binomial tree method for pricing a European call option

import math


def binomial_method(S, E, r, sigma, T, t_0, N):
    # Inputs are the same as black_scholes, plus:
    # N - number of time steps in the tree
    #
    # Output:
    # the estimated fair price of the call at t_0

    # length of each time step
    delta_t = (T - t_0) / N

    # A is used to work out the size of the up and down jumps
    A = 0.5 * (math.exp(-r * delta_t) + math.exp((r + sigma**2) * delta_t))

    # up jump
    u = A + math.sqrt(A**2 - 1)
    # down jump
    d = 1 / u
    # risk neutral probability of an up jump
    p = (math.exp(r * delta_t) - d) / (u - d)

    # discount factor for one time step
    discount = math.exp(-r * delta_t)

    # make a list of the payoffs at the end of the tree
    # there are N+1 end points, and i is the number of up jumps to get there
    payoffs = []
    for i in range(N + 1):
        # share price at this end point
        S_final = S * u**i * d**(N - i)
        # payoff of a call is share price minus strike price, or 0 if that is negative
        payoff = max(S_final - E, 0)
        payoffs.append(payoff)

    # now go backwards through the tree one step at a time
    for step in range(N):
        # list to store the values one step earlier
        new_payoffs = []
        # each value is the discounted average of the two values after it
        for i in range(len(payoffs) - 1):
            V = discount * (p * payoffs[i + 1] + (1 - p) * payoffs[i])
            new_payoffs.append(V)
        # replace the old list with the new one
        payoffs = new_payoffs

    # after going back N steps there is only one value left, which is the price today
    return payoffs[0]
