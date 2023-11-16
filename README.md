# Palm-2 Streamlit Chatbot

## Overview

This repository contains a simple chatbot powered by the Palm-2 API and deployed as a Streamlit app. The chatbot engages in natural language conversations and utilizes the Palm-2 language model.

## Features

- **Conversational AI:** Engage in natural language conversations with the Palm-2 Streamlit Chatbot.
- **Streamlit Interface:** Deployed as a Streamlit app, providing a user-friendly interface for interaction.
- **Conversation History:** Keep track of your conversation with the chatbot in a convenient history display.

## Prerequisites

- Python 3.8 or above
- Palm-2 API key (Get it from [Palm-2](https://makersuite.google.com/app/apikey))
- Streamlit (Install using `pip install streamlit`)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/palm-2-streamlit-chatbot.git
    cd palm-2-streamlit-chatbot
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

3. **Set Palm-2 API Key:**
   - Open the `palm-bot.py` file in a text editor.
   - Replace `'YOUR_PALM_2_API_KEY'` with your actual Palm-2 API key.

4. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

5. **Interact with the chatbot:**
   Open your web browser and navigate to the provided local address (usually http://localhost:8501). Enter prompts and receive natural language responses from the Palm-2 Chatbot.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [Palm-2](https://makersuite.google.com/app/home)
