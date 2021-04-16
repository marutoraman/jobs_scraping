# スクレイピングサンプル
工場求人ジョブズのスクレイピングサンプルです。
全求人を検索して、各個別求人のタイトルを取得します。

### 初期設定
- 仮想環境構築
python -m venv venv
- モジュールインストール
pip install -r requrements.txt
- テスト
python -m pytest scraping_test.py::<関数名> -s