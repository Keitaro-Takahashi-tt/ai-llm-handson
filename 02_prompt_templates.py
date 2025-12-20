
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
  ("system","あなたは{role}です。"),
  ("user","{input}")
])

llm = ChatOllama(
  model="llama3.2:1b",
  temperature=0.5)

prompt = template.format_messages(
  role ="AI特化のエキスパート",
  input="AI領域におけるLangChainの概念を簡潔に説明してください。"
)

response = llm.invoke(prompt)
print(f"AI: {response.content}")
