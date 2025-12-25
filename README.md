# AI・LLM ハンズオン学習プログラム

LangChainとローカルLLM（Ollama）を使った**実践的なコーディング学習プログラム**です。

## 🎯 このプログラムについて

このプログラムは**自分でコードを書いて学ぶ**スタイルです。
各レッスンの指示に従って、一つずつコードを書いて実行し、動作を確認しながら学習します。

## 📚 学習の流れ

### レッスン一覧

| レッスン | 指示ファイル | 作成するファイル | 学習内容 | 難易度 |
|---------|------------|----------------|---------|--------|
| 1 | `LESSON_01.md` | `01_basic_chat.py` | LLMの基本的なチャット機能 | ⭐ |
| 2 | `LESSON_02.md` | `02_prompt_templates.py` | プロンプトテンプレート | ⭐ |
| 3 | `LESSON_03.md` | `03_chains.py` | LCELチェーンの構築 | ⭐⭐ |
| 4 | `LESSON_04.md` | `04_streaming.py` | ストリーミング応答 | ⭐⭐ |
| 5 | `LESSON_05.md` | `05_error_handling.py` | エラーハンドリング | ⭐⭐⭐ |

## 🚀 始め方

### 前提条件

1. **Ollamaのインストール**
   ```bash
   # macOS/Linux
   curl -fsSL https://ollama.com/install.sh | sh
   
   # または公式サイトからダウンロード
   # https://ollama.com/download
   ```

2. **モデルのダウンロード**
   ```bash
   ollama pull llama3.2:1b
   ```

3. **Pythonパッケージのインストール**
   ```bash
   pip install langchain langchain-ollama langchain-core
   ```

### 学習の進め方

1. **LESSON_01.mdを開く**
   ```bash
   code LESSON_01.md
   ```

2. **指示に従ってコードを書く**
   - タスクごとに何を書くべきか説明があります
   - コードスニペットが提供されています
   - 解説を読んで理解してから書きましょう

3. **実行して動作を確認**
   ```bash
   python 01_basic_chat.py
   ```

4. **実験してみる**
   - パラメータを変更してみる
   - 質問内容を変えてみる
   - チャレンジ課題に挑戦する

5. **次のレッスンへ進む**
   - 各レッスンの最後に次のレッスンへの案内があります

## 📖 学習内容の概要

各レッスンで学ぶ内容の概要です。詳細は各 `LESSON_XX.md` を参照してください。

| レッスン | 主要トピック | 習得スキル |
|---------|------------|-----------|
| 1 | LLMの基本 | SystemMessage、HumanMessage、temperature |
| 2 | テンプレート | ChatPromptTemplate、変数の埋め込み |
| 3 | チェーン | LCEL（パイプライン演算子）、コンポーネント連結 |
| 4 | ストリーミング | stream()、リアルタイム応答 |
| 5 | エラーハンドリング | try-except、リトライ、入力検証 |

## 💡 学習のヒント

### 効果的な学習方法

1. **まずは実行してみる**
   - コードを読む前に、まず動かしてみる
   - 何が起こるか観察する

2. **コードを理解する**
   - コメントを丁寧に読む
   - わからない部分は調べる

3. **実験する**
   - パラメータを変更してみる
   - 自分の質問で試してみる
   - エラーを起こしてみる

4. **応用してみる**
   - 学んだことを組み合わせる
   - 独自のアプリケーションを作る

### つまずいたら

- **Ollamaが動かない**
  ```bash
  # Ollamaサービスの状態確認
  ollama list
  
  # モデルの再ダウンロード
  ollama pull llama3.2:1b
  ```

- **パッケージのエラー**
  ```bash
  # 仮想環境を作成して再インストール
  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate
  pip install langchain langchain-ollama langchain-core
  ```

- **応答が遅い**
  - より小さいモデル（llama3.2:1b）を使用
  - temperatureを下げる（0.3〜0.5）

## 🔗 参考リソース

### 公式ドキュメント
- [LangChain Documentation](https://python.langchain.com/)
- [Ollama Documentation](https://ollama.com/docs)
- [Llama Models](https://llama.meta.com/)

### 学習リソース
- Qiitaの記事貼る予定: AI・LLM・RAGの体系的まとめ
- [Awesome Prompt Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering)

## 🎯 次のステップ

基礎学習が完了したら、以下のような応用に挑戦してみましょう：

1. **RAG（検索拡張生成）の実装**
   - ドキュメント検索システム
   - 知識ベース構築

2. **エージェント開発**
   - タスク自動化
   - ツール連携

3. **プロダクション対応**
   - API化
   - デプロイメント
   - モニタリング

## 📝 ライセンス

このプロジェクトは教育目的で作成されています。

---

**Happy Learning! 🚀**
