from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.console import Group




def signal_color(signal):

    if signal == "BUY":
        return "[yellow]BUY[/yellow]"

    if signal == "SELL":
        return "[green]SELL[/green]"

    return "[red]HOLD[/red]"





def move_color(move):

    if move == "↑":
        return "[green]↑[/green]"

    if move == "↓":
        return "[red]↓[/red]"

    return "[white]→[/white]"





def candle_render(candles):

    text = Text()


    for candle in candles:

        if candle == "green":

            text.append(
                "▰",
                style="green"
            )


        elif candle == "red":

            text.append(
                "▰",
                style="red"
            )


        else:

            text.append(
                "·",
                style="white"
            )


    return text






def create_dashboard(
    data,
    info,
    top,
    investment
):


    table = Table(
        expand=True
    )


    columns = [

        "COIN",
        "PRICE",
        "MOVE",
        "24H",
        "TREND",
        "SIGNAL",
        "CONF",
        "RSI",
        "VOL",
        "CANDLES"

    ]



    for col in columns:

        table.add_column(
            col,
            justify="center"
        )





    for coin in data:


        change = coin["change"]


        if change >= 0:

            change_text = (
                f"[green]+{change:.2f}%[/green]"
            )

        else:

            change_text = (
                f"[red]{change:.2f}%[/red]"
            )



        if coin["trend"] == "BULLISH":

            trend = "[green]BULLISH[/green]"

        else:

            trend = "[red]BEARISH[/red]"




        table.add_row(

            coin["name"],

            f"${coin['price']:,.2f}",

            move_color(
                coin["move"]
            ),

            change_text,

            trend,

            signal_color(
                coin["signal"]
            ),

            f"{coin['confidence']}%",

            f"{coin['rsi']:.1f}",

            coin["volume"],

            candle_render(
                coin["candles"]
            )

        )





    radar = Text()


    radar.append(
        "\n🔥 TOP OPPORTUNITIES\n\n",
        style="bold yellow"
    )


    for index, coin in enumerate(top):

        radar.append(
            f"{index+1}. {coin['name']}  "
            f"{coin['confidence']}%\n",
            style="green"
        )



    radar.append(
        "\n⭐ LONG TERM INTEREST\n",
        style="bold cyan"
    )


    radar.append(
        investment,
        style="bold green"
    )





    header = Text()


    header.append(
        "BITC4SHEW LIVE TERMINAL\n",
        style="bold cyan"
    )


    header.append(
        f"""
Exchange : {info['exchange']}
Entry TF : {info['entry_tf']}
Trend TF : {info['trend_tf']}
Assets   : {info['assets']}
Updated  : {info['time']}

BY RYAN MOIETTA
""",
        style="white"
    )



    return Panel(

        Group(
            table,
            radar
        ),

        title=header,

        border_style="cyan"

    )
