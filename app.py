from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI, OpenAI

from langchain.schema import SystemMessage, HumanMessage, AIMessage

# load_dotenv()  # .env ファイルから環境変数を読み込む
# 
# client = OpenAI()  # .env の OPENAI_API_KEY を使う

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

#質問を回答するLLM

input_text = st.text_input(label="`質問を入力してください`")
    
selected_item = st.radio(
    "専門家を選択してください",
    ["健康に関する専門家", "教育に関する専門家"]
)

messages = [

    SystemMessage(content=f"あなたは{selected_item}です。質問に答えてください。"),

    HumanMessage(content=input_text),

]

result = llm(messages)

st.write(result.content)

st.divider()
