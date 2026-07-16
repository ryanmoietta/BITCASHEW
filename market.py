import requests


class Market:


    def __init__(self):

        print("Market Engine initialized.")



    def get_candles(
        self,
        symbol,
        interval="5m",
        limit=100
    ):

        url = (
            "https://api.binance.com/api/v3/klines"
            f"?symbol={symbol}"
            f"&interval={interval}"
            f"&limit={limit}"
        )


        response = requests.get(url)

        data = response.json()



        candles = []


        for c in data:

            candles.append({

                "open": float(c[1]),

                "high": float(c[2]),

                "low": float(c[3]),

                "close": float(c[4]),

                "volume": float(c[5])

            })


        return candles




    def get_24h_stats(self, symbol):


        url = (
            "https://api.binance.com/api/v3/ticker/24hr"
            f"?symbol={symbol}"
        )


        response = requests.get(url)

        data = response.json()



        return {

            "change": float(
                data["priceChangePercent"]
            ),

            "volume": float(
                data["quoteVolume"]
            )

        }
