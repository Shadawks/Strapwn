import os, importlib, requests
from typing import List
from json import JSONDecodeError

class StrapiExploitInterface:
    ''''Interface for Strapi Exploit'''
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    def run(self) -> bool:
        '''Run the plugin. Returns True if successful, False if not.'''
        pass
    def get_name(self) -> str:
        '''Get the name of the plugin.'''
        return self.name
    def get_description(self) -> str:
        '''Get the description of the plugin.'''
        return self.description
    def is_valid(self) -> bool:
        '''Check if the plugin is valid.'''
        if self.name != "" and self.description != "":
            return True
        else:
            return False
    def get_strapi_version(self, url: str) -> str:
        '''Get the version of Strapi.'''
        try:
            version = requests.get(f"{url}/admin/init").json()["data"]["strapiVersion"]
            return version
        except JSONDecodeError:
            try:
                version = requests.get(f"{url}/admin/strapiVersion").json()["strapiVersion"]
                return version
            except JSONDecodeError:
                return ""

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
        except Exception as e:
            print(f"Error importing plugin {plugin}: {e}")
    return plugin_class_list

def print_available_plugins(plugins: List[StrapiExploitInterface]) -> None:
    '''Print available plugins.'''
    for plugin in plugins:
        print(f"{plugins.index(plugin) + 1}. [{plugin.get_name()}] - {plugin.get_description()}")

def choose_plugin(plugins: List[StrapiExploitInterface]) -> None:
    '''Choose a plugin to run.'''
    while True:
        try:
            choice = input("[>] Select a plugin to run: ")
            if choice == "exit":
                print("[!] Exiting...")
                exit(0)
            if choice == "?" or choice == "help":
                print_available_plugins(plugins)
                continue
            choice = int(choice)
            if choice > len(plugins):
                print("[!] Plugin doesn't exist.")
            else:
                print("-" * 20)
                plugins[choice - 1].run()
                print("-" * 20)
        except ValueError:
            print("[!] Plugin doesn't exist.")