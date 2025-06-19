import json
import os
from datetime import datetime

MEMORY_FILE = "data/user_memory.json"

# Ensure memory file exists
def init_memory():
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'w') as f:
            json.dump({"user_notes": []}, f)

# Add a memory note
def store_memory(note: str):
    init_memory()
    with open(MEMORY_FILE, 'r+') as f:
        data = json.load(f)
        timestamped_note = {
            "timestamp": datetime.now().isoformat(),
            "note": note
        }
        data["user_notes"].append(timestamped_note)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

# Retrieve all notes
def retrieve_memory():
    init_memory()
    with open(MEMORY_FILE, 'r') as f:
        return json.load(f)["user_notes"]

# Example usage
if __name__ == "__main__":
    store_memory("User said they want to get fit before August.")
    store_memory("User skipped gym on Monday.")
    
    print("EGO SHIFT™ Memory Recall:\n")
    for m in retrieve_memory():
        print(f"[{m['timestamp']}] {m['note']}")
