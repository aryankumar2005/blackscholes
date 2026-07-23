import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from pricing.black_scholes import black_scholes

"""
    Computes and plots the Black Scholes diagram with input sliders for Exercise Price, Interest Rate,
    Volatility, Expiry Date

"""


# Parameters
initial_S = 100
initial_strike = 105
initial_sigma = 0.3
initial_expiry = 3
t_0 = 0
initial_rate = 0.05

S_values = np.linspace(50, 150, 100)


# Function to calculate option prices

def calculate_prices(rate, sigma, strike, expiry):

    prices = []

    for stock_price in S_values:

        _, _, price, _ = black_scholes(
            stock_price,
            strike,
            rate,
            sigma,
            expiry,
            t_0
        )

        if np.isfinite(price):
            prices.append(price)
        else:
            prices.append(0)
        
       

    return prices


# Initial graph

fig, ax = plt.subplots(figsize=(8,5))

plt.subplots_adjust(bottom=0.2)

initial_prices = calculate_prices(initial_rate, initial_sigma, initial_strike, initial_expiry)

line, = ax.plot(
    S_values,
    initial_prices,
    linewidth=2,
    label="Black-Scholes Call Price"
)

ax.set_xlabel("Share Price")
ax.set_ylabel("Option Price")
ax.set_title("Black-Scholes Call Option Value")
ax.grid(True)
ax.legend()


# Sliders

plt.subplots_adjust(bottom=0.25)

ax_rate = plt.axes([0.25, 0.15, 0.5, 0.03])

rate_slider = Slider(
    ax_rate,
    "Interest Rate",
    -0.01,
    0.2,
    valinit=initial_rate
)

ax_sigma = plt.axes([0.25,0.10,0.5,0.03])

sigma_slider = Slider(
    ax_sigma,
    "Volatility",
    0.05,
    1,
    valinit=initial_sigma
)

ax_strike = plt.axes([0.25, 0.05, 0.5, 0.03])

strike_slider = Slider(
    ax_strike,
    "Strike Price",
    50,
    200,
    valinit=initial_strike
)

ax_expiry = plt.axes([0.25, 0, 0.5, 0.03])

expiry_slider = Slider(
    ax_expiry,
    "Expiry Date",
    0.01,
    10950,
    valinit=initial_expiry
)


# Update function

def update(value):

    new_rate = rate_slider.val
    new_sigma = sigma_slider.val
    new_strike = strike_slider.val
    new_expiry = expiry_slider.val
    new_prices = calculate_prices(new_rate, new_sigma, new_strike, new_expiry)

    line.set_ydata(new_prices)
    ax.relim()
    ax.autoscale_view()

    

    ax.set_xlabel("Share Price")
    ax.set_ylabel("Option Price")
    ax.set_title("Black-Scholes Call Option Value")
    ax.grid(True)
    ax.legend()

    fig.canvas.draw_idle()


rate_slider.on_changed(update)
sigma_slider.on_changed(update)
strike_slider.on_changed(update)
expiry_slider.on_changed(update)

plt.show()