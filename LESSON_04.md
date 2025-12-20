# レッスン4: ストリーミング応答

## 🎯 学習目標
- ストリーミング応答の仕組みを理解する
- リアルタイムで応答を受け取る方法を学ぶ
- ユーザー体験向上のためのストリーミング活用法を習得する

## 📝 タスク1: ファイルを作成する

`04_streaming.py` というファイルを作成してください。

## 📝 タスク2: 必要なライブラリをインポートする

```python
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import time
```

## 📝 タスク3: チェーンをセットアップする

```python
prompt = ChatPromptTemplate.from_template(
    "次のトピックについて詳しく説明してください: {topic}"
)
model = ChatOllama(model="llama3.2:1b", temperature=0.7)
output_parser = StrOutputParser()

chain = prompt | model | output_parser
```

## 📝 タスク4: 通常の応答を試す

まず、ストリーミングなしで実行してみます：

```python
print("=== 通常の応答 ===")
start = time.time()
result = chain.invoke({"topic": "機械学習の基礎"})
end = time.time()

print(f"応答（{end - start:.2f}秒後）:")
print(result)
```

## 📝 タスク5: ストリーミング応答を実装する

次に、`stream()` メソッドを使ってストリーミングで受け取ります：

```python
print("\n=== ストリーミング応答 ===")
start = time.time()

for chunk in chain.stream({"topic": "人工知能の歴史"}):
    print(chunk, end="", flush=True)

end = time.time()
print(f"\n(完了: {end - start:.2f}秒)")
```

**解説:**
- `stream()`: 応答を少しずつ受け取る
- `chunk`: 応答の一部分
- `end=""`: 改行しない
- `flush=True`: すぐに表示する

## 📝 タスク6: 実行してみる

```bash
python 04_streaming.py
```

通常の応答とストリーミング応答の違いを観察してください。

## 🔬 チャレンジ課題: チャットボット風の対話

複数の質問に対してストリーミングで答えるチャットボットを作ってみましょう：

```python
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
```

## 🔬 発展課題: 遅延を加えてストリーミング感を演出

リアルタイム感を強調するために、わずかな遅延を加えてみましょう：

```python
for chunk in chat_chain.stream({"question": "AIとは？"}):
    print(chunk, end="", flush=True)
    time.sleep(0.02)  # 20ミリ秒の遅延
```

## ✅ 確認ポイント

- [ ] `stream()` メソッドが使えましたか？
- [ ] 応答がリアルタイムで表示されましたか？
- [ ] 通常の応答との違いが分かりましたか？

## 💡 理解度チェック

1. `invoke()` と `stream()` の違いは何ですか？
2. ストリーミングはどのような場面で有用ですか？
3. `flush=True` は何のために使いますか？

## 📊 ストリーミングのメリット

- ✅ すぐに結果が表示され始める
- ✅ 長い応答でも待ち時間が短く感じる
- ✅ チャットUIに最適
- ✅ ユーザー体験の向上

## 🎉 完了したら

`LESSON_05.md` を開いてレッスン5（最終レッスン）に進んでください！
