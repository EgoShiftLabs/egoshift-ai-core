Filename: core/goals.py

import json import os from datetime import datetime

GOALS_FILE = "data/user_goals.json"

Ensure the goals file exists

def init_goals(): if not os.path.exists(GOALS_FILE): with open(GOALS_FILE, 'w') as f: json.dump({"goals": []}, f)

Add a new goal to the tracker

def add_goal(title: str, category: str): init_goals() with open(GOALS_FILE, 'r+') as f: data = json.load(f) goal = { "title": title, "category": category, "created": datetime.now().isoformat(), "status": "active" } data["goals"].append(goal) f.seek(0) json.dump(data, f, indent=4) f.truncate()

Mark a goal as completed or failed

def update_goal_status(title: str, new_status: str): init_goals() with open(GOALS_FILE, 'r+') as f: data = json.load(f) for goal in data["goals"]: if goal["title"] == title: goal["status"] = new_status break f.seek(0) json.dump(data, f, indent=4) f.truncate()

Retrieve current goals list

def get_goals(): init_goals() with open(GOALS_FILE, 'r') as f: return json.load(f)["goals"]

Example usage

if name == "main": add_goal("Lose 10 pounds by August", "fitness") add_goal("Write a journal entry every day", "mindset") update_goal_status("Lose 10 pounds by August", "completed")

print("EGO SHIFT™ Goal Log:\n")
for g in get_goals():
    print(f"- [{g['status'].upper()}] {g['title']} ({g['category']})")

