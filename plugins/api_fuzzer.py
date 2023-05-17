from os.path import exists
from multiprocessing import Pool
import requests
from strapi_exploit import StrapiExploitInterface
from logger import logger

class ApiFuzzer(StrapiExploitInterface):
    '''Strapi API Fuzzer'''
    def __init__(self):
        super().__init__("API Fuzzer", "Find API endpoints")
    def run(self) -> bool:
        url = self.input("URL of the Strapi API (https://example.com/api)")
        if url[-1] == "/":
            url = url[:-1]
        r = requests.get(f"{url}/users" , timeout=10)
        if not r.status_code == 200 and not r.status_code == 403:
            self.error("Invalid API URL")
            return False
        wordlist = self.input_default("Wordlist file", "./assets/list.txt")
        if exists(wordlist) is False:
            self.error("Wordlist file does not exist")
            return False
        wordlist = [i.strip() for i in open(wordlist, "r", encoding="latin-1").readlines()]
        thread = self.input_default("Number of threads (default=10)", 10)
        try:
            thread = int(thread)
        except ValueError:
            self.error("Invalid thread number")
            return False
        self.info(f"Loaded {len(wordlist)} words - {thread} threads")
        run(url, wordlist, thread)

def check(url: str, word: str) -> None:
    '''Check if the password is correct'''
    r = requests.get(f"{url}/{word}", timeout=10)
    if r.status_code != 404:
        logger.display(f"[+][{r.status_code}] - /{word}")


def run(url: str, wordlist: list, thread: int) -> None:
    '''Run the bruteforce'''
    pool = Pool(thread)
    for word in wordlist:
        pool.apply_async(check, args=(url, word))
    pool.close()
    pool.join()

def init():
    return ApiFuzzer()