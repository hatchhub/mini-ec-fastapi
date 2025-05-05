# mini-ec-fastapi

FastAPI + HTMX を使用した、軽量なECサイトのプロトタイプです。

## 🚀 セットアップ手順

```bash
# 仮想環境を有効化（未作成の場合は python -m venv venv）
source venv/bin/activate  # Windowsの方は venv\Scripts\activate

# 依存パッケージのインストール
pip install -r requirements.txt

# サーバー起動
uvicorn app.main:app --reload
```

## 🛒 機能概要
- 商品一覧表示
- カート追加・削除（HTMXによる非同期処理）
- 購入完了画面の表示
- CSSコンポーネント分割対応（header/item/button など）

## 🗂️ ディレクトリ構成（抜粋）

```
app/
├── templates/
│   ├── index.html
│   ├── cart.html
│   ├── checkout.html
│   └── partials/
│       ├── header.html
│       └── footer.html
├── static/
│   └── css/
│       ├── base.css
│       ├── header.css
│       ├── item.css
│       └── button.css
├── main.py
```

## 📦 使用技術
- Python 3.x
- FastAPI
- HTMX
- Jinja2
- HTML / CSS
