"""
BITC4SHEW
Strategy Engine

Generates trading signals from indicators.
"""


class Strategy:

    def __init__(self, price, ema, rsi):
        self.price = price
        self.ema = ema
        self.rsi = rsi


    def analyze(self):

        score = 0
        reasons = []


        # Trend analysis
        if self.price > self.ema:
            score += 1
            reasons.append("Price above EMA (bullish)")
        else:
            score -= 1
            reasons.append("Price below EMA (bearish)")


        # Momentum analysis
        if self.rsi < 30:
            score += 1
            reasons.append("RSI oversold")

        elif self.rsi > 70:
            score -= 1
            reasons.append("RSI overbought")

        else:
            reasons.append("RSI neutral")


        # Decision

        if score >= 2:
            signal = "BUY"

        elif score <= -2:
            signal = "SELL"

        else:
            signal = "HOLD"


        return {
            "signal": signal,
            "score": score,
            "reasons": reasons
        }
