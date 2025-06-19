import random
import datetime

# Pre-defined mission categories and examples
MISSION_LIBRARY = {
    "fitness": [
        "Do 50 pushups before 10 AM",
        "Stretch for 10 minutes after waking up",
        "Drink 2 liters of water by 6 PM"
    ],
    "discipline": [
        "No social media for the next 4 hours",
        "Write down 3 priorities for tomorrow",
        "Clean your workspace before 5 PM"
    ],
    "mindset": [
        "Watch one motivational video before bed",
        "Journal for 10 minutes after lunch",
        "Repeat your core goals aloud in the mirror"
    ],
    "appearance": [
        "Iron your shirt for tomorrow",
        "Shave/edge up your beard before bed",
        "Pick tomorrow’s outfit in advance"
    ]
}

# Generates a daily mission set
def generate_daily_missions(user_goals: list) -> dict:
    today = datetime.date.today().isoformat()
    mission_set = {}

    for category in user_goals:
        if category in MISSION_LIBRARY:
            mission_set[category] = random.choice(MISSION_LIBRARY[category])

    return {
        "date": today,
        "missions": mission_set
    }

# Example usage
if __name__ == "__main__":
    sample_goals = ["fitness", "discipline", "appearance"]
    missions = generate_daily_missions(sample_goals)
    print("EGO SHIFT™ Daily Mission Set:\n")
    for cat, task in missions["missions"].items():
        print(f"[{cat.upper()}] {task}")
