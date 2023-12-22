# Jina Embeddings Streamlit ChatBot

## Overview

This repository contains a chatbot that utilizes Jina embeddings for embedding words or sentences. The chatbot is deployed as a Streamlit app, providing a user-friendly interface for interacting with the Jina embeddings.

## Features

- **Embedding Words/Sentences:** Use the Jina embeddings to embed words or sentences for various natural language processing tasks.
- **Streamlit Interface:** The chatbot is deployed as a Streamlit app, providing an intuitive interface for embedding operations.
- **Conversation History:** Keep track of your embedding requests with the chatbot through a convenient history display.

## Prerequisites

- Python 3.8 or above
- Jina API key (Get it from [Jina](https://jina.ai/embeddings/))
- Streamlit (Install using `pip install streamlit`)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/jina-embeddings-streamlit-chatbot.git
    cd jina-embeddings-streamlit-chatbot
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

3. **Set Jina API Key:**
   - Open the `jina-bot.py` file in a text editor.
   - Replace `'JINA_API_KEY'` with your actual Jina API key.

4. **Run the Streamlit app:**
    ```bash
    streamlit run jina-bot.py
    ```

5. **Interact with the chatbot for embeddings:**
   Open your web browser and navigate to the provided AWS Studio URL, removing any trailing parameters (e.g., "lab?") after the default, and then append /proxy/8501(port number)/ to the end. The URL format should look like this: https://{NOTEBOOK_URL}/proxy/8501/.(This Instructions is only for AWS studio). Enter words or sentences to receive Jina embeddings.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [Jina](https://jina.ai/)

