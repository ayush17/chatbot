from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchai_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv