# ⏰ Discord Reminder Bot（リマインダーくん）

指定した時刻にメッセージをリマインドしてくれるDiscordボットです。

---

## 🔧 機能

- `!remind HH:MM メッセージ`
  - 指定した時刻にリマインドメッセージを送信します
  - 例: `!remind 14:30 ミーティング！`

---

## 🚀 セットアップ（ローカル環境）

### 1. ライブラリをインストール

```bash
pip install -r requirements.txt
```

### 2. `.env` ファイルを作成（※ローカルのみ）

```env
DISCORD_BOT_TOKEN=あなたのボットトークン
```

### 3. Botを実行

```bash
python bot.py
```

---

## ☁️ Railwayでデプロイする方法

### 1. このリポジトリをGitHubにプッシュ

```bash
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/あなたのユーザー名/discord-reminder-bot.git
git push -u origin main
```

### 2. Railwayに接続・デプロイ

- [Railway](https://railway.app/) にGitHub連携でログイン
- 「New Project」→「Deploy from GitHub Repo」
- このリポジトリを選択

### 3. 環境変数を追加

`DISCORD_BOT_TOKEN` にボットのトークンを登録

---

## 📦 ファイル構成

```
discord-reminder-bot/
├── bot.py               # メインのボットコード
├── requirements.txt     # ライブラリ一覧
└── README.md            # このファイル
```

---

## 🧠 今後のアップデート候補

- 日付指定のリマインダー
- 毎日 / 毎週繰り返し通知
- Slashコマンド対応
- Web UIからの管理機能

---

## 📬 ご連絡・作者

このBotは自由に改変・商用利用できます！  
不具合・要望はIssueかPR、またはX（Twitter）などでご連絡ください。
```

---

