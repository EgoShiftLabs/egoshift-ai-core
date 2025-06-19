Filename: core/wallet.py

import json import os from datetime import datetime

WALLET_FILE = "data/user_wallet.json"

Initialize wallet if it doesn't exist

def init_wallet(): if not os.path.exists(WALLET_FILE): with open(WALLET_FILE, 'w') as f: json.dump({ "balance": 0, "transaction_log": [] }, f)

Add tokens to the wallet (for completed actions)

def reward_tokens(amount: int, reason: str): init_wallet() with open(WALLET_FILE, 'r+') as f: data = json.load(f) data["balance"] += amount data["transaction_log"].append({ "type": "reward", "amount": amount, "reason": reason, "timestamp": datetime.now().isoformat() }) f.seek(0) json.dump(data, f, indent=4) f.truncate()

Subtract tokens (for redemptions or infractions)

def spend_tokens(amount: int, reason: str): init_wallet() with open(WALLET_FILE, 'r+') as f: data = json.load(f) if data["balance"] >= amount: data["balance"] -= amount data["transaction_log"].append({ "type": "spend", "amount": amount, "reason": reason, "timestamp": datetime.now().isoformat() }) f.seek(0) json.dump(data, f, indent=4) f.truncate() else: raise ValueError("Insufficient balance")

Get current wallet state

def get_wallet(): init_wallet() with open(WALLET_FILE, 'r') as f: return json.load(f)

Example usage

if name == "main": reward_tokens(10, "Completed morning workout") reward_tokens(5, "Logged daily journal") spend_tokens(7, "Accessed premium AI insight")

print("\nEGO SHIFT™ WALLET:")
print(json.dumps(get_wallet(), indent=4))

