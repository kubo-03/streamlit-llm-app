import streamlit as st
from langchain_openai import ChatOpenAI

from langchain.schema import SystemMessage, HumanMessage, AIMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

messages = [

    SystemMessage(content="You are a helpful assistant."),

    HumanMessage(content="私の名前は大久保雅子です"),

    AIMessage(content="大久保雅子です"),

    HumanMessage(content="私の名前が分かりますか？"),

]

result = llm(messages)

st.write(result.content)

st.divider()
