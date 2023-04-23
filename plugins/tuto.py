from strapi_plugin import StrapiExploitInterface

class MyStrapiExploit(StrapiExploitInterface):
    def __init__(self):
        super().__init__("MyStrapiExploit", "MyStrapiExploit description")
    def run(self) -> bool:
        print("MyStrapiExploit running...")
        return True

def init():
    return MyStrapiExploit()