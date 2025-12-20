from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template(
    "次の質問に日本語で簡潔に答えてください: {question}"
)

model = ChatOllama(
  model="llama3.2:1b",
  temperature=0.5
  )

output_parser = StrOutputParser()

chain = prompt | model | output_parser


result =chain.invoke({"question":"人工知能とはなんでしょうか？"})
print(result)

translation_prompt = ChatPromptTemplate.from_messages([
  ("system", "You are a translator. Translate from {source_lang} to {target_lang}. Output ONLY the translation, nothing else."),
  ("user","Translate this text to {target_lang}: {text}")
])
translation_chain = translation_prompt | model | output_parser

result = translation_chain.invoke({
  "source_lang":"Japanese",
  "target_lang":"English",
  "text":"機械学習は面白いです。"
})

print(result)

questions = [
    "Pythonの特徴は？",
    "機械学習とは？",
    "クラウドとは？"
]

for q in questions:
    answer = chain.invoke({"question": q})
    print(f"Q: {q}")
    print(f"A: {answer}\n")
