import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def plot_portfolio_values(cash, returns, positions):
    portfolio_value_list = cash * np.cumprod(1 + returns)
    position_list = positions.iloc[:, 0].values
    date_list = portfolio_value_list.index

    plt.figure(figsize=(10, 6))
    plt.plot(portfolio_value_list)

    # Find the entry and exit points
    entry_list = []
    exit_list = []

    for i, position in enumerate(position_list):
        if i == len(position_list) - 1:
            continue
        if position == 0 and position_list[i + 1] != 0:
            entry_list.append(i)
        elif position != 0 and position_list[i + 1] == 0:
            exit_list.append(i)

    # Plot the entry points as green triangles
    plt.plot([date_list[i] for i in entry_list], [portfolio_value_list[i] for i in entry_list],
             marker='^', color='green', linestyle='None', label='Entry Point')

    # Plot the exit points as red triangles
    plt.plot([date_list[i] for i in exit_list], [portfolio_value_list[i] for i in exit_list],
             marker='v', color='red', linestyle='None', label='Exit Point')

    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

    plt.xlabel('Date')
    plt.title('Portfolio Values with Entry and Exit Points')
    plt.legend()

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