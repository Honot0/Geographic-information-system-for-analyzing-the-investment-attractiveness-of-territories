import os.path
import time
import re
import ast
import requests
import json


def get_time():
    ttt=(str("{}.{}.{} / {}:{}".format(time.localtime().tm_year, time.localtime().tm_mon,
                                             time.localtime().tm_mday, time.localtime().tm_hour,
                                             time.localtime().tm_min, )))
    return ttt
# print(get_time())

def write_in_file(file_name,text_in, *args,need_time = True ):
    file_name = re.sub(r'\\|\:|\*|\?|\"|\<|\>|\|',"",file_name, count=0)
    file = open(file_name, "w", encoding="utf-8")
    # print(type(text_in))
    # print(text_in)
    file.write(str(text_in))
    # file.writelines(text_in)
    if need_time == True:
        file.write(get_time())
        file.write('\n')

    for each in args:
        file.write(str(each))
    file.write('\n\n')
    file.close()




def log(folder_name,file_name, *args):
    file_name = file_name+".txt"
    text_in = ''
    file_name = re.sub(r'\\|\/|\:|\*|\?|\"|\<|\>|\|', "", file_name, count=0)

    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

    done_flag = False
    while done_flag==False:
        try:
            if os.path.exists(folder_name+"/"+file_name) == False:
                write_in_file(folder_name+"/"+file_name, text_in, args)
            else:
                file = open(folder_name+"/"+file_name, "r", encoding="utf-8")
                text_in = file.read()
                file.close()
                write_in_file(folder_name+"/"+file_name,text_in, args)


            print("logged ", file_name)
            done_flag=True
        except Exception as e:

            print('logging failed', e)
            time.sleep(0.4)


def dump(folder_name,file_name, data):
    file_name = file_name+".txt"
    file_name = re.sub(r'\\|\/|\:|\*|\?|\"|\<|\>|\|', "", file_name, count=0)
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    write_in_file(folder_name+"/"+file_name,data,need_time = False)




def get_right(folder_name,file_name, result_type = "LIST"):
    file_name = folder_name + "/" +file_name + ".txt"
    file = open(file_name, "r", encoding="utf-8")
    text_in = file.read()
    file.close()
    for_return=None
    if result_type == "LIST":
        for_return = ast.literal_eval(text_in)  # штука переводящая строку формата листа в лист
    if result_type == "STRING":
        for_return = str(text_in)
    if result_type == "DICT":
        res_bytes = json.dumps(text_in).encode('utf-8')
        res_dict = json.loads(res_bytes.decode('utf-8'))
        # print(type(res_dict))
        # print(res_dict)
        res_dict = re.sub(r"'", '"', res_dict, count=0)
        for_return = json.loads(res_dict)
    return for_return


def download_file(link):#download_file(folder_name,file_name,link):
    fileName = str(link[-9:])
    r = requests.get(link)
    with open(fileName, 'wb') as f:
        f.write(r.content)
    print(fileName, "downloaded")

#универсальная функция для открытия страниц в интернете или на локальной машине в зависимости от названия.
def get_html(url):
    from bs4 import BeautifulSoup
    if bool(re.search(r'[а-яА-Я]', url)) or  bool(re.search(r'\.txt', url)) :
        response = open(url, encoding='utf-8').read()
        print("local_open")
        return response
    else:
        response = requests.get(url)#, params=headers)
        soup1 = BeautifulSoup(response.content, features="html.parser")
        soup1 = soup1.prettify()
        print("INTERNET_OPEN!")
        return soup1


if __name__ == '__main__':
    print("log('folder_name','file_name',arg1,arg2,argN)")
    print('dump("dumpFolder", "dumpFile", "data")')
    print('get_right("folder_name", "file_name", result_type="LIST")')

    url = "листорг_организация.txt"
    link = "https://translate.google.ru/?sl=en&tl=ru&text=retryes&op=translate"
    e = "fdfdfsdfsrtwrq"
    data = 'link, " \n"link, " \n"link, " \n"link, " \n"link, " \n"'

    # log("folder_name","List page parsing", "exception_in   ", url, "   with_page  ", link, " \n", e, "\n")
    # dump("folder_name","file_name", data)