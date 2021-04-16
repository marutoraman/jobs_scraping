import requests
from bs4 import BeautifulSoup as bs
import urllib.parse

SEARCH_URL = "https://factory-jobs.jp/search.php"
BASE_URL = "https://factory-jobs.jp/info.php?type=job&id={job_id}"

def parse_query_string():
    '''
    クエリストリングを取得
    （開発用のため、運用では使わない）
    '''
    url = "https://factory-jobs.jp/search.php?run=true&type=job&adds=&add_sub=&adds_PAL%5B%5D=group+table+area+adds+area_id&add_sub_PAL%5B%5D=match+comp&job_type%5B%5D=JT001&job_type%5B%5D=JT002&job_type%5B%5D=JT003&job_type%5B%5D=JT004&job_type%5B%5D=JT005&job_type%5B%5D=JT006&job_type%5B%5D=JT007&job_type%5B%5D=JT008&job_type%5B%5D=JT009&job_type%5B%5D=JT010&job_type%5B%5D=JT011&job_type%5B%5D=JT013&job_type%5B%5D=JT014&job_type%5B%5D=JT016&job_type%5B%5D=JT017&job_type%5B%5D=JT012&job_type%5B%5D=JT015&job_type%5B%5D=JT018&job_type%5B%5D=JT019&job_type_PAL%5B%5D=match+in&job_type_CHECKBOX=&job_addition_CHECKBOX=&job_addition_PAL%5B%5D=match+and&salary_type=&salary_type_PAL%5B%5D=match+comp&term_flg=&term_flg_PAL%5B%5D=match+comp&free=&page=0"
    query = urllib.parse.parse_qs(url)
    print(query)
    
def fetch_all_item():
    '''
    全求人を取得
    '''
    # https://factory-jobs.jp/search.php?run=true&type=job&adds=&add_sub=&adds_PAL%5B%5D=group+table+area+adds+area_id&add_sub_PAL%5B%5D=match+comp&job_type%5B%5D=JT001&job_type%5B%5D=JT002&job_type%5B%5D=JT003&job_type%5B%5D=JT004&job_type%5B%5D=JT005&job_type%5B%5D=JT006&job_type%5B%5D=JT007&job_type%5B%5D=JT008&job_type%5B%5D=JT009&job_type%5B%5D=JT010&job_type%5B%5D=JT011&job_type%5B%5D=JT013&job_type%5B%5D=JT014&job_type%5B%5D=JT016&job_type%5B%5D=JT017&job_type%5B%5D=JT012&job_type%5B%5D=JT015&job_type%5B%5D=JT018&job_type%5B%5D=JT019&job_type_PAL%5B%5D=match+in&job_type_CHECKBOX=&job_addition_CHECKBOX=&job_addition_PAL%5B%5D=match+and&salary_type=&salary_type_PAL%5B%5D=match+comp&term_flg=&term_flg_PAL%5B%5D=match+comp&free=&page=0
    # 全検索用のリクエストパラメーターを作成
    params = {
        'run':'true', 
        'type': 'job', 
        'adds_PAL[]': ['group table area adds area_id'], 
        'add_sub_PAL[]': ['match comp'], 
        'job_type[]': ['JT001', 'JT002', 'JT003', 'JT004', 'JT005', 'JT006', 'JT007', 'JT008', 'JT009', 'JT010', 'JT011', 'JT013', 'JT014', 'JT016', 'JT017', 'JT012', 'JT015', 'JT018', 'JT019'], 
        'job_type_PAL[]': ['match in'], 
        'job_addition_PAL[]': ['match and'], 
        'salary_type_PAL[]': ['match comp'], 
        'term_flg_PAL[]': ['match comp'], 
        'page': ""}
    
    # ページ分繰り返し
    for page in range(1000):
        params["page"] = page
        res = requests.get(SEARCH_URL, params=params)
        if not(300 > res.status_code >= 200):
            return False
        
        # BeautifulSoupでHTMLを解析して個別ページのURLを取得
        soup = bs(res.text, "html.parser")
        item_link_elms = soup.select(".btn_style_06 a")        
        item_links = [item_link_elm.get("href") for item_link_elm in item_link_elms]
        
        # 個別ページの情報を取得
        for item_link in item_links:
            print(item_link)
            fetch_item(item_link)


def fetch_item(url:str):
    '''
    個別ページの情報を取得
    '''
    # urlからjob_idを取得
    if not url.find("id=") >= 0:
        return None
    job_id = url[url.find("id=")+3:]
    
    # 個別ページにアクセス
    res = requests.get(BASE_URL.format(job_id=job_id))
    if not(300 > res.status_code >= 200):
        return False
    
    # BeautifulSoupでHTMLを解析して個別ページのURLを取得
    soup = bs(res.text, "html.parser")
    item_title_elm = soup.select_one(".item_title")        
    print(f"タイトル:{item_title_elm.text}")


if __name__ == "__main__":
    fetch_all_item()