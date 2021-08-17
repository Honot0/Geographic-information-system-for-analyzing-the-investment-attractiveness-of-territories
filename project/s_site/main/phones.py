# http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
# (?<=\|)(.+?)(?=\.|,)
# [^\s]*q(?!werty)[^\s]*
# (\d{1,}(?:\ |\-|\)|\()*){10,}



import re
# import tkinter as tk
# from tkinter.ttk import Combobox


from .models import Task3
from django.forms import ModelForm, Textarea, TimeField, Select

def make_list_of_phones(data):

    pattern1 = r"(\d{1,}(?:\ |\-|\)|\()*){10,11}"
    list_of_phones1 = []

    # file_handler = open(file_name)
    # for line in file_handler:
    #     print(line)
    #     for each1 in re.finditer(pattern1, line):
    #         list_of_phones1.append(each1[0])
    # file_handler.close()

    for each1 in re.finditer(pattern1, data, flags=re.MULTILINE):
        # print(each1[0])
        list_of_phones1.append(each1[0])


    list_of_phones2 = []
    for each2 in list_of_phones1:
        each2 = re.sub(r'\-', '', each2, count=0)
        each2 = re.sub(r'\ ', '', each2, count=0)
        each2 = re.sub(r'\(', '', each2, count=0)
        each2 = re.sub(r'\)', '', each2, count=0)
        each2 = re.sub(r'\+', '', each2, count=0)
        if len(each2)>=11:
            each2 = each2[1:]
        list_of_phones2.append(each2)

    list_of_phones1 = []
    for each in list_of_phones2:
        if len(each)>10:
            amount = int(len(each)/10)
            start = 0
            end = 10
            try:
                for i in range(amount):
                    list_of_phones1.append(each[start:end])
                    start = start+10
                    end=end+11
            except:
                print("ошибка 0 - старайтесь вводить по одному телефону в строке")
                pass
        else:
            list_of_phones1.append(each)

    list_of_phones2 = []
    for each in list_of_phones1:
        if len(each)>=11:
            each = each[1:]
        list_of_phones2.append(each)
    return list_of_phones2

# phones = make_list_of_phones("884444-4-44-43\n885555-5-55-66 89033746608")
# print(phones)

def add_pref(phones,add1):
    list_of_phones2 = []
    for each2 in phones:
        each2 = str(add1)+str(each2)
        list_of_phones2.append(each2)
    return list_of_phones2


def remake_to(phones,formatt):
    phones2 = []
    for each in phones:
        formatted =""
        get_num = 0
        for i in formatt:
            if re.match(r"\d", i):
                formatted=formatted + str(each[get_num])
                get_num+=1
            else:
                formatted=formatted + i
        phones2.append(formatted)
    return phones2





def extract_phones(theText, preNum, endNum):

    phones = make_list_of_phones(str(theText))
    phones = remake_to(phones,str(endNum))
    phones_with_pref=add_pref(phones,str(preNum))

    return phones_with_pref
    # text1.delete(1.0, tk.END)
    # for each in phones_with_pref[::-1] :
    #
    #     text1.insert(1.0, str(each))
    #     text1.insert(1.0, "\n")
    # pass


# def call():
#
#     data = text.get(1.0, tk.END)
#     # print(data)
#     phones = make_list_of_phones(data)
#     phones = remake_to(phones,combo2.get())
#     phones_with_pref=add_pref(phones,combo1.get())
#
#     text1.delete(1.0, tk.END)
#     for each in phones_with_pref[::-1] :
#
#         text1.insert(1.0, str(each))
#         text1.insert(1.0, "\n")
#     pass



# root = tk.Tk()
# canvas = tk.Canvas(root, height=500, width=1000)
# canvas.pack()
#
# text = tk.Text()
# text.pack()
# # entry = tk.Scrollbar(command=text.yview)
# text.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.3)
#
# combo1 = Combobox(canvas)
# combo1['values'] = ["8 ", "+7 ", "", "7 "]
# combo1.current(0)
# combo1.place(relx=0.1, rely=0.36, relwidth=0.4, relheight=0.05)
#
# combo2 = Combobox(canvas)
# combo2['values'] = ["(123) 456-78-90", "(123) 456 78 90", "123-456-78-90", "123 456 78 90", "123 456-78-90", "12-34-56-78-90", "12 34 56 78 90", "1234567890"]
# combo2.current(0)
# combo2.place(relx=0.5, rely=0.36, relwidth=0.4, relheight=0.05)
#
# button1 = tk.Button(root, text='поменять цифры', command=lambda: call())
# button1.place(relx=0.1, rely=0.43, relwidth=0.8, relheight=0.05)
#
# text1 = tk.Text(width=25, height=5)
# text1.pack()
# # entry1 = tk.Scrollbar(command=text1.yview)
# text1.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.35)
#
# root.mainloop()


