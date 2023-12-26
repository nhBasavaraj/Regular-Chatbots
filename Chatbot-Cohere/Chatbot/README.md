# Cohere Chatbot

## Overview

This folder contains a simple chatbot powered by the Cohere API and deployed as a Streamlit app & a Gradio interface. The chatbot engages in natural language conversations and utilizes the Cohere language model.

## Features

- **Conversational AI:** Engage in natural language conversations with the Cohere Chatbot.
- **User-Friendly Interface:** Choose between the Streamlit app or the Gradio interface for a seamless user experience.
- **Conversation History:** Keep track of your conversation with the chatbot in a convenient history display.

## Prerequisites

- Python 3.8 or above
- Cohere API key (Get it from [Cohere](https://dashboard.cohere.com/api-keys))
- Streamlit (Install using `pip install streamlit`)
- Gradio (Install using `pip install gradio`)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/cohere-chatbot.git
    cd cohere-chatbot
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

3. **Set Cohere API Key:**
   - Open the `cohere-bot.py` file in a text editor.
   - Replace `'YOUR_COHERE_API_KEY'` with your actual Cohere API key.

### Streamlit Deployment

4. **Run the Streamlit app:**
    ```bash
    streamlit run streamlit_bot.py
    ```

5. **Interact with the chatbot:**
   Open your web browser and navigate to the provided local address (usually http://localhost:8501). Enter prompts and receive natural language responses from the Cohere Chatbot.

### Gradio Deployment

4. **Run the Gradio interface:**
    ```bash
    python gradio_bot.py
    ```

5. **Visit the Gradio Interface:**
   Open your web browser and navigate to the provided local address (usually http://localhost:7860). Engage in conversations with the chatbot using the intuitive Gradio interface.

## Dependencies

- [Cohere](https://cohere.com/)
- [Streamlit](https://streamlit.io/) (for Streamlit deployment)
- [Gradio](https://www.gradio.app/) (for Gradio deployment)
