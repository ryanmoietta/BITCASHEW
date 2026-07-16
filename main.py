import time
from datetime import datetime

from market import Market
from indicators import Indicators
from strategy import Strategy
from analysis import Analyzer

from radar import rank_opportunities, long_term_pick

from rich.live import Live

from dashboard import create_dashboard
from banner import show_banner

import state



market = Market()



coins = [
    "BTCUSDT",
    "ETHUSDT",
    "BNBUSDT",
    "SOLUSDT",
    "XRPUSDT",
    "ADAUSDT",
    "DOGEUSDT",
    "TRXUSDT",
    "LINKUSDT",
    "AVAXUSDT",
]


ENTRY_INTERVAL = "5m"

previous_prices = {}





def candle_strip(candles):

    result = []

    for candle in candles[-10:]:

        if candle["close"] > candle["open"]:
            result.append("green")

        elif candle["close"] < candle["open"]:
            result.append("red")

        else:
            result.append("neutral")

    return result






def price_move(symbol, price):

    old = previous_prices.get(symbol)

    previous_prices[symbol] = price


    if old is None:
        return "→"

    if price > old:
        return "↑"

    if price < old:
        return "↓"

    return "→"






def scan_market():

    data = []


    for coin in coins:


        candles = market.get_candles(
            coin,
            ENTRY_INTERVAL,
            100
        )


        stats = market.get_24h_stats(
            coin
        )


        analysis = Analyzer(
            candles
        ).calculate()



        price = candles[-1]["close"]



        strategy = Strategy(

            price,

            Indicators(candles)
            .ema()
            .iloc[-1],

            analysis["rsi"]

        )


        signal = strategy.analyze()



        data.append({

            "name":coin,

            "price":price,

            "change":stats["change"],

            "trend":analysis["trend"],

            "confidence":analysis["confidence"],

            "signal":signal["signal"],

            "rsi":analysis["rsi"],

            "volume":analysis["volume"],

            "move":price_move(
                coin,
                price
            ),

            "candles":candle_strip(
                candles
            )

        })


    return data






def info():

    return {

        "exchange":"Binance",

        "entry_tf":"5m",

        "trend_tf":"1h",

        "assets":len(coins),

        "time":datetime.now()
        .strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    }






show_banner()



with Live(

    create_dashboard(
        [],
        info(),
        [],
        "Loading..."
    ),

    refresh_per_second=4

) as live:


    while True:


        try:


            data = scan_market()



            state.market_data = data


            state.top_opportunities = rank_opportunities(
                data
            )


            state.long_term_pick = long_term_pick(
                data
            )


            state.last_update = datetime.now().strftime(
                "%H:%M:%S"
            )



            live.update(

                create_dashboard(

                    data,

                    info(),

                    state.top_opportunities,

                    state.long_term_pick

                )

            )


            time.sleep(10)




        except KeyboardInterrupt:

            print(
                "BITC4SHEW OFFLINE"
            )

            break
