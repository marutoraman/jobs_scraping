# スクレイピングサンプル
工場求人ジョブズのスクレイピングサンプルです。<BR>
全求人を検索して、各個別求人のタイトルを取得します。

### 初期設定
- 仮想環境構築<BR>
python -m venv venv
- モジュールインストール<BR>
pip install -r requrements.txt
- テスト<BR>
python -m pytest scraping_test.py::<関数名> -s

### 実行方法
python scraping.py