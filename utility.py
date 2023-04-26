'''Utility functions for Strapwn.'''
from os import system, name
from rich.console import Console
from logger import logger

def cls() -> None:
    '''Clear the screen.'''
    system('cls' if name=='nt' else 'clear')

def display_motd() -> None:
    '''Display the MOTD.'''
    console = Console()
    cls()
    console.print("""[bold magenta]
    ███████╗████████╗██████╗  █████╗ ██████╗ ██╗    ██╗███╗   ██╗
    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║    ██║████╗  ██║
    ███████╗   ██║   ██████╔╝███████║██████╔╝██║ █╗ ██║██╔██╗ ██║
    ╚════██║   ██║   ██╔══██╗██╔══██║██╔═══╝ ██║███╗██║██║╚██╗██║
    ███████║   ██║   ██║  ██║██║  ██║██║     ╚███╔███╔╝██║ ╚████║
    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝
    [/bold magenta][bold yellow]\n\tby @Shadawks[/bold yellow]
    """, justify="center")

def clean_exit() -> None:
    display_motd()
    logger.info("Goodbye !")
    exit(0)