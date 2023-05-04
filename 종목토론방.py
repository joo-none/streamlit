import streamlit as st
import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup



st.title('종목 토론방 분석')

# 한페이지를 수집하는 함수
def get_one_page(item_code, page_no):
    url = f"https://finance.naver.com/item/board.naver?code={item_code}&page={page_no}"
    headers = {"user-agent":"Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    table = pd.read_html(response.text)[1]
    cols = ["날짜", "제목", "글쓴이", "조회", "공감", "비공감"]
    table = table[cols]
    temp = table.dropna()
    return temp

# 여러 페이지를 수집하는 함수
def jongmok_toron(item_code, last_page):
    
    post_list = []
    for page_no in range(1, last_page + 1):

        df = get_one_page(item_code, page_no)
        post_list.append(df)  
        time.sleep(0.001)

    post_list = pd.concat(post_list, ignore_index=True)
    return post_list

# 내용 링크를 수집하는 함수
def jongmok_context(item_code, page_no):
    url = f'https://finance.naver.com/item/board.naver?code={item_code}&page={page_no}'
    headers = {"user-agent":"Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    base_url = 'https://finance.naver.com/'
    sub_url_list = [soup.select('td.title > a')[i]['href'] for i in range(len(soup.select('td.title > a')))]
    context_url_list = [base_url + i for i in sub_url_list]
    return context_url_list

# 원하는 페이지만큼 내용 링크를 수집하는 함수 만들기
def context_link(item_code, last_page):
    b=[]
    for i in range(1, last_page + 1):
        a = jongmok_context(item_code, i)
        b.append(a)
        context_list = pd.concat([pd.DataFrame(x) for x in b], ignore_index=True)
    return context_list

# # 종목토론 목록과 내용링크를 포함한 데이터프레임 만들기
# def 목록_내용링크(item_code, last_page):
#     종목토론_목록 = jongmok_toron(item_code, last_page)
#     종목토론_내용링크 = context_link(item_code, last_page)
#     a = pd.concat([종목토론_목록, 종목토론_내용링크], axis=1, ignore_index=True)
#     a.columns = ['날짜', '제목', '글쓴이', '조회', '공감', '비공감', '내용링크']
#     return a

# # 내용을 수집하는 함수
# def 종목토론_내용(item_code, last_page):
#     content = []
#     df = 목록_내용링크(item_code, last_page)
#     for i in df['내용링크']:
#         headers = {"user-agent": "Mozilla/5.0"}
#         response = requests.get(i, headers=headers)
#         html = BeautifulSoup(response.text)
#         a = html.select('#body')[0].text
#         content.append(a)        
#     return content

# def 종목토론_목록_내용링크_내용(item_code, last_page):
#     df = 목록_내용링크(item_code, last_page)
#     df['내용'] = 종목토론_내용(item_code, last_page)
#     return df

item_code = '086520'
last_page = 1
st.dataframe(context_link(item_code, last_page))







