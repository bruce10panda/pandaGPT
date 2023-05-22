import openai

# Step 1: Install the OpenAI library
# pip install openai

# Step 2: Set up your OpenAI API key
openai.api_key = 'YOUR_API_KEY'  # Replace with your OpenAI API key

# Step 3: Create a function to send a message to the chatbot and receive a response
def ask_chatbot(message):
    response = openai.Completion.create(
        engine='davinci',  # Choose the language model (e.g., davinci, curie, etc.)
        prompt=message,
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Example usage
user_input = input("You: ")

while user_input.lower() != 'bye':
    response = ask_chatbot(user_input)
    print("Chatbot:", response)
    user_input = input("You: ")
