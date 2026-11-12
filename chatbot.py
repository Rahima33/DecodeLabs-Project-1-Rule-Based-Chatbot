
import string

RESPONSES = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm a program, so I'm obviously running fine. How are you?",
    "what is your name": "I'm D-codeBot, a rule-based chatbot.",
    "whats your name": "I'm D-codeBot, a rule-based chatbot.",
    "what can you do": "I can greet you and answer a few predefined questions.",
    "who made you": "I was built by Rahima for Project 1 of the DecodeLabs AI internship.",
    "thanks": "You're welcome!",
    "help": "Try: hello, how are you, what is your name, what can you do. Type 'bye' to exit.",
}

# Commands used to terminate the chatbot
EXIT_COMMANDS = {"bye", "exit", "quit", "goodbye"}

# Default response for unrecognised inputs
FALLBACK = "I do not understand. Type 'help' to see what I can answer."


def sanitize(text):
    """Normalize case, whitespace and punctuation."""
    text = " ".join(text.lower().split())
    return text.translate(
        str.maketrans("", "", string.punctuation)
    )


def main():
    print("=" * 50)
    print("D-codeBot: Hello! Welcome to DecodeLabs AI Chatbot.")
    print("Type 'help' for available options or 'bye' to exit.")
    print("=" * 50)

    # Continuous conversation loop
    while True:
        user_input = sanitize(input("\nYou: "))

        # Handle empty input
        if not user_input:
            print("D-codeBot: Please enter a message.")
            continue

        # Handle exit commands
        if user_input in EXIT_COMMANDS:
            print("D-codeBot: Goodbye! Have a great day.")
            break

        # Retrieve response or display fallback
        response = RESPONSES.get(user_input, FALLBACK)
        print("D-codeBot:", response)


if __name__ == "__main__":
    main()
