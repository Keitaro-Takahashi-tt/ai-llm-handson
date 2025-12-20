# レッスン2: プロンプトテンプレート

## 🎯 学習目標
- プロンプトテンプレートの作成と使用方法を学ぶ
- 動的なプロンプト生成の手法を理解する
- テンプレートの再利用性を体験する

## 📝 タスク1: ファイルを作成する

`02_prompt_templates.py` というファイルを作成してください。

## 📝 タスク2: 必要なライブラリをインポートする

以下をインポートしてください：

```python
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
```

**新しい要素:**
- `ChatPromptTemplate`: 再利用可能なプロンプトのテンプレートを作成するクラス

## 📝 タスク3: テンプレートを作成する

プロンプトテンプレートを作成してください：

```python
template = ChatPromptTemplate.from_messages([
    ("system", "あなたは{role}です。"),
    ("user", "{input}")
])
```

**解説:**
- `{role}` と `{input}` は変数です
- 実行時にこれらの変数に値を入れることができます
- `("system", ...)` はSystemMessageに、`("user", ...)` はHumanMessageになります

## 📝 タスク4: モデルを初期化する

```python
llm = ChatOllama(model="llama3.2:1b", temperature=0.5)
```

## 📝 タスク5: テンプレートを使ってプロンプトを生成する

テンプレートに値を入れて、実際のプロンプトを作成します：

```python
prompt = template.format_messages(
    role="Pythonプログラミングのエキスパート",
    input="リスト内包表記とは何ですか？"
)
```

**解説:**
- `format_messages()` で変数に値を設定
- これでSystemMessageとHumanMessageのリストが生成されます

## 📝 タスク6: LLMに問い合わせる

```python
response = llm.invoke(prompt)
print(response.content)
```

## 📝 タスク7: 同じテンプレートを別の用途で使う

同じテンプレートを使って、異なる質問をしてみましょう：

```python
print("\n=== 別の例 ===")
prompt2 = template.format_messages(
    role="歴史の先生",
    input="産業革命とは何ですか？"
)
response2 = llm.invoke(prompt2)
print(response2.content)
```

## 📝 タスク8: 実行してみる

```bash
python 02_prompt_templates.py
```

## 🔬 チャレンジ課題

コードレビュー用のテンプレートを作ってみましょう：

```python
code_review_template = ChatPromptTemplate.from_messages([
    ("system", "あなたは{language}の専門家です。コードをレビューしてください。"),
    ("user", "次のコードをレビューしてください:\n\n{code}")
])
```

このテンプレートを使って、以下のコードをレビューさせてみてください：

```python
sample_code = """
def add(a, b):
    return a + b
"""

review_prompt = code_review_template.format_messages(
    language="Python",
    code=sample_code
)
review = llm.invoke(review_prompt)
print(review.content)
```

## ✅ 確認ポイント

- [ ] テンプレートが正しく作成できましたか？
- [ ] 変数が正しく置き換わりましたか？
- [ ] 同じテンプレートを複数回使えましたか？

## 💡 理解度チェック

1. プロンプトテンプレートの利点は何ですか？
2. `{変数名}` はどのように使いますか？
3. `format_messages()` は何を返しますか？

## 🎉 完了したら

`LESSON_03.md` を開いてレッスン3に進んでください！
