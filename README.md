# gh_copilot_handson

GitHub Copilot を使って Python 製のチャットアプリを作成

# 事前準備

- Python 3.10 以上の環境を用意してください
- git コマンドが使える環境を用意してください
- GitHub アカウントを作成してください
- Visual Studio Code をインストールしてください
- Visual Studio Code に GitHub Copilot をインストールしてください
- Visual Studio Code に Python 拡張機能をインストールしてください
- Visual Studio Code に Git 拡張機能をインストールしてください

# 手順

### 1. このリポジトリをクローンしてください

```
git clone
```

### 2. プロジェクトを Visual Studio Code に開いてください

```
code gh_copilot_handson
```

### 3. Python の仮想環境を作成してください

```
python -m venv .venv
```

### 4. 仮想環境を有効化してください

```
source .venv/bin/activate
```

### 5. 依存パッケージをインストールしてください

```
pip install -r requirements.txt
```

### 6. プロジェクトを起動してください

```
uvicorn main:app --reload
```
