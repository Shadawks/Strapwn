from rich.console import Console
from rich.theme import Theme

class StrapwnLogger:
    def __init__(self):
        self.theme = Theme({
            "error": "red",
            "display": "cyan",
            "success": "green",
            "warning": "yellow",
            "info": "blue"
        })
        self.console = Console(theme=self.theme)
    def error(self, text: str):
        '''Print an error message.'''
        self.console.print(f"\n[!] {text}\n", style="error")
    def display(self, text: str):
        '''Print a message.'''
        self.console.print(text, style="display")
    def success(self, text: str):
        '''Print a success message.'''
        self.console.print(f"\n[+] {text}\n", style="success")
    def warning(self, text: str):
        '''Print a warning message.'''
        self.console.print(f"\n[-] {text}\n", style="warning")
    def info(self, text: str):
        '''Print an info message.'''
        self.console.print(f"\n[?] {text}\n", style="info")

logger = StrapwnLogger()