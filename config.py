import json

RPC = ["https://rpc.ankr.com/optimism"]

with open("accounts.txt", "r") as file:
    ACCOUNTS = [row.strip() for row in file]

with open("data/omnix_abi.json", "r") as file:
    OMNIX_ABI = json.load(file)

OMNIX_CONTRACT = "0x012caeb558dffc053a6a092835a1e7f5c8eeba8b"

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
}
