# Cohere Document Q&A Streamlit Bot

## Overview

This folder contains a document question and answer (Q&A) bot powered by the Cohere API and deployed as a Streamlit app. The bot allows users to upload a PDF document and ask questions, receiving relevant answers based on the document's content.

## Features

- **Document Q&A:** Upload a PDF document and ask questions to receive accurate and contextual answers.
- **Streamlit Interface:** Deployed as a Streamlit app for an interactive and user-friendly experience.
- **Conversation History:** Track and display previous conversations, including user queries and bot responses.

## Prerequisites

- Python 3.8 or above
- Cohere API key (Obtain it from [Cohere](https://dashboard.cohere.com/api-keys))
- Streamlit (Install using `pip install streamlit`)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/cohere-document-qa-streamlit-bot.git
    cd cohere-document-qa-streamlit-bot
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

3. **Set Cohere API Key:**
   - Open the `doc-Q&A-cohere-bot.py` file in a text editor.
   - Replace `'YOUR_COHERE_API_KEY'` with your actual Cohere API key.

4. **Run the Streamlit app:**
    ```bash
    streamlit run cohere_doc_bot.py
    ```

5. **Interact with the document Q&A bot:**
   Open your web browser and navigate to the provided local address (usually http://localhost:8503). Upload a PDF document, ask questions, and receive answers based on the document's content.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [Cohere](https://cohere.com/)
- [LangChain](https://github.com/langchain-ai/langchain)

## Configuration

Ensure that you set up your Cohere API key by replacing the placeholder in the code with your actual API key.

```python
cohere_api_key = 'YOUR_COHERE_API_KEY'
embeddings = CohereEmbeddings(cohere_api_key=cohere_api_key)

