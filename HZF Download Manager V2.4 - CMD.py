import os
import time
import requests

version = 2.3

def installSMS():
            path = 'c:/HZF Project'
            try:
                os.mkdir(path)
            except OSError as error:
                False
            os.system('cls')
            f=open(r'c:/HZF Project/HZF Bomber.zip',"wb")
            ufr = requests.get("https://github.com/AvenCores/HZF-sms-bomber/releases/download/V1.2/HZF.SMS.BOMBER.V1.2.zip")
            f.write(ufr.content)
            f.close()

            os.system("pip3 install --upgrade pip")
            bib = ["tk", "colorama", "bs4", "as", "termcolor", "Label", "colored", "requests"]
            for i in range(len(bib)):
                os.system("pip3 install "+bib[i])
            os.system('cls')
            global banner
            print(banner+"\nSMS Bomber был скачен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
            input()

def installVkTok():
            path = 'c:/HZF Project'
            try:
                os.mkdir(path)
            except OSError as error:
                False
            os.system('cls')
            f=open(r'c:/HZF Project/HZF_Vk_token_dialog.zip', "wb")
            ufr = requests.get("https://github.com/AvenCores/HZF_VK_DIALOG_TOKEN/releases/download/V1/HZF_VK_DIALOG_TOKEN.zip")
            f.write(ufr.content)
            f.close()

            os.system("pip3 install --upgrade pip")
            bib = ["requests", "as"]
            for i in range(len(bib)):
                os.system("pip3 install "+bib[i])
            os.system('cls')
            global banner
            print(banner+"\nToken Manager был скачен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
            input()

def installEmail():
            path = 'c:/HZF Project'
            try:
                os.mkdir(path)
            except OSError as error:
                False
            os.system('cls')
            f=open(r'c:/HZF Project/HZF Email Bomber.zip', "wb")
            ufr = requests.get("https://github.com/AvenCores/HZF-Email-Bomber/releases/download/V1.1/Email.Bomber.zip")
            f.write(ufr.content)
            f.close()
            global banner
            print(banner+"\nEmail Bomber был скачен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
            input()

def installWinControl():
            path = 'c:/HZF Project'
            try:
                os.mkdir(path)
            except OSError as error:
                False
            os.system('cls')
            f=open(r'c:/HZF Project/Windows Control.zip', "wb")
            ufr = requests.get("https://github.com/AvenCores/HZF-Windows-Control/releases/download/V1.0/Windows.Control.V1.0.zip")
            f.write(ufr.content)
            f.close()
            global banner
            print(banner+"\nWindows Control был скачен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
            input()

def installWeather():
            path = 'c:/HZF Project'
            try:
                os.mkdir(path)
            except OSError as error:
                False
            os.system('cls')
            f=open(r'c:/HZF Project/HZF Weather in your city.zip', "wb")
            ufr = requests.get("https://github.com/AvenCores/HZF-Weather/releases/download/V1.1/HZF.Weather.V1.1.zip")
            f.write(ufr.content)
            f.close()

            os.system("pip3 install --upgrade pip")
            bib = ["pyowm"]
            for i in range(len(bib)):
                os.system("pip3 install "+bib[i])
            os.system('cls')
            global banner
            print(banner+"\nWeather in your city был скачен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
            input()

def info():
    global banner, version
    print(banner+"\nВерсия "+str(version)+"\n\nЗа все действия с программой отвечаете только вы!\n\nСоздатель Telegram - @avencores\n\nНажмите ENTER чтобы выйти")
    input()

while True:
    banner = ("\n" * 100)+ """
 ______        __  __  __
|  _ \ \      / / |  \/  | __ _ _ __   __ _  __ _  ___ _ __
| | | \ \ /\ / /  | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| |_| |\ V  V /   | |  | | (_| | | | | (_| | (_| |  __/ |
|____/  \_/\_/    |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|
                                            |___/
Telegram Channel: t.me/hzfnews
VK: vk.com/hzforum1
    """

    print(banner)
    menu = input("1 - Скачать HZF Bomber V1.2\n2 - Скачать HZF Email Bomber V1.1\n3 - Скачать HZF_VK_DIALOG_TOKEN\n4 - Скачать HZF Windows Control V1.0\n5 - Скачать HZF Weather in your city V1.1\n\n6 - Важная информация!\n\n0 - Выход\n")
    if menu == "0": exit()
    if menu == "1": installSMS()
    if menu == "2": installEmail()
    if menu == "3": installVkTok()
    if menu == "4": installWinControl()
    if menu == "5": installWeather()
    if menu == "6": info()
