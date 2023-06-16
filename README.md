# NewStockTrader
This code utilizes the backtesting library to backtest two trading strategies, RsiOscillator and EMAStrategy, on historical price data for Google (GOOG) stock. Here's a summary of what the code does:
It imports necessary modules including mimetypes, backtesting, talib, and pandas.
The GOOG variable represents historical price data for Google (GOOG) stock, which is obtained from the backtesting.test module.
The code defines two custom trading strategies: RsiOscillator and EMAStrategy.
The RsiOscillator strategy uses the Relative Strength Index (RSI) to generate buy and sell signals based on upper and lower RSI bounds. It closes a position if the RSI crosses above the upper bound and opens a new position if the RSI crosses below the lower bound.
The EMAStrategy strategy uses exponential moving averages (EMA) and a simple moving average (SMA) to generate buy signals. If the closing price is above both the 20-period SMA and the 9-day EMA, it opens a new position.
The code creates a list of strategies containing EMAStrategy and RsiOscillator.
A Backtest object is created with the GOOG data and the EMAStrategy as the strategy to be backtested. The initial cash is set to $10,000.
The code performs optimization by iterating over specified parameter ranges for the strategies. It optimizes the upper bound, lower bound, and RSI window for the strategies 
The backtest is executed by running bt.run(), and the results are stored in the stats variable.
The results of the backtest, including performance metrics and trade statistics, are printed.
A plot of the backtest results is generated using bt.plot().
In summary, this code conducts a backtest on the EMAStrategy with different parameter combinations, such as upper and lower bounds, and RSI window, to find the optimal trading strategy. It also backtests the RsiOscillator strategy. The results are printed, and a plot is generated to visualize the backtest results.
