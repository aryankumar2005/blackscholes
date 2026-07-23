import math

def binomial_method(S: float, E: float, r: float, sigma: float, T: float, t_0: float, N: int) -> float:
    
    """
    Pricing a European call option using an N-step binomial tree, using i up-jumps, (i-N) down-jumps

    Parameters:
    
    S: Share Price
    E: Strike Price
    r: Risk Free Interest Rate
    sigma: Volatility
    T: Expiry Date
    t_0: Purchase Date
    N: Number of time steps

    Returns:

    The fair price of the call at t_0 (estimate), float
    """
    
    delta_t = (T - t_0) / N 
    A = 0.5 * (math.exp(-r * delta_t) + math.exp((r + sigma**2) * delta_t))
    
    # Up Jump Formula
    u = A + math.sqrt(A**2 - 1) 
    # Down Jump Formula             
    d = 1 / u     
    # Probability Formula                           
    p = (math.exp(r * delta_t) - d) / (u - d) 
    

    payoffs = []
    for i in range(N + 1):
       S_final = S * u**i * d**(N - i)
       payoff = max(S_final - E, 0)
       payoffs.append(payoff)

    for _ in range(N):
        new_payoffs = []
        for i in range(len(payoffs) - 1):
            V = math.exp(-r * delta_t) * (p * payoffs[i + 1] + (1 - p) * payoffs[i])
            new_payoffs.append(V)
        payoffs = new_payoffs

    return payoffs[0]

