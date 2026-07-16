"""
BITC4SHEW
Indicator Engine

Calculates technical indicators.
"""

import pandas as pd


class Indicators:

    def __init__(self, candles):
        self.data = pd.DataFrame(candles)


    def ema(self, period=20):
        """
        Calculate Exponential Moving Average.
        """

        return self.data["close"].ewm(
            span=period,
            adjust=False
        ).mean()


    def rsi(self, period=14):
        """
        Calculate Relative Strength Index.
        """

        delta = self.data["close"].diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(period).mean()
        avg_loss = loss.rolling(period).mean()

        rs = avg_gain / avg_loss

        rsi = 100 - (100 / (1 + rs))

        return rsi
