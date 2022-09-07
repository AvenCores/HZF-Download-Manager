import os
import requests
from sys import platform
import pip._vendor.requests 
from pathlib import Path

version = 3.3

def installSMS():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'HZF Project/HZF SMS Bomber.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/HZF-sms-bomber/releases/download/V1.4/HZF.SMS.BOMBER.V1.4.zip")
                f.write(ufr.content)
                f.close()
                os.system("mv HZF\ Project $HOME")
                os.system("pip3 install --upgrade pip")
                bib = ["tk", "colorama", "bs4", "termcolor", "Label", "colored", "requests"]
                for i in range(len(bib)):
                    os.system("pip3 install "+bib[i])
                os.system('cls' if os.name == 'nt' else 'clear')
                global banner
                print(banner+"\nSMS Bomber был загружен в папку $HOME\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()
            
            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    os.mkdir(path)
                except OSError as error:
                    False
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF Bomber.zip',"wb")
                ufr = requests.get("https://github.com/AvenCores/HZF-sms-bomber/releases/download/V1.4/HZF.SMS.BOMBER.V1.4.zip")
                f.write(ufr.content)
                f.close()
                os.system("pip3 install --upgrade pip")
                bib = ["tk", "colorama", "bs4", "termcolor", "Label", "colored", "requests"]
                for i in range(len(bib)):
                    os.system("pip3 install "+bib[i])
                os.system('cls' if os.name == 'nt' else 'clear')
                print(banner+"\nSMS Bomber был загружен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()

def installVkTok():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'HZF Project/HZF_Vk_token_dialog.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/HZF_VK_DIALOG_TOKEN/releases/download/V1/HZF_VK_DIALOG_TOKEN.zip")
                f.write(ufr.content)
                f.close()
                os.system("mv HZF\ Project $HOME")
                os.system("pip3 install --upgrade pip")
                bib = ["requests", "as"]
                for i in range(len(bib)):
                    os.system("pip3 install "+bib[i])
                os.system('cls' if os.name == 'nt' else 'clear')
                global banner
                print(banner+"\nToken Manager был загружен в папку $HOME\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input() 

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    os.mkdir(path)
                except OSError as error:
                    False
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF_Vk_token_dialog.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/HZF_VK_DIALOG_TOKEN/releases/download/V1/HZF_VK_DIALOG_TOKEN.zip")
                f.write(ufr.content)
                f.close()
                os.system("pip3 install --upgrade pip")
                bib = ["requests", "as"]
                for i in range(len(bib)):
                    os.system("pip3 install "+bib[i])
                os.system('cls' if os.name == 'nt' else 'clear')
                print(banner+"\nToken Manager был загружен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()

def installEmail():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'HZF Project/HZF Email Bomber.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/HZF-Email-Bomber/releases/download/V1.1/Email.Bomber.zip")
                f.write(ufr.content)
                f.close()
                os.system("mv HZF\ Project $HOME")
                os.system("pip3 install --upgrade pip")
                os.system('cls' if os.name == 'nt' else 'clear')
                global banner
                print(banner+"\nEmail Bomber был загружен в папку $HOME\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    os.mkdir(path)
                except OSError as error:
                    False
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF Email Bomber.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/HZF-Email-Bomber/releases/download/V1.1/Email.Bomber.zip")
                f.write(ufr.content)
                f.close()
                print(banner+"\nEmail Bomber был загружен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()

def installWinControl():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                global banner
                print(banner+"\nWindows Control не поддерживает ваше систему!")
                input()

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    os.mkdir(path)
                except OSError as error:
                    False
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Windows Control.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/HZF-Windows-Control/releases/download/V1.0/Windows.Control.V1.0.zip")
                f.write(ufr.content)
                f.close()
                print(banner+"\nWindows Control был загружен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()

def installWeather():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'HZF Project/HZF Weather in your city.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/HZF-Weather/releases/download/V2.0/HZF.Weather.V2.0.zip")
                f.write(ufr.content)
                f.close()
                os.system("mv HZF\ Project $HOME")
                os.system("pip3 install --upgrade pip")
                os.system('cls' if os.name == 'nt' else 'clear')
                os.system("pip3 install --upgrade pip")
                bib = ["pyowm"]
                for i in range(len(bib)):
                    os.system("pip3 install "+bib[i])
                os.system('cls' if os.name == 'nt' else 'clear')
                global banner
                print(banner+"\nWeather in your city был загружен в папку $HOME\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    os.mkdir(path)
                except OSError as error:
                    False
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF Weather in your city.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/HZF-Weather/releases/download/V2.0/HZF.Weather.V2.0.zip")
                f.write(ufr.content)
                f.close()
                os.system("pip3 install --upgrade pip")
                bib = ["pyowm"]
                for i in range(len(bib)):
                    os.system("pip3 install "+bib[i])
                os.system('cls' if os.name == 'nt' else 'clear')
                print(banner+"\nWeather in your city был загружен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()

def installproxyinst():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                global banner
                print(banner+"\nHZF Downloader Proxy не поддерживает ваше систему!")
                input()

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    os.mkdir(path)
                except OSError as error:
                    False
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF Downloader Proxy.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/HZF-Downloader-Proxy/releases/download/V1.0/HZF.Downloader.Proxy.V1.0.zip")
                f.write(ufr.content)
                f.close()
                os.system("pip3 install --upgrade pip")
                bib = ["requests"]
                for i in range(len(bib)):
                    os.system("pip3 install "+bib[i])
                os.system('cls' if os.name == 'nt' else 'clear')
                print(banner+"\nHZF Downloader Proxy был загружен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()

def installCsExCheat():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                global banner
                print(banner+"\nHZF csgo external cheats не поддерживает ваше систему!")
                input()
                
            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    os.mkdir(path)
                except OSError as error:
                    False
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF csgo external cheats.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/CS-GO-external-cheat/releases/download/V1.1/HZF.csgo.cheats.V1.1.zip")
                f.write(ufr.content)
                f.close()
                os.system("pip3 install --upgrade pip")
                bib = ["requests", "pymem", "keyboard"]
                for i in range(len(bib)):
                    os.system("pip3 install "+bib[i])
                os.system('cls' if os.name == 'nt' else 'clear')
                print(banner+"\nHZF csgo external cheats был загружен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()

def installHZFORIONBomber():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'HZF Project/HZF-ORION-Bomber.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/HZF-ORION-Bomber/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                os.system("mv HZF\ Project $HOME")
                os.system("pip3 install --upgrade pip")
                os.system('cls' if os.name == 'nt' else 'clear')
                os.system("pip3 install --upgrade pip")
                bib = ["requests", "termcolor", "fake_useragent", "progress", "beautifulsoup4", "datetime"]
                for i in range(len(bib)):
                    os.system("pip3 install "+bib[i])
                os.system('cls' if os.name == 'nt' else 'clear')
                global banner
                print(banner+"\nHZF ORION Bomber был загружен в папку $HOME\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    os.mkdir(path)
                except OSError as error:
                    False
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF-ORION-Bomber.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/HZF-ORION-Bomber/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                os.system("pip3 install --upgrade pip")
                bib = ["requests", "termcolor", "fake_useragent", "progress", "beautifulsoup4", "datetime"]
                for i in range(len(bib)):
                    os.system("pip3 install "+bib[i])
                os.system('cls' if os.name == 'nt' else 'clear')
                print(banner+"\nHZF ORION Bomber был загружен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()

def installpipupgrade():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'HZF Project/Upgrade-pip-modules.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/Upgrade-pip-modules/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                os.system("mv HZF\ Project $HOME")
                os.system("pip3 install --upgrade pip")
                os.system('cls' if os.name == 'nt' else 'clear')
                global banner
                print(banner+"\nUpgrade pip modules был загружен в папку $HOME\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    os.mkdir(path)
                except OSError as error:
                    False
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Upgrade-pip-modules.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/Upgrade-pip-modules/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                print(banner+"\nUpgrade pip modules был загружен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()

def installhzftkclock():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'HZF Project/HZF-Tk-Clock.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/HZF-Tk-Clock/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                os.system("mv HZF\ Project $HOME")
                os.system("pip3 install --upgrade pip")
                os.system('cls' if os.name == 'nt' else 'clear')
                os.system("pip3 install --upgrade pip")
                bib = ["tk"]
                for i in range(len(bib)):
                    os.system("pip3 install "+bib[i])
                os.system('cls' if os.name == 'nt' else 'clear')
                global banner
                print(banner+"\nHZF Tk Clock был загружен в папку $HOME\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()   

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    os.mkdir(path)
                except OSError as error:
                    False
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF-Tk-Clock.zip', "wb")
                ufr = requests.get("https://github.com/AvenCores/HZF-Tk-Clock/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                os.system("pip3 install --upgrade pip")
                bib = ["tk"]
                for i in range(len(bib)):
                    os.system("pip3 install "+bib[i])
                os.system('cls' if os.name == 'nt' else 'clear')
                print(banner+"\nHZF Tk Clock был загружен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input() 

def installtgavadwnld():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'HZF Project/TG-AVA-DOWNLOAD.zip', "wb")
                ufr = requests.get("https://github.com/mr-mar493/tg-ava-download/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                os.system("mv HZF\ Project $HOME")
                os.system("pip3 install --upgrade pip")
                bib = ["Telethon"]
                for i in range(len(bib)):
                    os.system("pip3 install "+bib[i])
                os.system('cls' if os.name == 'nt' else 'clear')
                global banner
                print(banner+"\nTG AVA DOWNLOAD был загружен в папку $HOME\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input()   

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    os.mkdir(path)
                except OSError as error:
                    False
                os.system('cls' if os.name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/TG-AVA-DOWNLOAD.zip', "wb")
                ufr = requests.get("https://github.com/mr-mar493/tg-ava-download/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                os.system("pip3 install --upgrade pip")
                bib = ["Telethon"]
                for i in range(len(bib)):
                    os.system("pip3 install "+bib[i])
                os.system('cls' if os.name == 'nt' else 'clear')
                print(banner+"\nTG AVA DOWNLOAD был загружен в папку C:\HZF Project.\n\nНажмите ENTER для выхода в главное меню")
                input() 

def info():
    global banner, version
    print(banner+"\nВерсия "+str(version)+"\n\nЗа все действия с программой отвечаете только вы!\n\nСоздатель Telegram - @hzfnews\n\nНажмите ENTER чтобы выйти")
    input()

while True:
    banner = ("\n" * 100)+ """
 ______        __  __  __
|  _ \ \      / / |  \/  | __ _ _ __   __ _  __ _  ___ _ __
| | | \ \ /\ / /  | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| |_| |\ V  V /   | |  | | (_| | | | | (_| | (_| |  __/ |
|____/  \_/\_/    |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|
                                            |___/
YouTube Channel: youtube.com/c/HZFYT
Telegram Channel: t.me/hzfnews
VK: vk.com/hzforum1
    """

    print(banner)
    menu = input("Неподдерживаемое\n" + "1 - Скачать HZF Bomber V1.4\n2 - Скачать HZF Email Bomber V1.1\n3 - Скачать HZF_VK_DIALOG_TOKEN\n4 - Скачать HZF Windows Control V1.0\n5 - Скачать HZF csgo external cheats V1.1\n\n" + "Поддерживаемое\n" + "6 - Скачать HZF Weather in your city V2.0\n7 - Скачать HZF Downloader Proxy V1.0\n8 - Скачать HZF ORION Bomber V1.5\n9 - Скачать Upgrade pip modules V1.0\n10 - Скачать HZF Tk Clock V1.0\n11 - Скачать TG AVA DOWNLOAD V1.0" + "\n\n99 - Важная информация!\n\n0 - Выход\n")
    if menu == "0": exit()
    if menu == "1": installSMS()
    if menu == "2": installEmail()
    if menu == "3": installVkTok()
    if menu == "4": installWinControl()
    if menu == "5": installCsExCheat()
    if menu == "6": installWeather()
    if menu == "7": installproxyinst()
    if menu == "8": installHZFORIONBomber()
    if menu == "9": installpipupgrade()
    if menu == "10": installhzftkclock()
    if menu == "11": installtgavadwnld()
    if menu == "99": info()
