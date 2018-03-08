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

def ppomppu_test():
    fpage = 1
    epage = 15
    wdate = (datetime.date.today() - datetime.timedelta(1)).strftime("%y/%m/%d")
    #edate = input("원하는 종료 날짜를 입력하세요(ex, 2017.07.31)")

    # DB 연결
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
        cafe_url = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=phone&page=' + str(fpage)
        cafe.get(cafe_url)

        html = cafe.page_source

        soup = BeautifulSoup(html, 'html.parser')

        for n in range(2):
            for line in soup.select('tr.list'+str(n)):
                board_writer1 = line.select('td.list_vspace')[2].text.strip()
                board_title1 = line.select('td.list_vspace')[3].text.strip()
                board_date1 = line.select('td.list_vspace')[4].text.strip()
                board_recommand1 = line.select('td.list_vspace')[5].text.strip()
                board_view1 = line.select('td.list_vspace')[6].text.strip()

                try:
                    board_ur = line.select('td.list_vspace > a')[0].get('href')
                    board_url1 = 'http://www.ppomppu.co.kr/zboard/' + str(board_ur)
                except IndexError:
                    board_url1 = ''


                # writer가 이미지일 경우
                if board_writer1 == '':
                    board_writer1 = line.select('td.list_vspace')[2]
                    board_writer1 = board_writer1.select('a > img')[0].get('alt')

                # 추천필드에서 추천수만 추출(비추천 제거)
                p = re.compile('^\d+')
                board_recommand1 = p.findall(board_recommand1)
                board_recommand1 = ''.join(board_recommand1)

                if board_recommand1 == '':
                    board_recommand1 = 0
                try:
                    q = re.compile('\d+$')
                    board_num = q.findall(board_url1)
                    board_num = int(''.join(board_num))
                except ValueError:
                    board_num = ''

                ## 해당 날짜만 가져옴
                if board_date1 == wdate:
                    try:
                        sql = "INSERT INTO ppomppu_test VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        values = (board_num, board_title1, board_writer1, board_date1, board_view1, board_recommand1, board_url1)
                        cur.execute(sql, values)
                        con.commit()
                    except pymysql.err.IntegrityError:
                        continue
                    except pymysql.err.InternalError:
                        continue

                    # print(board_num)
                    # print(board_writer1)
                    # print(board_title1)
                    # print(board_date1)
                    # print(board_recommand1)
                    # print(board_view1)
                    # print(board_url1)
                    # print()

        fpage += 1

    cur.close()
    con.close()

    cafe.quit()

def ppomppu_test_detail():
    # DB 연결
    con = pymysql.connect(host="1.246.219.220", user="safty", password="Cndqnreo!@#$", db="product_safty", charset="utf8mb4")
    #con = pymysql.connect(host="localhost", user="root", password="7747", db="momsholic", charset="utf8")
    cur = con.cursor()

    # DB 정보 불러오기
    sql = "select board_num, board_url from ppomppu_test where board_date = '{}'".format((datetime.date.today() - datetime.timedelta(1)).strftime("%Y-%m-%d"))
    cur.execute(sql)
    rows = cur.fetchall()

    # 크롬 드라이버의 위치 설정
    cafe = webdriver.Chrome('C:/Users/KyeongMin/Desktop/App/chrome/chromedriver.exe')
    #cafe = webdriver.Chrome('/Users/kyeongmin/Documents/chromedriver')

    # 팬텀 JS 위치 지정 - 안보이게 하는 코드
    #cafe = webdriver.PhantomJS('C:/Users/KyeongMin/Desktop/App/chrome/phantomjs-2.1.1-windows/bin/phantomjs')
    #cafe = webdriver.PhantomJS('/Users/kyeongmin/Documents/phantomjs-2.1.1-macosx/bin/phantomjs')

    # 페이지가 모두 로드되기까지 5초 기다림
    cafe.implicitly_wait(5)

    for i in range(len(rows)) :
        # 게시글 부분
        board_num = rows[i][0]
        detail_url = rows[i][1]
        if detail_url == '':
            continue
        str_url = ''.join(detail_url)

        cafe.get(str_url)
        html = cafe.page_source

        soup = BeautifulSoup(html, 'html.parser')

        ## 비밀글일 경우 거르기
        try:
            d_title = soup.select('font.view_title2')[0].text.strip()
        except IndexError:
            continue

        ## 아이디가 이미지일 경우 처리하기
        try:
            d_writer = soup.select('font.view_name')[0].text.strip()
        except IndexError:
            try:
                d_writer = soup.select('td.han > span')[0]
                d_writer = d_writer.select('a > img')[0].get('alt')
            except IndexError:
                d_writer = '[*비회원*]'

        ## 블라인드 게시글처리
        try:
            d_content = soup.select('td.board-contents')[0].text.strip()
        except IndexError:
            continue

        # 정규식을 활용하여 날짜부분만 추출
        p = re.compile('\d+\-\d+\-\d+\s\d+\:\d+')
        d_date = p.findall(soup.select('td.han')[1].text.strip())
        d_date = ''.join(d_date) # 리스트형식을 스트링형태로 변환

        try:
            sql = "INSERT INTO ppomppu_test_detail VALUES (%s, %s, %s, %s, %s)"
            values = (board_num, d_title, d_writer, d_content, d_date)
            cur.execute(sql, values)
        except pymysql.err.InternalError:
            continue
        except pymysql.err.IntegrityError:
            continue
        except IndexError:
            continue

        # print(board_num)
        # print(d_title)
        # print(d_writer)
        # print(d_content)
        # print(d_date)
        # print()
        # print()

        reply = soup.select('div#quote')
        reply_nick = []
        for r in reply:
            rr = r.select('td')
            reply_content = r.select('div.han')
            reply_date = r.select('font.eng')
            rl = len(rr)
            for p in range(rl):
                r_nick = rr[p].select('b > a')
                if r_nick != []:
                    reply_nick.append(r_nick)

            ## 이중리스트 벗기기
            reply_nick = [row_element for row in reply_nick for row_element in row]

            for p in range(len(reply_nick)):
                a = reply_nick[p].text.strip()
                b = reply_content[p].text.strip()
                c = reply_date[p].text.strip()
                try:
                    if a == '':
                        a = reply_nick[p].select('img')[0].get('alt')
                except IndexError:
                    a = '익명'

                day = c[:10]
                time = c[10:]
                dt = str(day) + ' ' + str(time)
                # print(a)
                # print(b)
                # print(dt)
                # print('---------------------')
                # print('---------------------')

                sql = "INSERT INTO ppomppu_test_reply(reply_nick, reply_content, reply_date, board_num) VALUES (%s, %s, %s, %s)"
                values = (a, b, dt, board_num)
                cur.execute(sql, values)


            con.commit()
            #time.sleep(1*random.random())

    cur.close()
    con.close()
    cafe.quit()

def main():
    ppomppu_test()
    ppomppu_test_detail()
    print("{} 크롤링 완료".format(datetime.date.today().strftime("%Y-%m-%d")))

if __name__ == "__main__" :
    schedule.every().day.at("07:00").do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
