from core.mission_engine import assign_mission
from core.memory import store_memory, retrieve_memory
from core.goals import add_goal, update_goal_status, get_goals
from core.wallet import reward_tokens, spend_tokens, get_wallet

def main():
    print("\nWelcome to EGO SHIFT™ — Your Second Consciousness\n")

    # Assign today's mission
    mission = assign_mission()
    print(f"Today's Mission: {mission['description']} [Category: {mission['category']}]\n")

    # Simulate mission completion
    user_input = input("Did you complete this mission? (yes/no): ").strip().lower()
    if user_input == "yes":
        store_memory(f"User completed mission: {mission['description']}")
        reward_tokens(10, f"Completed mission: {mission['description']}")
        print("\n💰 +10 $SHIFT tokens awarded!")
    else:
        store_memory(f"User skipped mission: {mission['description']}")
        print("\n⏳ No tokens earned. Try again tomorrow.")

    # Show current wallet state
    print("\n🔐 Your Wallet:")
    wallet = get_wallet()
    print(f"Balance: {wallet['balance']} $SHIFT")

    # List past memory logs
    print("\n🧠 Recent Memory:")
    for note in retrieve_memory()[-3:]:
        print(f"[{note['timestamp']}] {note['note']}")

    # Show current goals
    print("\n🎯 Active Goals:")
    for g in get_goals():
        if g['status'] == 'active':
            print(f"- {g['title']} ({g['category']})")

if __name__ == "__main__":
    main()
