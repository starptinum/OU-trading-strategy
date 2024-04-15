import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def plot_portfolio_values(cash, returns):
    portfolio_value_list = cash * np.cumprod(1 + returns)

    plt.figure(figsize=(10, 6))
    plt.plot(portfolio_value_list)

    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

    plt.xlabel('Date')
    plt.title('Portfolio Values')

    plt.show()


def plot_underwater(returns):
    accumulated_values_list = np.cumprod(1 + returns)
    date_list = returns.index

    # Calculate drawdown
    drawdown = []
    peak = accumulated_values_list[0]
    for price in accumulated_values_list:
        if price > peak:
            peak = price
        drawdown.append(price / peak - 1)

    drawdown = np.array(drawdown)

    plt.figure(figsize=(10, 6))
    plt.plot(date_list, drawdown, color='red')
    plt.fill_between(date_list, drawdown, 0, where=drawdown < 0, color='red', alpha=0.5)

    plt.xlabel('Date')
    plt.ylabel('Drawdown')
    plt.title('Underwater Plot')
    plt.show()