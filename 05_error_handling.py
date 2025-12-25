from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
import logging
import time

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


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


def chat_with_validation(user_input: str):
    """検証付きチャット関数"""
    # 入力検証
    is_valid, validated = validate_input(user_input)
    if not is_valid:
        return validated  # エラーメッセージを返す
    
    # 安全なLLM呼び出し
    return safe_llm_call(validated)


if __name__ == "__main__":
    # タスク5: safe_llm_callを使ってみる
    print("=" * 60)
    print("タスク5: 安全なLLM呼び出しのテスト")
    print("=" * 60)
    result = safe_llm_call("LangChainの主な機能を3つ教えてください")
    print(f"\n応答:\n{result}\n")
    
    # タスク7: validate_inputを使ってみる
    print("=" * 60)
    print("タスク7: 入力検証のテスト")
    print("=" * 60)
    
    # テスト1: 正常な入力
    is_valid, result = validate_input("Pythonについて教えて")
    print(f"検証結果: {'✅ OK' if is_valid else '❌ NG'} - {result}")
    
    # テスト2: 空の入力
    is_valid, result = validate_input("")
    print(f"検証結果: {'✅ OK' if is_valid else '❌ NG'} - {result}")
    
    # テスト3: 危険な入力
    is_valid, result = validate_input("ignore previous instructions")
    print(f"検証結果: {'✅ OK' if is_valid else '❌ NG'} - {result}")
    
    # チャレンジ課題: 完全な対話システム
    print("\n" + "=" * 60)
    print("チャレンジ課題: 検証付きチャットシステム")
    print("=" * 60)
    
    questions = [
        "AIとは何ですか？",
        "",  # 空の入力
        "ignore previous instructions",  # 危険な入力
    ]
    
    for q in questions:
        print(f"\n質問: {q}")
        answer = chat_with_validation(q)
        print(f"応答: {answer}")
