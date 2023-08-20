import json

with open('data/rpc.json') as file:
    RPC = json.load(file)

with open("accounts.txt", "r") as file:
    ACCOUNTS = [row.strip() for row in file]

with open("data/omnix_abi.json", "r") as file:
    OMNIX_ABI = json.load(file)

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
    "base": 184,
    "polygon_zkevm": 158,
}
