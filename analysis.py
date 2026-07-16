import pandas as pd
import ta



class Analyzer:


    def __init__(self, candles):

        self.candles = candles


        self.df = pd.DataFrame(candles)



    def calculate(self):


        close = self.df["close"]

        volume = self.df["volume"]



        ema20 = ta.trend.EMAIndicator(
            close,
            window=20
        ).ema_indicator().iloc[-1]



        ema50 = ta.trend.EMAIndicator(
            close,
            window=50
        ).ema_indicator().iloc[-1]



        rsi = ta.momentum.RSIIndicator(
            close
        ).rsi().iloc[-1]



        macd = ta.trend.MACD(
            close
        ).macd_diff().iloc[-1]



        current_volume = volume.iloc[-1]

        avg_volume = volume.mean()



        if ema20 > ema50:

            trend = "BULLISH"

        else:

            trend = "BEARISH"




        if rsi > 70:

            momentum = "OVERBOUGHT"


        elif rsi < 30:

            momentum = "OVERSOLD"


        else:

            momentum = "HEALTHY"




        if current_volume > avg_volume:

            volume_state = "HIGH"


        else:

            volume_state = "NORMAL"




        score = 50



        if trend == "BULLISH":

            score += 20

        else:

            score -= 10




        if macd > 0:

            score += 15



        if 40 < rsi < 70:

            score += 15



        score = max(
            0,
            min(
                score,
                100
            )
        )



        return {


            "trend": trend,

            "momentum": momentum,

            "volume": volume_state,

            "confidence": score,

            "rsi": rsi,

            "macd": macd

        }
