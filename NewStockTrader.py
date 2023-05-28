from mimetypes import init
import backtesting 
from backtesting import Backtest, Strategy
from backtesting.test import GOOG
import talib 
from backtesting.lib import crossover
import pandas as pd

print(GOOG)
 
class RsiOscillator(Strategy):
    upper_bound = 70    
    lower_bound = 30
    rsi_window = 14

    def init(self):
        self.rsi = self.I(talib.RSI, self.data.Close, self.rsi_window)

    def next(self):
        price = self.data.Close[-1]

        if crossover(self.rsi, self.upper_bound):
            self.position.close()

        elif crossover(self.lower_bound, self.rsi):
            self.buy(tp=1.15 * price, sl=0.90 * price) # Take profit if return is 15% & sell if return is -10%


# Buy signal is when price crosses both 20MA and 9-day EMA 
class EMAStrategy(Strategy):
     upper_bound = 70    
     lower_bound = 30
     rsi_window = 14

     def init(self):
        self.ema = self.I(talib.EMA, self.data.Close, self.rsi_window)

     def next(self):
        price = self.data.Close[-1]

        ma_20 = talib.SMA(self.data.Close, timeperiod=20)[-1]
        ema_9 = talib.EMA(self.data.Close, timeperiod=9)[-1]
 
        if price > ma_20 and price > ema_9:
            self.buy(tp=1.15 * price, sl=0.90 * price) # Taking profit if return is 15% & selling if return is -10%
            pass

strategies = [EMAStrategy, RsiOscillator]

#Stratigies I am backtesting
bt = Backtest(GOOG,
              EMAStrategy, 
             cash=10_000)

#Testing for optimal trading strategy

stats = bt.optimize(
    upper_bound=range(50, 85, 5),
    lower_bound=range(10, 45, 5),
    rsi_window=range(10, 30, 2))

# Prints data about trades
#trade_details = bt.run().get_trades()
#print(trade_details.to_string())
stats = bt.run()
print(stats)
bt.plot()
