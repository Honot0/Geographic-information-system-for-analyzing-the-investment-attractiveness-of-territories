import urllib.request
import urllib.request
from bs4 import BeautifulSoup
import re
import os
import time
from threading import Thread
from multiprocessing import Process
import ast
import cfscrape
import lxml.html
import requests
from lxml.cssselect import CSSSelector
from lxml import etree
try:
    from helpTools import dump, get_right, log, get_html
except:
    from .helpTools import dump, get_right, log, get_html

import functions


import pycurl






def get_session(url):

    session = requests.Session()
    session.headers ={
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'dnt': '1',
        'pragma': 'no-cache',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    # print("INTERNET_OPEN!")
    return cfscrape.create_scraper(sess=session)




def listorg_list_parser(page, url):

    #как сделать запрос через сессию и получить страницу
    # session = get_session(url)
    # rqst = session.get(url).content
    # try:
    #     soup = BeautifulSoup(rqst, features="html.parser")
    #     print(soup)
    # except:
    #     pass

    #как использовать cssSelector если он может работать на полученной странице
    # rqst = get_html(url)
    # tree = lxml.html.parse(rqst)
    # td_empformbody = CSSSelector('td.empformbody')#/html/body/div[1]/div[2]/div[2]/p[2]
    # for elem in td_empformbody(tree):
    #     # Do something with these table cells.

    #вариант через суп
    soup = BeautifulSoup(page, features="html.parser")
    # print(soup.prettify())

    link=''
    short_name=''
    name=''
    working=True
    inn=''
    address=''

    list_of_orgs = []
    pattern1 = r' {3,}'
    pattern2 =  r'\n'
    table1 = soup.find_all('label')
    try:
        for ea in table1:
            link = ea.find('a').get('href')
            link = "https://www.list-org.com"+link
            link = re.sub(pattern2, '', link, count=0)

            short_name = ea.find('a').get_text()
            short_name = re.sub(pattern1, '', short_name, count=0)
            short_name = re.sub(pattern2, '', short_name, count=0)

            work_and_content= ea.find_all("span")
            if len(work_and_content)>1:
                working=False
            else:
                working = True
            working = str(working)

            work_and_content = work_and_content[-1].get_text().split('\n')



            # print(work_and_content)
            # print("work_and_content2++++++++++++++++++++++++++++++++++")

            for each in work_and_content:
                if len(each)<14:
                    work_and_content.pop(work_and_content.index(each))

            work_and_content_glued = ''#
            for each in work_and_content:
                work_and_content_glued = work_and_content_glued+str(each)

            # print(work_and_content_glued)
            name = re.search(r'(.){5,}(?=ИНН:)', work_and_content_glued,flags=re.MULTILINE)[0]
            try:
                inn = re.search(r'\d{5,}', work_and_content_glued,flags=re.MULTILINE)[0]
            except:
                inn = ''
            address = re.search(r'(?<=адрес:)(.){2,}', work_and_content_glued,flags=re.MULTILINE)[0]
            # address = re.sub(pattern1, '', work_and_content[0], count=0)
            list_of_orgs.append([link, short_name, name, working, address, inn])
    except Exception as e:
        print("List page parsing", "exception_in   ", url, "   with_page  ", link, " \n", e, "\n")
        log("LOGS","List page parsing","exception_in   ",url,"   with_page  ",link," \n", e, "\n")
    return list_of_orgs



def listorg_org_parser(page, url):
    soup = BeautifulSoup(page, features="html.parser")
    # print(soup.prettify())

    date=''
    profit =""
    costs =""
    inn =''
    kpp =''
    okpo =''
    ogrn = ''
    okopf =''
    okved =''

    # try:
    fin_results = re.search(r'(Сведения о доходах и расходах)(.){4,}\b', page, flags=re.MULTILINE)
    print(fin_results)
    if fin_results!=None:
        date = re.search(r'\d{2}\.\d{2}\.\d{4}',fin_results[0],flags=re.MULTILINE)[0]
        table2 = soup.find("td", class_="nwra")
        table3 = table2.find_parent()
        table4 = table3.find_all("td", class_="nwra")
        pattern_money = r'(\d{1,}(?:\ |\-|\)|\()*){1,}'
        profit =re.search(pattern_money,table4[0].get_text(),flags=re.MULTILINE)[0]
        costs =re.search(pattern_money,table4[1].get_text(),flags=re.MULTILINE)[0]
        print(profit)
        print(costs)

    # except Exception as e:
    #     print("ORGS EXCEPTION page parsing", "exception_in   ", url, "   MoneyData  ", "\n", e, "\n")
    #     log("LOGS", "ORGS EXCEPTION page parsing", "exception_in   ", url, "   MoneyData  ", "\n", e, "\n")


    try:
        table=soup.find("div", class_="c2").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        table2 = re.sub(r' {2,}','', table, count=0)
        table2 = re.sub(r'\n', '', table2, count=0)
        # print(table2)
        inn =re.search(r"(?<=ИНН:)(\d){1,}(?=КПП:)",table2,flags=re.MULTILINE)[0]
        kpp =re.search(r"(?<=КПП:)(\d){1,}(?=ОКПО:)",table2,flags=re.MULTILINE)[0]
        okpo =re.search(r"(?<=ОКПО:)(\d){1,}(?=ОГРН:)",table2,flags=re.MULTILINE)[0]
        ogrn = re.search(r"(?<=ОГРН:)(\d){1,}(?=ОКФС:)",table2,flags=re.MULTILINE)[0]
        okopf =re.search(r"(?<=ОКОПФ:)(\d){1,}",table2,flags=re.MULTILINE)[0]
    except Exception as e:
        print("ORGS EXCEPTION page parsing", "exception_in   ", url, "   with_INNS  ", "\n", e, "\n")
        log("LOGS","ORGS EXCEPTION page parsing", "exception_in   ", url, "   with_INNS  ", "\n", e, "\n")

    try:
        table = soup.find("div", class_="c2").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        # print(table)
        table2 = re.sub(r'\ {2,}','', table, count=0)
        table2 = re.sub(r'\n', '', table2, count=0)
        okved =re.search(r"(\d){1,}\.(\d){1,}",table2,flags=re.MULTILINE)[0]
    except Exception as e:
        print("ORGS EXCEPTION page parsing", "exception_in   ", url, "   with_OKVED  ", "\n", e, "\n")
        log("LOGS","ORGS EXCEPTION page parsing", "exception_in   ", url, "   with_OKVED  ", "\n", e, "\n")

    return inn,    kpp,    okpo,    ogrn,    okopf,    okved,    date,    profit,    costs







def scrape_List ():

    counter = 1
    url_Pattern = "https://www.list-org.com/list?okato=18401395"
    pages = "&page={}"  # .format(inn)
    url = ""
    session = get_session(url)

    while True:
        time.sleep(2.3)
        if counter >=1000:
            break
        counter+=1


        url = url_Pattern+pages.format(counter)
        rqst = session.get(url).content


        # url = "листtHTML.txt"
        # rqst = get_html(url)

        print(url)

        soup1 = BeautifulSoup(rqst, features="html.parser")
        soup1 = soup1.prettify()
        dump("list_of_orgs", url, soup1)


        page_list = listorg_list_parser(soup1, url)

        print(page_list)

        for each in page_list:
            url2 = each[0]
            short_name= each[1]
            name= each[2]
            working= each[3]
            address= each[4]
            inn= each[5]

            inn2=""
            kpp=""
            okpo=""
            ogrn=""
            okopf=""
            okved=""
            date=""
            profit=""
            costs=""
            time.sleep(3.1)
            if inn !="":
                # url2 = "https://www.list-org.com/company/12246550"
                session2 = get_session(url2)
                rqst = session2.get(url2).content

                # url2 = "листорг_организация.txt"
                # rqst = get_html(url2)

                soup1 = BeautifulSoup(rqst, features="html.parser")
                soup1 = soup1.prettify()
                dump("org_pages", url2, soup1)

                inn2, kpp, okpo, ogrn, okopf, okved, date, profit, costs = listorg_org_parser(soup1, url2)
                link = url2


                # short_name = 'https://www.list-org.com/company/1383977'
                # name = '"ВОЛГОГРАДСКАЯ ОМЦ "ПРЕОБРАЖЕНИЕ"'
                # working = "True"
                # address = "Г ВОЛГОГРАД,УЛ ДВИНСКАЯ,13..'"
                # inn = inn2
                print("url2", url2)
                print("short_name",short_name)
                print("name",name)
                print("working",working)
                print("address",address)
                print("inn",inn)
                print("inn2", inn2)
                print("kpp", kpp)
                print("okpo", okpo)
                print("ogrn", ogrn)
                print("okopf", okopf)
                print("okved", okved)
                print("date", date)
                print("profit", profit)
                print("costs", costs)

                functions.add_organization(link, short_name, name, working, address, inn, kpp, okpo, ogrn, okopf, okved, date, profit, costs)


    # https://www.list-org.com/company/12246550

def test_page():


    inn2=""
    kpp=""
    okpo=""
    ogrn=""
    okopf=""
    okved=""
    date=""
    profit=""
    costs=""


    # url2 = "https://www.list-org.com/company/12246550"
    # session2 = get_session(url2)
    # rqst = session2.get(url2).content



    url2 = "httpswww.list-org.comcompany1383977.txt"
    # url2 = "листорг_организация.txt"
    rqst = get_html(url2)

    soup1 = BeautifulSoup(rqst, features="html.parser")
    soup1 = soup1.prettify()
    dump("org_pages", url2, soup1)

    inn2, kpp, okpo, ogrn, okopf, okved, date, profit, costs = listorg_org_parser(soup1, url2)
    link = url2


    short_name = 'https://www.list-org.com/company/1383977'
    name = '"ВОЛГОГРАДСКАЯ ОМЦ "ПРЕОБРАЖЕНИЕ"'
    working = "True"
    address = "Г ВОЛГОГРАД,УЛ ДВИНСКАЯ,13..'"
    inn = inn2
    print("url2",url2)
    # print("short_name",short_name)
    # print("name",name)
    # print("working",working)
    # print("address",address)
    # print("inn",inn)
    print("inn2",inn2)
    print("kpp",kpp)
    print("okpo",okpo)
    print("ogrn",ogrn)
    print("okopf",okopf)
    print("okved",okved)
    print("date",date)
    print("profit",profit)
    print("costs",costs)



    functions.add_organization(link, short_name, name, working, address, inn, kpp, okpo, ogrn, okopf, okved, date, profit, costs)


    # https://www.list-org.com/company/12246550


if __name__ == '__main__':
    # test_page()
    scrape_List()


