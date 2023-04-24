'''Strapi Plugin Utility'''
from typing import List
import os
import importlib
from strapi_exploit import StrapiExploitInterface
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt
from rich.box import SIMPLE
from utility import cls, display_motd
from logger import logger


def load_plugins() -> List[str]:
    '''Load plugins from the plugins directory.'''
    plugins = []
    for plugin in os.listdir("plugins"):
        if plugin.endswith(".py") and plugin != "__init__.py":
            plugins.append(plugin)
    return plugins

def import_plugins(plugins: List[str]) -> List[StrapiExploitInterface]:
    '''Import plugins from the plugins list and return a list of plugin classes.'''
    plugin_class_list = []
    for plugin in plugins:
        try:
            plugin = plugin.replace(".py", "")
            plugin = importlib.import_module(f"plugins.{plugin}", "init")
            plugin_class = plugin.init()
            if issubclass(plugin_class.__class__, StrapiExploitInterface) and plugin_class.is_valid():
                plugin_class_list.append(plugin.init())
        except Exception as exception:
            print(f"Error importing plugin {plugin}: {exception}")
    return plugin_class_list

def print_available_plugins(plugins: List[StrapiExploitInterface]) -> None:
    '''Print available plugins.'''
    console = Console()
    table = Table(show_header=True, header_style="bold red", box=SIMPLE)
    table.add_column("ID", width=5, style="yellow")
    table.add_column("Name", width=25)
    table.add_column("Description")
    for plugin in plugins:
        table.add_row(str(plugins.index(plugin) + 1), plugin.get_name(), plugin.get_description())
    console.print(table, justify="center")

def choose_plugin(plugins: List[StrapiExploitInterface]) -> None:
    '''Choose a plugin to run.'''
    while True:
        choice = Prompt.ask("[bold magenta]Strapwn[/bold magenta] > ", default="?")
        if choice == "exit":
            logger.info("Goodbye !")
            exit(0)
        elif choice == "?" or choice == "help":
            cls()
            display_motd()
            print_available_plugins(plugins)
            continue
        else:
            try:
                choice = int(choice)
                if choice > len(plugins):
                    logger.error("Plugin doesn't exist.")
                    continue
            except ValueError:
                logger.error("Invalid input.")
                continue
            try:
                cls()
                display_motd()
                console = Console()
                console.print(f"[bold red]Strapwn[/bold red] > [bold yellow]{plugins[choice - 1].get_name()}[/bold yellow]\n\n", justify="center")
                plugins[choice - 1].run()
            except Exception as exception:
                logger.error(f"Unhandled error: {exception.__class__.__name__}")
                continue