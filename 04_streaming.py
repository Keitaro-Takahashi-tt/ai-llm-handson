from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import time

prompt = ChatPromptTemplate.from_template(
    "次のトピックについて詳しく説明してください: {topic}"
)
model = ChatOllama(model="llama3.2:1b", temperature=0.7)
output_parser = StrOutputParser()

chain = prompt | model | output_parser
print("=== 通常の応答 ===")
start = time.time()
result = chain.invoke({"topic": "機械学習の基礎"})
end = time.time()

print(f"応答（{end - start:.2f}秒後）:")
print(result)

print("\n=== ストリーミング応答 ===")
start = time.time()

for chunk in chain.stream({"topic": "人工知能の歴史"}):
    print(chunk, end="", flush=True)

end = time.time()
print(f"\n(完了: {end - start:.2f}秒)")

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "あなたは親切なアシスタントです。"),
    ("user", "{question}")
])

chat_chain = chat_prompt | model | output_parser

questions = [
    "Pythonとは何ですか？",
    "なぜPythonは人気があるのですか？"
]

for question in questions:
    print(f"\n👤 ユーザー: {question}")
    print("🤖 AI: ", end="", flush=True)
    
    for chunk in chat_chain.stream({"question": question}):
        print(chunk, end="", flush=True)
    
    print()  # 改行
