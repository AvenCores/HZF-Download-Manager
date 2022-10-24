from os import system,mkdir,name
from turtle import color
from requests import get
from sys import platform
from pathlib import Path
from termcolor import colored

version = "4.2.1"

def installSMS():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'HZF Project/HZF SMS Bomber.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-sms-bomber/releases/download/V1.4/HZF.SMS.BOMBER.V1.4.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                system("pip3 install --upgrade pip")
                bib = ["tk", "colorama", "bs4", "termcolor", "Label", "colored", "requests"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                global banner
                global banner2
                global banner3
                global banner4
                global banner5
                global banner6
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nSMS Bomber был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()
            
            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF Bomber.zip',"wb")
                ufr = get("https://github.com/AvenCores/HZF-sms-bomber/releases/download/V1.4/HZF.SMS.BOMBER.V1.4.zip")
                f.write(ufr.content)
                f.close()
                system("pip3 install --upgrade pip")
                bib = ["tk", "colorama", "bs4", "termcolor", "Label", "colored", "requests"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nSMS Bomber был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()

def installVkTok():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'HZF Project/HZF_Vk_token_dialog.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF_VK_DIALOG_TOKEN/releases/download/V1/HZF_VK_DIALOG_TOKEN.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                system("pip3 install --upgrade pip")
                bib = ["requests", "as"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                global banner
                global banner2
                global banner3
                global banner4
                global banner5
                global banner6
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nToken Manager был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input() 

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF_Vk_token_dialog.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF_VK_DIALOG_TOKEN/releases/download/V1/HZF_VK_DIALOG_TOKEN.zip")
                f.write(ufr.content)
                f.close()
                system("pip3 install --upgrade pip")
                bib = ["requests", "as"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nToken Manager был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()

def installEmail():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'HZF Project/HZF Email Bomber.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Email-Bomber/releases/download/V1.1/Email.Bomber.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                system("pip3 install --upgrade pip")
                system('cls' if name == 'nt' else 'clear')
                global banner
                global banner2
                global banner3
                global banner4
                global banner5
                global banner6
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nEmail Bomber был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF Email Bomber.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Email-Bomber/releases/download/V1.1/Email.Bomber.zip")
                f.write(ufr.content)
                f.close()
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nEmail Bomber был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()

def installWinControl():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                global banner
                global banner2
                global banner3
                global banner4
                global banner5
                global banner6
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nWindows Control не поддерживает ваше систему!")
                input()

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Windows Control.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Windows-Control/releases/download/V1.0/Windows.Control.V1.0.zip")
                f.write(ufr.content)
                f.close()
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nWindows Control был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()

def installWeather():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'HZF Project/HZF Weather in your city.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Weather/releases/download/V2.0/HZF.Weather.V2.0.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                system("pip3 install --upgrade pip")
                system('cls' if name == 'nt' else 'clear')
                system("pip3 install --upgrade pip")
                bib = ["pyowm"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                global banner
                global banner2
                global banner3
                global banner4
                global banner5
                global banner6
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nWeather in your city был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF Weather in your city.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Weather/releases/download/V2.0/HZF.Weather.V2.0.zip")
                f.write(ufr.content)
                f.close()
                system("pip3 install --upgrade pip")
                bib = ["pyowm"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nWeather in your city был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()

def installproxyinst():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'HZF Project/HZF Downloader Proxy.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Downloader-Proxy/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                system("pip3 install --upgrade pip")
                system('cls' if name == 'nt' else 'clear')
                system("pip3 install --upgrade pip")
                bib = ["requests", "termcolor"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                global banner
                global banner2
                global banner3
                global banner4
                global banner5
                global banner6
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHZF Downloader Proxy был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF Downloader Proxy.zip', "wb")
                ufr = get("hhttps://github.com/AvenCores/HZF-Downloader-Proxy/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("pip3 install --upgrade pip")
                bib = ["requests", "termcolor"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHZF Downloader Proxy был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()

def installCsExCheat():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                global banner
                global banner2
                global banner3
                global banner4
                global banner5
                global banner6
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHZF csgo external cheats не поддерживает ваше систему!")
                input()
                
            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF csgo external cheats.zip', "wb")
                ufr = get("https://github.com/AvenCores/CS-GO-external-cheat/releases/download/V1.1/HZF.csgo.cheats.V1.1.zip")
                f.write(ufr.content)
                f.close()
                system("pip3 install --upgrade pip")
                bib = ["requests", "pymem", "keyboard"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHZF csgo external cheats был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()

def installHZFORIONBomber():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'HZF Project/HZF-ORION-Bomber.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-ORION-Bomber/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                system("pip3 install --upgrade pip")
                system('cls' if name == 'nt' else 'clear')
                system("pip3 install --upgrade pip")
                bib = ["requests", "termcolor", "fake_useragent", "progress", "beautifulsoup4", "datetime"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                global banner
                global banner2
                global banner3
                global banner4
                global banner5
                global banner6
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHZF ORION Bomber был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF-ORION-Bomber.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-ORION-Bomber/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                system("pip3 install --upgrade pip")
                bib = ["requests", "termcolor", "fake_useragent", "progress", "beautifulsoup4", "datetime"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHZF ORION Bomber был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()

def installpipupgrade():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'HZF Project/Upgrade-pip-modules.zip', "wb")
                ufr = get("https://github.com/AvenCores/Upgrade-pip-modules/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                system("pip3 install --upgrade pip")
                system('cls' if name == 'nt' else 'clear')
                global banner
                global banner2
                global banner3
                global banner4
                global banner5
                global banner6
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nUpgrade pip modules был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Upgrade-pip-modules.zip', "wb")
                ufr = get("https://github.com/AvenCores/Upgrade-pip-modules/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nUpgrade pip modules был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()

def installhzftkclock():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'HZF Project/HZF-Tk-Clock.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Tk-Clock/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                system("pip3 install --upgrade pip")
                system('cls' if name == 'nt' else 'clear')
                system("pip3 install --upgrade pip")
                bib = ["tk"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                global banner
                global banner2
                global banner3
                global banner4
                global banner5
                global banner6
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHZF Tk Clock был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF-Tk-Clock.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Tk-Clock/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("pip3 install --upgrade pip")
                bib = ["tk"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHZF Tk Clock был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input() 

def installtgavadwnld():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF-support-tg-ava-download.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-support-tg-ava-download/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                system("pip3 install --upgrade pip")
                bib = ["Telethon"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                global banner
                global banner2
                global banner3
                global banner4
                global banner5
                global banner6
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nTG AVA DOWNLOAD был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF-support-tg-ava-download.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-support-tg-ava-download/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("pip3 install --upgrade pip")
                bib = ["Telethon"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nTG AVA DOWNLOAD был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input() 

def interupgrdmodules():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Integration-Upgrade-pip-modules-in-Windows.zip', "wb")
                ufr = get("https://github.com/AvenCores/Integration-Upgrade-pip-modules-in-Windows/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                global banner
                global banner2
                global banner3
                global banner4
                global banner5
                global banner6
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nIntegration Upgrade pip modules был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Integration-Upgrade-pip-modules-in-Windows.zip', "wb")
                ufr = get("https://github.com/AvenCores/Integration-Upgrade-pip-modules-in-Windows/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nIntegration Upgrade pip был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

def info():
    global banner
    global banner2
    global banner3
    global banner4
    global banner5
    global banner6
    print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nАвтор данной утилиты не несет никакой ответственности за проделлание вами действия, все продукт команды HZF предостовляются только в азнокомительных целях!\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
    input()

while True:
    banner = ("\n" * 100) + colored("""
██████╗ ██╗    ██╗    ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
██╔══██╗██║    ██║    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██║  ██║██║ █╗ ██║    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██║  ██║██║███╗██║    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██████╔╝╚███╔███╔╝    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═════╝  ╚══╝╚══╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
    """, "green")
    banner2 = colored("[", "blue")+"Developers      :"+colored("HZF", "green")
    banner3 = colored("[", "blue")+"Version         :"+colored(version, "red")
    banner4 = colored("[", "blue")+"Telegram Channel:"+colored("@hzfnews", "cyan")+colored("              <-- Подпишись!", "green")
    banner5 = colored("[", "blue")+"YouTube Channel :"+colored("youtube.com/c/HZFYT", "cyan")+colored("   <-- Подпишись!", "green")
    banner6 = colored("[", "blue")+"VK              :"+colored("vk.com/hzforum1", "cyan")+colored("       <-- Подпишись!", "green")+"\n"

    print(banner)
    print(banner2)
    print(banner3)
    print(banner4)
    print(banner5)
    print(banner6)
    menu = input(colored("Неподдерживаемое\n", "red") + colored("1 ", "cyan") + "- Скачать HZF Bomber V1.4\n" + colored("2 ", "cyan") + "- Скачать HZF Email Bomber V1.1\n" + colored("3 ", "cyan") + "- Скачать HZF_VK_DIALOG_TOKEN\n" + colored("4 ", "cyan") + "- Скачать HZF Windows Control V1.0\n" + colored("5 ", "cyan") + "- Скачать HZF csgo external cheats V1.1\n\n" + colored("Поддерживаемое\n", "blue") +colored("6 ", "cyan") + "- Скачать HZF Weather in your city V2.0\n" + colored("7 ", "cyan") +  "- Скачать HZF Downloader Proxy V2.0\n" + colored("8 ", "cyan") + "- Скачать HZF ORION Bomber V1.5.2\n"  + colored("9 ", "cyan") + "- Скачать Upgrade pip modules V1.0\n" + colored("10 ", "cyan") +  "- Скачать HZF Tk Clock V2.2\n" + colored("11 ", "cyan") +  "- Скачать TG AVA DOWNLOAD V2.0\n" + colored("12 ", "cyan") + "- Скачать Integration Upgrade pip modules V2.0" + "\n\n" + colored("99 ", "cyan") + "- Важная информация!\n\n" + colored("0 ", "cyan") + "- Выход\n")
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
    if menu == "12": interupgrdmodules()
    if menu == "99": info()
