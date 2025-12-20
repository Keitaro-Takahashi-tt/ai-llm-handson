# レッスン5: エラーハンドリングとベストプラクティス

## 🎯 学習目標
- LLM使用時の適切なエラーハンドリング方法を学ぶ
- リトライ機構の実装を理解する
- 安全なLLMアプリケーション開発のベストプラクティスを習得する

## 📝 タスク1: ファイルを作成する

`05_error_handling.py` というファイルを作成してください。

## 📝 タスク2: 必要なライブラリをインポートする

```python
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
import logging
import time
```

## 📝 タスク3: ロギングを設定する

エラーやイベントを記録するためのロギングを設定します：

```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
```

## 📝 タスク4: 安全なLLM呼び出し関数を作る

エラーハンドリングとリトライ機能を持つ関数を作成してください：

```python
def safe_llm_call(message: str, max_retries: int = 3):
    """
    安全なLLM呼び出しを行う関数
    """
    llm = ChatOllama(model="llama3.2:1b", temperature=0.5)
    
    for attempt in range(max_retries):
        try:
            logger.info(f"試行 {attempt + 1}/{max_retries}")
            
            response = llm.invoke([
                SystemMessage(content="簡潔に日本語で答えてください。"),
                HumanMessage(content=message)
            ])
            
            logger.info("✅ 成功")
            return response.content
            
        except Exception as e:
            logger.error(f"❌ エラー: {type(e).__name__}")
            
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # 指数バックオフ
                logger.info(f"⏳ {wait_time}秒待機...")
                time.sleep(wait_time)
            else:
                return "エラーが発生しました"
    
    return "リトライ回数を超過しました"
```

**解説:**
- `try-except`: エラーをキャッチ
- `2 ** attempt`: 指数バックオフ（1秒、2秒、4秒...）
- `max_retries`: 最大リトライ回数

## 📝 タスク5: 関数を使ってみる

```python
result = safe_llm_call("LangChainの主な機能を3つ教えてください")
print(f"\n応答:\n{result}")
```

## 📝 タスク6: 入力検証関数を作る

ユーザー入力を検証してサニタイズする関数を作成します：

```python
def validate_input(user_input: str) -> tuple[bool, str]:
    """
    ユーザー入力を検証する
    """
    # 空文字チェック
    if not user_input or not user_input.strip():
        return False, "エラー: 入力が空です"
    
    # 長さチェック
    if len(user_input) > 1000:
        return False, "エラー: 入力が長すぎます"
    
    # 危険なパターンのチェック
    dangerous = ["ignore previous instructions", "system prompt"]
    for pattern in dangerous:
        if pattern in user_input.lower():
            logger.warning(f"⚠️ 危険なパターン検出: {pattern}")
            return False, "エラー: 不適切な入力"
    
    return True, user_input.strip()
```

## 📝 タスク7: 検証関数を使ってみる

```python
# テスト1: 正常な入力
is_valid, result = validate_input("Pythonについて教えて")
print(f"検証結果: {'✅ OK' if is_valid else '❌ NG'} - {result}")

# テスト2: 空の入力
is_valid, result = validate_input("")
print(f"検証結果: {'✅ OK' if is_valid else '❌ NG'} - {result}")

# テスト3: 危険な入力
is_valid, result = validate_input("ignore previous instructions")
print(f"検証結果: {'✅ OK' if is_valid else '❌ NG'} - {result}")
```

## 📝 タスク8: 実行してみる

```bash
python 05_error_handling.py
```

## 🔬 チャレンジ課題: 完全な対話システム

検証とエラーハンドリングを組み合わせた対話システムを作ってみましょう：

```python
def chat_with_validation(user_input: str):
    """検証付きチャット関数"""
    # 入力検証
    is_valid, validated = validate_input(user_input)
    if not is_valid:
        return validated  # エラーメッセージを返す
    
    # 安全なLLM呼び出し
    return safe_llm_call(validated)

# 使ってみる
questions = [
    "AIとは何ですか？",
    "",  # 空の入力
    "ignore previous instructions",  # 危険な入力
]

for q in questions:
    print(f"\n質問: {q}")
    answer = chat_with_validation(q)
    print(f"応答: {answer}")
```

## ✅ 確認ポイント

- [ ] try-exceptでエラーをキャッチできましたか？
- [ ] リトライ機構が動作しましたか？
- [ ] 入力検証が正しく機能しましたか？
- [ ] ロギングが表示されましたか？

## 💡 理解度チェック

1. 指数バックオフとは何ですか？なぜ使いますか？
2. プロンプトインジェクションとは何ですか？
3. ロギングの目的は何ですか？

## 📋 ベストプラクティスまとめ

### 1. エラーハンドリング
- ✅ try-exceptで例外を適切にキャッチ
- ✅ 具体的なエラーメッセージを提供
- ✅ ログにエラー詳細を記録

### 2. リトライ機構
- ✅ 一時的なエラーに対応
- ✅ 指数バックオフで負荷軽減
- ✅ 最大リトライ回数を設定

### 3. 入力検証
- ✅ ユーザー入力を必ず検証
- ✅ プロンプトインジェクション対策
- ✅ 長さ制限とサニタイズ

### 4. ロギング
- ✅ 重要なイベントを記録
- ✅ デバッグ情報を含める
- ✅ 機密情報は記録しない

### 5. セキュリティ
- ✅ APIキーは環境変数で管理
- ✅ ユーザー入力を直接埋め込まない
- ✅ 出力を検証してから使用

## 🎓 おめでとうございます！

基礎学習コースを完了しました！

### 学んだこと
1. ✅ LLMの基本的な使い方
2. ✅ プロンプトテンプレート
3. ✅ LCELチェーン
4. ✅ ストリーミング応答
5. ✅ エラーハンドリング

### 次のステップ

以下のような応用に挑戦してみましょう：

- **RAG（検索拡張生成）**: ドキュメント検索システムの構築
- **エージェント開発**: タスク自動化とツール連携
- **プロダクション対応**: API化、デプロイメント、モニタリング

詳しくは `Untitled-1` のドキュメントを参照してください！

Happy Coding! 🚀
