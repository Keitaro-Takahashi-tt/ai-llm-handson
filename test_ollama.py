from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

print("�� Ollamaに接続中...")
print("使用モデル: llama3.2:1b (ローカル実行)")
print("=" * 60)

# Ollamaモデルの初期化
llm = ChatOllama(
    model="llama3.2:1b",  # ダウンロードしたモデル
    temperature=0.7
)

# メッセージの作成
messages = [
    SystemMessage(content="You are a helpful AI assistant. Answer concisely in Japanese."),
    HumanMessage(content="LangChainとは何ですか？簡潔に説明してください。")
]

# 応答の取得
print("\n� 質問を送信中...\n")
response = llm.invoke(messages)

print("=" * 60)
print("� 質問: LangChainとは何ですか？")
print("=" * 60)
print(f"� AI: {response.content}")
print("=" * 60)
print("\n✨ テスト成功！ローカルLLMが正常に動作しています。")
