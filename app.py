import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate


import os
from dotenv import load_dotenv

load_dotenv()


## langsmith track

os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACKING_V2']="true"
os.environ['LANGCHAIN_PROJECT']="Q&A E2E"

## prompt temp

prompt=ChatPromptTemplate.from_messages(
    [
        ('system',"you are a helpful assistant follow the user command and answer the user queries")
        ("user","Question;{question}")
    ]
)

