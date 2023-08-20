RANDOM_WALLET = False

#################
IS_SLEEP = False

SLEEP_FROM = 100  # second
SLEEP_TO = 300  # second
#################

SLEEP_BRIDGE = 15  # second
AMOUNT = 1  # quantity mint and bridge

OMNIX_CONTRACT = "0x061A883E8c2FEFFB4F3eA42046ABD4bE88E1333f"

SOURCE_CHAIN = "base"

BRIDGE_CHAIN = [
    # "test" comment the line if you don't need
    # "binance", don't work in this contract
    # "avalanche", don't work in this contract
    # "polygon", don't work in this contract
    # "arbitrum", don't work in this contract
    # "fantom", don't work in this contract
    # "moonbeam", don't work in this contract
    # "base",
    "metis",
    # "gnosis", don't work in this contract
    # "nova", don't work in this contract
    "zk_evm"
]
