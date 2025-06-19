# EGO SHIFT™ AI CORE - LangChain Assistant (v0.1)
# Filename: main.py

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage

# Initialize memory for tracking conversation
memory = ConversationBufferMemory()

# System message to shape AI behavior
system_prompt = SystemMessage(
    content=(
        "You are the voice of the EGO SHIFT protocol — a smart, brutally honest, goal-oriented life coach. "
        "Your job is to guide users toward self-mastery by helping them make better decisions in real time. "
        "Be direct, tactical, motivational, and hold them accountable."
    )
)

# Set up the core AI assistant using OpenAI (or other backend)
llm = ChatOpenAI(temperature=0.3, model="gpt-4")

chain = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Run basic interaction loop (to be replaced with app UI or API hook)
def main():
    print("Welcome to EGO SHIFT™: AI Mode Activated")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("EGO SHIFT terminated.")
            break
        response = chain.run(input=user_input)
        print(f"EGO SHIFT: {response}\n")

if __name__ == "__main__":
    main()
