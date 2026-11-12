# D-codeBot

D-codeBot is a small, command-line rule-based chatbot created for Project 1 of the DecodeLabs AI internship. It responds to a set of predefined phrases and demonstrates a simple conversation loop in Python.

## Features

- Recognizes greetings and a few common questions.
- Normalizes input by ignoring capitalization, extra whitespace, and punctuation.
- Shows a help message for supported topics.
- Keeps chatting until you enter an exit command.
- Gives a helpful fallback when it does not recognize a message.

## Requirements

- Python 3
- No third-party packages are required.

## Run the chatbot

Open a terminal in the project folder and run:

```bash
python chatbot.py
```

On some systems, use `python3 chatbot.py` instead.

## Example

```text
D-codeBot: Hello! Welcome to DecodeLabs AI Chatbot.
Type 'help' for available options or 'bye' to exit.

You: HI!
D-codeBot: Hello! What can I do for you?

You: what can you do?
D-codeBot: I can greet you and answer a few predefined questions.

You: bye
D-codeBot: Goodbye! Have a great day.
```

## What it can answer

Try `hello`, `hi`, `how are you`, `what is your name`, `what can you do`, `who made you`, `thanks`, or `help`. Enter `bye`, `exit`, `quit`, or `goodbye` to end the conversation. Input matching is based on the cleaned-up whole message, so unlisted phrases receive the fallback response.

## How it works

The `sanitize` function lowercases each message, collapses repeated whitespace, and removes punctuation. The chatbot then checks the cleaned message against the `RESPONSES` dictionary. Exit commands are handled separately, and messages without a matching rule receive the `FALLBACK` response.

To add a response, add a phrase and its reply to `RESPONSES` in `chatbot.py`. To change how the chatbot exits or handles unknown messages, update `EXIT_COMMANDS` or `FALLBACK`.

## Project structure

```text
.
├── chatbot.py
└── README.md
```
