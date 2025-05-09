import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

# LangSmith tracking setup
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACKING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = "Q&A E2E"

# Chat prompt template
prompt = ChatPromptTemplate.from_messages([
    ('system', "You are a helpful assistant. Follow the user command and answer the user queries."),
    ('user', "Question: {question}")
])

# Response generator function
def generate_response(question, api_key, llm_model, temperature, max_tokens):
    openai.api_key = api_key
    llm = ChatOpenAI(model=llm_model, temperature=temperature, max_tokens=max_tokens)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer



import streamlit as st

st.set_page_config(page_title="OpenAI Chat", page_icon="💬")

# Sidebar for settings
st.sidebar.title("🔧 Settings")
api_key = st.sidebar.text_input("🔑 Enter your OpenAI API Key:", type="password", help="Paste your OpenAI secret key here.")

engine = st.sidebar.selectbox(
    "🤖 Select OpenAI Model",
    ["gpt-4o", "gpt-4-turbo", "gpt-4"],
    help="Choose which GPT model to use."
)

temperature = st.sidebar.slider("🌡️ Temperature", min_value=0.0, max_value=1.0, value=0.7,
                                help="Controls creativity. Lower is more focused, higher is more random.")
max_tokens = st.sidebar.slider("🧠 Max Tokens", min_value=50, max_value=300, value=150,
                               help="Maximum length of the response.")

# Main interface
st.title("💬 Chat with OpenAI")
st.markdown("Type your question below and get answers from your selected OpenAI model.")

user_input = st.text_input("📝 You:", placeholder="Ask anything...")

if user_input and api_key:
    with st.spinner("Thinking..."):
        response = generate_response(user_input, api_key, engine, temperature, max_tokens)
    st.chat_message("assistant").write(response)

elif user_input:
    st.warning("⚠️ Please enter your OpenAI API Key in the sidebar.")

else:
    st.info("ℹ️ Waiting for your input...")

# Optional: footer or instructions
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and OpenAI")

























