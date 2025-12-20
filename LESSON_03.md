# レッスン3: LCELチェーン（パイプライン）

## 🎯 学習目標
- LCELを使ったチェーンの構築方法を学ぶ
- パイプライン演算子 `|` の使い方を理解する
- 複数のコンポーネントを連携させる方法を習得する

## 📝 タスク1: ファイルを作成する

`03_chains.py` というファイルを作成してください。

## 📝 タスク2: 必要なライブラリをインポートする

```python
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
```

**新しい要素:**
- `StrOutputParser`: LLMの応答を文字列に変換するパーサー

## 📝 タスク3: コンポーネントを作成する

3つのコンポーネントを作成してください：

```python
# 1. プロンプトテンプレート
prompt = ChatPromptTemplate.from_template(
    "次の質問に日本語で簡潔に答えてください: {question}"
)

# 2. LLMモデル
model = ChatOllama(model="llama3.2:1b", temperature=0.5)

# 3. 出力パーサー
output_parser = StrOutputParser()
```

## 📝 タスク4: チェーンを構築する

パイプライン演算子 `|` を使ってコンポーネントを連結します：

```python
chain = prompt | model | output_parser
```

**解説:**
- これは `prompt → model → output_parser` の流れを作ります
- データが左から右へ流れていきます
- 各コンポーネントの出力が次のコンポーネントの入力になります

## 📝 タスク5: チェーンを実行する

```python
result = chain.invoke({"question": "人工知能とは何ですか？"})
print(result)
```

**解説:**
- `invoke()` に辞書を渡します
- キーは `{question}` という変数名に対応します
- チェーン全体を通って最終的な文字列が返ります

## 📝 タスク6: 実行してみる

```bash
python 03_chains.py
```

## 🔬 チャレンジ課題1: 翻訳チェーンを作る

複数の変数を持つテンプレートでチェーンを作ってみましょう：

```python
translation_prompt = ChatPromptTemplate.from_messages([
    ("system", "あなたは{source_lang}から{target_lang}への翻訳者です。"),
    ("user", "{text}")
])

translation_chain = translation_prompt | model | output_parser

# 使ってみる
result = translation_chain.invoke({
    "source_lang": "日本語",
    "target_lang": "英語",
    "text": "機械学習は面白いです。"
})
print(result)
```

## 🔬 チャレンジ課題2: 複数の質問を処理する

同じチェーンで複数の質問に答えさせてみましょう：

```python
questions = [
    "Pythonの特徴は？",
    "機械学習とは？",
    "クラウドとは？"
]

for q in questions:
    answer = chain.invoke({"question": q})
    print(f"Q: {q}")
    print(f"A: {answer}\n")
```

## ✅ 確認ポイント

- [ ] パイプライン演算子 `|` が使えましたか？
- [ ] チェーンが正しく動作しましたか？
- [ ] チェーンを再利用できましたか？

## 💡 理解度チェック

1. LCEL（`|` 演算子）の利点は何ですか？
2. `prompt | model | output_parser` のデータフローを説明できますか？
3. チェーンの再利用はどのようなメリットがありますか？

## 🎉 完了したら

`LESSON_04.md` を開いてレッスン4に進んでください！
