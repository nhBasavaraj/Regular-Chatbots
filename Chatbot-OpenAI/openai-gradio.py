import gradio as gr
import requests

# OpenAI GPT-3 Chatbot
def generate_response(prompt):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {"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"}'
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()
    completion = response_data['choices'][0]['message']['content'] if 'choices' in response_data else 'No completion available'
    return completion

def chatbot_interface(prompt):
    output = generate_response(prompt)
    return f"👤 You: {prompt}\n🤖 Bot: {output}\n----------------------"

iface = gr.Interface(fn=chatbot_interface, inputs="text", outputs="text", title="OpenAI Chatbot 🤖 ")
iface.launch(share=True)

