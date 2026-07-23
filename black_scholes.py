import math
from scipy.stats import norm

def black_scholes(S: float, E: float, r: float, sigma: float, T: float, t_0: float):
    
    """
    Pricing a European call option using the known Black Scholes solution

    Parameters:
    
    S: Share Price
    E: Strike Price
    r: Risk Free Interest Rate
    sigma: Volatility
    T: Expiry Date
    t_0: Purchase Date

    Returns:

    The fair price of the call at t_0, float
    """
    
    tau = T - t_0

    d_1 = (math.log(S / E) + (r + (sigma ** 2) / 2) * tau) / (sigma * math.sqrt(tau))
    d_2 = d_1 - sigma * math.sqrt(tau)

    N_d_1 = norm.cdf(d_1)
    N_d_2 = norm.cdf(d_2)

    call_price = S * N_d_1 - E * math.exp(-r * tau) * N_d_2
    
    # Using Put-Call Parity, we can derive the corresponding fair European Vanilla Put price
    put_price = call_price - S + E * math.exp(-r * tau)
    return d_1, d_2, call_price, put_price



