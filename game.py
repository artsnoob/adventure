import openai

# Initialize the OpenAI API client
openai.api_key = 'ADD YOUR OWN GPT API HERE'

def generate_adventure(session_messages):
    """
    Use the OpenAI API's chat model to generate the next part of the adventure,
    maintaining the context of the adventure.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=session_messages
    )
    return response.choices[0].message['content'].strip()

def adventure_game():
    # Session messages to maintain the conversation context
    session_messages = [
        {"role": "system", "content": "You are a wise guide helping an adventurer navigate a mystical forest."}
    ]
    
    print("\nYou stand at the edge of a mystical forest. This is the start of your adventure.")
    
    while True:
        print()  # Ensures an empty line before the input prompt
        choice = input("What would you like to do? : ").lower()
        
        if choice == "quit":
            print("\nYou've chosen to end your adventure. Goodbye!")
            break

        # Update the session context with the user's choice
        session_messages.append({"role": "user", "content": choice})

        # Generate the adventure dynamically based on the player's choice, with context
        adventure_text = generate_adventure(session_messages)
        
        # Update the session context with the API's response
        session_messages.append({"role": "assistant", "content": adventure_text})

        print("\n" + adventure_text)

if __name__ == "__main__":
    adventure_game()
