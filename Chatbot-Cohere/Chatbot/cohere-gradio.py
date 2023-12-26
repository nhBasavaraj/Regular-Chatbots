import gradio as gr
import cohere

# Cohere API key
cohere_key = 'OyjmiSGIOTWSxwyP2sPxhzUKi7WYP6KwUqPG5N3N'
co = cohere.Client(cohere_key)

# Initialize the conversation history
conversation_history = []

# Gradio interface for the chatbot
def chatbot_interface(user_prompt):
    # Cohere API call
    response = co.generate(
        model='command-nightly',
        prompt=user_prompt,
        max_tokens=300,
        temperature=0.9,
        k=0,
        p=0.75,
        stop_sequences=[],
        return_likelihoods='NONE'
    )

    # Append the current conversation to the history
    conversation_history.append({"user": user_prompt, "bot": response.generations[0].text})

    # Format the conversation for display
    display_conversation = ""
    for conv in reversed(conversation_history):
        display_conversation += f"User 👨‍🦱: {conv['user']}\nBot 🤖: {conv['bot']}\n----------------\n"

    return display_conversation.strip()

# Add a headline to the Gradio interface
iface = gr.Interface(fn=chatbot_interface, inputs="text", outputs="text", title="Cohere Chatbot 🤖 ")
iface.launch(share=True)
