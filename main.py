import random
import time

from modules import Omnix
from config import ACCOUNTS
from settings import RANDOM_WALLET, SLEEP_TO, SLEEP_FROM, IS_SLEEP, AMOUNT


def main():
    if RANDOM_WALLET:
        random.shuffle(ACCOUNTS)

    for j, key in enumerate(ACCOUNTS):
        omnix = Omnix(key)
        omnix.bridge(AMOUNT)

        if j + 1 < len(ACCOUNTS) and IS_SLEEP:
            time.sleep(random.randint(SLEEP_FROM, SLEEP_TO))


if __name__ == '__main__':
    print("\n\n Subscribe to me – https://t.me/sybilwave\n\n")
    main()
    print("\n\n Subscribe to me – https://t.me/sybilwave\n\n")
