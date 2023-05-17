![strapwn_logo.png](./assets/strapwn_logo.png)


# **🚀** Description


Strapwn is a tool designed to automate the exploitation of Strapi websites.

# 🐍 Requirements


- Python 3.8

# 📔 Usage


```bash
python3 strapwn.py
```

# ⚙️ Plugins


With Strapwn, you can create your own automation plugins by following these steps:

1. Create a new Python file in the "plugins" folder.
2. Import the StrapiExploitInterface and implement your logic.

```python
from strapi_exploit import StrapiExploitInterface

class MyStrapiExploit(StrapiExploitInterface):
    def __init__(self):
        super().__init__("CVE-XXXX-XXXX", "MyStrapiExploit description")
    def run(self) -> bool:
        '''This method is called when the exploit is selected.'''
        self.info("MyStrapiExploit is running")
        return True

def init():
    return MyStrapiExploit()
```

## 📚 Documentation


Method and class documentation is available in the [StrapiExploitInterface](./strapi_exploit.py) file.

```python
    def run(self) -> bool:
        '''Run the plugin. Returns True if successful, False if not.'''
    def get_name(self) -> str:
        '''Get the name of the plugin.'''
    def get_description(self) -> str:
        '''Get the description of the plugin.'''
    def is_valid(self) -> bool:
        '''Check if the plugin is valid.'''
    def get_strapi_version(self, url: str) -> str:
        '''Get the version of Strapi.'''
    def input(self, prompt: str) -> str:
        '''Get input from the user.'''
    def display(self, text: str) -> None:
        '''Display text to the user.'''
    def success(self, text: str) -> None:
        '''Display success message to the user.'''
    def error(self, text: str) -> None:
        '''Display error message to the user.'''
    def warning(self, text: str) -> None:
        '''Display warning message to the user.'''
    def info(self, text: str) -> None:
        '''Display info message to the user.'''

    # NEW

    def input_default(self, prompt: str, default: str) -> str:
        '''Get input from the user with a default value.'''
    def get_random_email(self) -> str:
        '''Get a random email.'''
    def get_random_password(self) -> str:
        '''Get a random password.'''
    def get_random_username(self) -> str:
        '''Get a random username.'''
    def get_admin_token(self, url: str, email: str, password: str) -> str:
        '''Get the admin token.'''
```

🌝 If you would like to share your plugin with the community, simply make a pull request!

# ⚠️ Disclaimer


Please note that this tool is intended for educational purposes only, and I cannot be held responsible for any misuse of it.

# 🤝 Contributing


<a href="https://github.com/Axel672"><img src="https://github.com/Axel672.png" width="50"></a>
<a href="https://github.com/sofianeelhor"><img src="https://github.com/sofianeelhor.png" width=50></a>
<a href="https://github.com/TomF0x"><img src="https://github.com/TomF0x.png" width=50></a>

We welcome your suggestions and look forward to hearing from you.
## 🍀 Thanks and have fun !
