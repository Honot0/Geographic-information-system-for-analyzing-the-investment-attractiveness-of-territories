try:
    from helpTools import dump, get_right, log, get_html
except:
    from .helpTools import dump, get_right, log, get_html


from bs4 import BeautifulSoup
import re
from selenium.webdriver import Firefox
import time

''''
пост про регулярки
https://habr.com/ru/post/349860/
тестер регулярок
https://regex101.com/r/
документация бс
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
'''


# пример использования флажка
# import time
# done_flag=False
# while done_flag==False:
#     try:
#         print("stuff done")
#         done_flag=True
#     except:
#         print('stuff not done. Waiting')
#         time.sleep(1)


# http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
# (?<=\|)(.+?)(?=\.|,)
# [^\s]*q(?!werty)[^\s]*
# (\d{1,}(?:\ |\-|\)|\()*){10,}


def extractProfit(url):
    # url="https://sbis.ru/contragents/5013047887/504001001"
    # url = 'https://sbis.ru/contragents/5013047887/504001001'
    page = get_html(url)
    # dump("org_pages", "bis",page)

    # page= get_right("debug","html2","STRING")
    soup = BeautifulSoup(page, features="html.parser")
    table1 = soup.find_all("span", class_="cCard__BlockMaskSum")
    print(table1)
    profit = 0.0
    gain = 0.0
    compPrice = 0.0

    profitData = []
    for each in table1:
        each = str(each)
        digit = re.search(r"(\d{1,}(?:\ |\.)){1,6}", each, flags=re.MULTILINE)[0]
        # print(digit)
        profitData.append(float(digit))
    profitData.sort()
    try:
        profit = profitData[0]
    except:
        pass
    try:
        gain = profitData[1]
    except:
        pass
    try:
        compPrice = profitData[2]
    except:
        pass
    return profit, gain, compPrice


# print(extractProfit())


def getProfData(INN):
    profit = 0.0
    gain = 0.0
    compPrice = 0.0
    # INN = '5013047887'

    Current_url = 'https://sbis.ru/contragents'

    if Current_url == 'https://sbis.ru/contragents':
        browser = Firefox(executable_path="geckodriver", service_log_path="geckodriver.log")
        browser.get(Current_url)
        time.sleep(1)

        browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/div/div/input").click()
        browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/div/div/input").send_keys(
            INN)
        browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div[3]").click()
        time.sleep(2)
        html2 = browser.page_source
        soup1 = BeautifulSoup(html2, features="html.parser")
        soup1 = soup1.prettify()
        try:

            dump("debug", "html2", soup1)
        except:
            pass
        # print(extractProfit("trypage.txt"))
        browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/span[1]").click()
        time.sleep(4)

        yrl = browser.current_url
        profit, gain, compPrice = extractProfit(yrl)
        browser.close()
    return profit, gain, compPrice




















