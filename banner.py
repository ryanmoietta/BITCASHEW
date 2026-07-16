from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import pyfiglet


console = Console()



def show_banner():


    logo = pyfiglet.figlet_format(
        "BITC4SHEW",
        font="slant"
    )


    text = Text(
        logo,
        style="bold cyan"
    )


    subtitle = Text(
    "\nCRYPTO INTELLIGENCE ENGINE\n"
    "LIVE MARKET ANALYSIS TERMINAL\n"
    "STATUS: ONLINE\n\n"
    "BY RYAN MOIETTA",
    style="bold yellow"
)


    content = Text()

    content.append_text(text)
    content.append_text(subtitle)



    console.print(
        Panel(
            Align.center(content),
            border_style="green",
            title="SYSTEM BOOT"
        )
    )
