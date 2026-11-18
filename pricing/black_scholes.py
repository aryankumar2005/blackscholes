# Black-Scholes formula for pricing a European call option

import math
from scipy.stats import norm   # norm.cdf(x) is N(x), the standard normal cumulative distribution function


def black_scholes(S, E, r, sigma, T, t_0):
    # Inputs:
    # S - share price
    # E - strike price (the price you can buy the share for at expiry)
    # r - risk free interest rate
    # sigma - volatility
    # T - expiry date (in years)
    # t_0 - purchase date (in years)
    #
    # Outputs:
    # call_price - fair price of the European call at t_0
    # put_price - fair price of the European put at t_0

    # time left until expiry
    tau = T - t_0

    # work out d1 and d2
    d_1 = (math.log(S / E) + (r + sigma**2 / 2) * tau) / (sigma * math.sqrt(tau))
    d_2 = d_1 - sigma * math.sqrt(tau)

    # Black-Scholes formula for the call price
    call_price = S * norm.cdf(d_1) - E * math.exp(-r * tau) * norm.cdf(d_2)

    # use put-call parity to get the put price from the call price
    put_price = call_price - S + E * math.exp(-r * tau)

    return call_price, put_price
