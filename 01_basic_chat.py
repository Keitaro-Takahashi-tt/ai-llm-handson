from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

# llmって実際どういう動きをしているのかを調べる
#　temperatureの影響とかも見てみる
llm=ChatOllama(
  model="llama3.2:1b",
  temperature=0.7
)

# SystemMessageがllmのなかでどういう働きをしているのか知りたい
# ふるまいなどを決めると記載あるが、具体的にどういう影響を与えるのか
messages=[
  SystemMessage(content="You are a helpful AI assistant. Answer concisely in Japanese."),
  HumanMessage(content="LangChainの概念を簡潔に説明してください。")
]

response=llm.invoke(messages)
print(f"AI: {response.content}")

print("\n=== temperature = 0.0 (決定的) ===")
llm_low = ChatOllama(model="llama3.2:1b", temperature=0.0)
response_low = llm_low.invoke([HumanMessage(content="こんにちは")])
print(response_low.content)

print("\n=== temperature = 1.0 (創造的) ===")
llm_high = ChatOllama(model="llama3.2:1b", temperature=1.0)
response_high = llm_high.invoke([HumanMessage(content="こんにちは")])
print(response_high.content)
