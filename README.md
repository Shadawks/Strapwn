# ReadMe

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
from strapi_plugin import StrapiExploitInterface

class MyStrapiExploit(StrapiExploitInterface):
    def __init__(self):
        super().__init__("CVE-XXXX-XXXX", "MyStrapiExploit description")
    def run(self) -> bool:
        print("MyStrapiExploit running...")
        return True

def init():
    return MyStrapiExploit()
```

🌝 If you would like to share your plugin with the community, simply make a pull request!

## ⚠️ Disclaimer

---

Please note that this tool is intended for educational purposes only, and I cannot be held responsible for any misuse of it.

---

We welcome your suggestions and look forward to hearing from you.
### 🍀 Thanks and have fun !