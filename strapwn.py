''' Main file for the Strapwn tool'''
from strapi_plugin import load_plugins, import_plugins, print_available_plugins, choose_plugin
from utility import display_motd, cls
from logger import logger

if __name__ == "__main__":
    try:
        display_motd()
        plugins = import_plugins(load_plugins())
        print_available_plugins(plugins)
        choose_plugin(plugins)
    except KeyboardInterrupt:
        cls()
        display_motd()
        logger.info("Goodbye !")
