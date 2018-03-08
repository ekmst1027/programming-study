# -*- coding: utf-8 -*-

#2017.09.06 (수) - 작업시작

### 디시인사이드 스마트폰갤러리 게시글 크롤링

import schedule
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import requests
import pymysql
import time, random
import datetime

def dcinside_test():
    fpage = 1
    epage = 20
    wdate = (datetime.date.today() - datetime.timedelta(1)).strftime("%Y.%m.%d")
    #edate = input("원하는 종료 날짜를 입력하세요(ex, 2017.07.31)")

    con = pymysql.connect(host="1.246.219.220", user="safty", password="Cndqnreo!@#$", db="product_safty", charset="utf8mb4")
    #con = pymysql.connect(host="localhost", user="root", password="7747", db="momsholic", charset="utf8")
    cur = con.cursor()

    # 크롬 드라이버의 위치 설정
    cafe = webdriver.Chrome('C:/Users/KyeongMin/Desktop/App/chrome/chromedriver.exe')
    #cafe = webdriver.Chrome('/Users/kyeongmin/Documents/chromedriver')

    # 팬텀 JS 위치 지정 - 안보이게 하는 코드
    #cafe = webdriver.PhantomJS('C:/Users/KyeongMin/Desktop/App/chrome/phantomjs-2.1.1-windows/bin/phantomjs')
    #cafe = webdriver.PhantomJS('/Users/kyeongmin/Documents/phantomjs-2.1.1-macosx/bin/phantomjs')

    # 페이지가 모두 로드되기까지 3초 기다림
    cafe.implicitly_wait(3)

    while fpage <= epage:
        cafe_url = 'http://gall.dcinside.com/board/lists/?id=smartphone&page=' + str(fpage)
        cafe.get(cafe_url)
        html = cafe.page_source

        soup = BeautifulSoup(html, 'html.parser')

        # 필요한 부분 파싱하기
        for tbody in soup.select('tbody.list_tbody'):
            board_num = tbody.select('td.t_notice') # 게시글 번호
            board_title = tbody.select('td.t_subject') # 게시글 제목
            board_id = tbody.select('td.t_writer') # 게시자
            board_date = tbody.select('td.t_date') # 게시날짜
            board_v = tbody.select('td.t_hits')

            board_view = [] # 조회수
            board_like = [] # 추천수
            board_url = [] # url 주소

            for j in range(0, len(board_v)):
                if (j % 2) == 0:
                    board_vie = board_v[j]
                    board_view.append(board_vie)
                else:
                    board_lik = board_v[j]
                    board_like.append(board_lik)

            for i in range(0, len(board_num)):
                board_num[i] = board_num[i].text.strip()
                board_title[i] = board_title[i].text.strip()
                board_id[i] = board_id[i].text.strip()
                board_date[i] = board_date[i].text.strip()
                board_view[i] = board_view[i].text.strip()
                board_like[i] = board_like[i].text.strip()
                board_ur = "http://gall.dcinside.com/board/view/?id=smartphone&no=" + str(board_num[i])
                board_url.append(board_ur)

                ## 해당 날짜만 가져옴
                if board_date[i] == wdate :
                    if board_num[i] != "공지":
                        # print(board_num[i])
                        # print(board_title[i])
                        # print(board_id[i])
                        # print(board_date[i])
                        # print(board_view[i])
                        # print(board_like[i])
                        # print(board_url[i])

                        try:
                            sql = "INSERT INTO dcinside_test VALUES (%s, %s, %s, %s, %s, %s, %s)"
                            values = (board_num[i], board_title[i], board_id[i], board_date[i], board_view[i], board_like[i], board_url[i])
                            cur.execute(sql, values)
                            con.commit()

                        ## 다음에 시험할때는 continue로 바꿔서 해보기!!
                        except pymysql.err.IntegrityError:
                            continue

        fpage += 1

    cur.close()
    con.close()

    cafe.quit()

def dc_smartph_detail():
    # DB 연결
    con = pymysql.connect(host="1.246.219.220", user="safty", password="Cndqnreo!@#$", db="product_safty", charset="utf8mb4")
    #con = pymysql.connect(host="localhost", user="root", password="7747", db="momsholic", charset="utf8")
    cur = con.cursor()

    # DB 정보 불러오기
    sql = "select board_num, board_url from dcinside_test where board_date = '{}'".format((datetime.date.today() - datetime.timedelta(1)).strftime("%Y-%m-%d"))
    cur.execute(sql)
    rows = cur.fetchall()

    # 크롬 드라이버의 위치 설정
    cafe = webdriver.Chrome('C:/Users/KyeongMin/Desktop/App/chrome/chromedriver.exe')
    #cafe = webdriver.Chrome('/Users/kyeongmin/Documents/chromedriver')

    # 팬텀 JS 위치 지정 - 안보이게 하는 코드
    #cafe = webdriver.PhantomJS('C:/Users/KyeongMin/Desktop/App/chrome/phantomjs-2.1.1-windows/bin/phantomjs')
    #cafe = webdriver.PhantomJS('/Users/kyeongmin/Documents/phantomjs-2.1.1-macosx/bin/phantomjs')

    # 페이지가 모두 로드되기까지 3초 기다림
    cafe.implicitly_wait(3)

    for i in range(len(rows)) :

        # 게시글 부분
        board_num = rows[i][0]
        detail_url = rows[i][1]
        str_url = ''.join(detail_url)

        cafe.get(str_url)
        html = cafe.page_source

        soup = BeautifulSoup(html, 'html.parser')

        try:
            d_title = soup.select('dl.wt_subject > dd')[0].text.strip()
            d_date = soup.select('div.w_top_right')[0].text.strip()[0:19]
            d_nick = soup.select('span.user_nick_nm')[0].text.strip()
            d_content = soup.select('table')[0].text.strip()

            sql = "INSERT INTO dcinside_test_detail VALUES (%s, %s, %s, %s, %s)"
            values = (board_num, d_title, d_nick, d_content, d_date)
            cur.execute(sql, values)

        ## 삭제되거나 없는 게시물 예외처리
        except IndexError:
            continue

        ## 이미 적재되어 있는 게시물일 경우 다시 적재 안함
        except pymysql.err.IntegrityError:
            continue

        # 댓글부분
        reply = soup.select('tr.reply_line')

        reply_nick = []
        reply_content = []
        reply_date = []

        for r in reply:
            reply_nic = r.select('td.user.user_layer')
            reply_conten = r.select('td.reply')
            reply_dat = r.select('td.retime')
            for i in range(len(reply_nic)):
                reply_nick.append(reply_nic[i].text.strip())
                reply_content.append(str(reply_conten[i].text.strip()))
                if reply_dat[i].text.strip() == '':
                    reply_date.append('0000-00-00 00:00')
                else:
                    reply_date.append(reply_dat[i].text.strip())

        for j in range(len(reply_nick)):
            sql = "INSERT INTO dcinside_test_reply (reply_nick, reply_content, reply_date, board_num) VALUES (%s, %s, %s, %s)"
            values = (reply_nick[j], reply_content[j], reply_date[j], board_num)
            cur.execute(sql, values)

        con.commit()
        #time.sleep(1*random.random())

        # print(board_num)
        # print(d_title)
        # print(d_date)
        # print(d_nick)
        # print(d_content)
        # print(reply_nick)
        # print(reply_content)
        # print(reply_date)

    cur.close()
    con.close()

    cafe.quit()

def main():
    dcinside_test()
    dc_smartph_detail()
    print("{} 크롤링 완료".format(datetime.date.today().strftime("%Y-%m-%d")))

if __name__ == "__main__" :
    #main()
    schedule.every().day.at("07:00").do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
