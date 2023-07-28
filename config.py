import json

RPC = ["https://rpc.ankr.com/optimism"]

with open("accounts.txt", "r") as file:
    ACCOUNTS = [row.strip() for row in file]

with open("data/omnix_abi.json", "r") as file:
    OMNIX_ABI = json.load(file)

OMNIX_CONTRACT = "0xd12999440402d30f69e282d45081999412013844"

CHAIN_ID = {
    "binance": 102,
    "avalanche": 106,
    "polygon": 109,
    "arbitrum": 110,
    "fantom": 112,
    "moonbeam": 126,
    "metis": 151,
    "gnosis": 145,
    "nova": 175,
}
