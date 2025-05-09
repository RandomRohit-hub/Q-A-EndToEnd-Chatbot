# 💬 Conversational Q&A Chatbot with Streamlit and OpenAI

This project is a conversational Q&A chatbot web application built using **Streamlit**, **OpenAI GPT models**, and **LangChain**. It allows users to ask questions and get AI-generated responses while customizing parameters like model selection, creativity (temperature), and max token limits.

---

## 🚀 Features

- 🔐 API key-based access to OpenAI models
- 🤖 Support for GPT-4, GPT-4-turbo, and GPT-4o
- 🔄 Conversational context handling using LangChain
- 🎛️ User-configurable temperature and token limit
- 🖼️ Interactive web UI powered by Streamlit

---

## 🧰 Tech Stack & Libraries Used

| Library             | Purpose                                                                 |
|---------------------|-------------------------------------------------------------------------|
| `streamlit`         | For creating the interactive web interface                              |
| `openai`            | To access OpenAI models using API keys                                  |
| `langchain_openai`  | LangChain wrapper for OpenAI LLMs                                       |
| `langchain_core`    | For chaining prompts and parsing outputs                                |
| `dotenv`            | To load environment variables securely                                  |

---

## 🏗️ How It Works

1. **Prompt Template**: A chat prompt template defines how user input is presented to the LLM.
2. **Model Selection**: The user selects from available OpenAI models (e.g., `gpt-4`, `gpt-4o`, etc.).
3. **LangChain Pipeline**: The system constructs a chain with `PromptTemplate -> LLM -> OutputParser`.
4. **Streamlit Interface**: Users interact with the chatbot via an easy-to-use web UI with sliders and input fields.

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name



