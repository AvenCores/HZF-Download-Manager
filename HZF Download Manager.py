from tkinter import *
from tkinter import messagebox
import os
import time
import requests

version = 1.1
set = [1, 10]
fav_phones = []

root = Tk()
root.title('Download Manager')
root.geometry('350x140')
root.resizable(width=False, height=False)
os.system('cls' if os.name == 'nt' else 'clear')

def update():
    global version
    print("Проверка обновлений")
    try:
        upd=requests.get('https://raw.githubusercontent.com/AvenCores/HZF-Download-Manager/main/last_version.txt')
        upd_vers = float(upd.text[0:5])
        if upd_vers > version:
            print("Найдено обновление\n" + upd.text[0:5] + "\nИзменения:\n" + upd.text[7:])
            print("\nНачато обновление")
            upd_boom=requests.get('https://raw.githubusercontent.com/AvenCores/HZF-Download-Manager/main/HZF%20Download%20Manager.py')
            f = open("HZF Download Manager.py", "wb")
            f.write(upd_boom.content)
            f.close()
            print("\nОбновление завершено, откройте бомбер заново командой\npython HZF Download Manager.py")
            return "exit"
        elif upd_vers == version: print("Установлена последняя версия.")
        elif upd_vers < version: print("Не хочешь попасть в команду?")
        else: print("Ошибка, файл обновлений не найден")
    except BaseException:
        print("Нет интернета, попробуйте позже")

def downloadSms():
        path = 'c:/Bomber'
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)
        os.system('cls' if os.name == 'nt' else 'clear')
        f=open(r'c:/Bomber/HZF Bomber.zip',"wb")
        ufr = requests.get("https://github.com/AvenCores/HZF-sms-bomber/releases/download/V1.2/HZF.SMS.BOMBER.V1.2.zip")
        f.write(ufr.content)
        f.close()
        messagebox.showinfo(title="Удачно", message='SMS Bomber был скачен в папку C:\Bomber')
        return "exit"

def downloadEmail():
        path = 'c:/Bomber'
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)
        os.system('cls' if os.name == 'nt' else 'clear')
        f=open(r'c:/Bomber/HZF Email Bomber.zip', "wb")
        ufr = requests.get("https://github.com/AvenCores/HZF-Email-Bomber/releases/download/V1.1/Email.Bomber.zip")
        f.write(ufr.content)
        f.close()
        messagebox.showinfo(title="Удачно", message='Email Bomber был скачен в папку C:\Bomber')
        return "exit"

if update() == "exit": exit()
time.sleep(1)

file = Button(text='Скачать HZF Bomber V1.2', command=downloadSms)
file.pack()
file.place(x=11, y=26)
file = Button(text='Скачать HZF Email Bomber V1.1', command=downloadEmail)
file.pack()
file.place(x=11, y=63)
poetry = 'Downloader Manager by HZF'
label3 = Label(text=poetry, justify=CENTER)
label3.place(x=10, y=110)
root.mainloop()
