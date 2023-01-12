from os import system,mkdir,name
from termcolor import colored
from requests import get
from sys import platform,argv
from pathlib import Path

version = 8

if "--updated" in argv:
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

    print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + f"Обновление завершено, вы успешно обновились до {version}" + colored(".\n\nНажмите ENTER для выхода в главное меню", "yellow"))
    input()

def removelasttxt():
    if platform == "win32":
        system("del /Q lastver.txt")
    elif platform == "linux" or platform == "linux2" or platform == "unix":
        system("rm -r lastver.txt")

def autoupdate():
    system('cls' if name == 'nt' else 'clear')
    global version

    f=open(r'lastver.txt', "wb")
    ufr = get("https://pastebin.com/raw/PHFVUtBM")
    f.write(ufr.content)
    f.close()

    num = open("lastver.txt")
    var = int(num.read())

    try:
        if var > version:
            upd_dwn=get('https://raw.githubusercontent.com/AvenCores/HZF-Download-Manager/main/HZF-Download-Manager-Terminal.py')
            f = open(r"HZF-Download-Manager-Terminal.py", "wb")
            f.write(upd_dwn.content)
            f.close()
            system("python HZF-Download-Manager-Terminal.py --updated")
            exit()
        elif var == version:
            system('cls' if name == 'nt' else 'clear')
            print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "Вы используете последнюю версию.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
            input()
        elif var < version:
            system('cls' if name == 'nt' else 'clear')
            print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "Ты явно ахуел.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
            input()
        else:
            system('cls' if name == 'nt' else 'clear')
            print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "Файл обновлений не найден.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
            input()
    except BaseException:
        system('cls' if name == 'nt' else 'clear')
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\Нету подключения к серверу, попробуйте позже.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
        input()

def installSMS():
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
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
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
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
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
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
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
            if platform == "linux" or platform == "linux2" or platform == "unix":
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nWindows Control не поддерживает данную систему!")
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
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
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
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
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
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
            if platform == "linux" or platform == "linux2" or platform == "unix":
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHZF csgo external cheats не поддерживает данную систему!")
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
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
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
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'HZF Project/Upgrade-pip-modules.zip', "wb")
                ufr = get("https://github.com/AvenCores/Upgrade-pip-modules/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                system('cls' if name == 'nt' else 'clear')
                system("pip3 install --upgrade pip")
                bib = ["setuptools"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
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
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
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
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
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
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Integration-Upgrade-pip-modules-in-Windows.zip', "wb")
                ufr = get("https://github.com/AvenCores/Integration-Upgrade-pip-modules-in-Windows/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
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

def installwinrarcrack():
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Activator-WinRAR-crack.zip', "wb")
                ufr = get("https://github.com/AvenCores/Activator-WinRAR-crack/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nActivator WinRAR modules был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Activator-WinRAR-crack.zip', "wb")
                ufr = get("https://github.com/AvenCores/Activator-WinRAR-crack/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nActivator WinRAR был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

def windowscleaner():
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Windows-Cleaner.zip', "wb")
                ufr = get("https://github.com/AvenCores/Windows-Cleaner/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nWindows Cleaner modules был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Windows-Cleaner.zip', "wb")
                ufr = get("https://github.com/AvenCores/Windows-Cleaner/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nWindows Cleaner был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

def terminalclock():
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF-Terminal-Clock.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Terminal-Clock/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nTerminal Clock был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF-Terminal-Clock.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Terminal-Clock/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nTerminal Clock был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

def Autoinstallpipmodules():
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Auto-install-pip-modules.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Auto-install-pip-modules/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nAuto install pip modules был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Auto-install-pip-modules.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Auto-install-pip-modules/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nAuto install pip modules был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

def GiveMeBadgeRUS():
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/GiveMeBadge-RUS.zip', "wb")
                ufr = get("https://github.com/AvenCores/GiveMeBadge-RUS/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nGiveMeBadge-RUS modules был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/GiveMeBadge-RUS.zip', "wb")
                ufr = get("https://github.com/AvenCores/GiveMeBadge-RUS/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nGiveMeBadge-RUS был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

def DenisLeadERTVMinecraftServercheck():
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Denis-LeadER-TV-Minecraft-Server-check.zip', "wb")
                ufr = get("https://github.com/AvenCores/Denis-LeadER-TV-Minecraft-Server-check/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nDenis-LeadER-TV-Minecraft-Server-check modules был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Denis-LeadER-TV-Minecraft-Server-check.zip', "wb")
                ufr = get("https://github.com/AvenCores/Denis-LeadER-TV-Minecraft-Server-check/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nDenis-LeadER-TV-Minecraft-Server-check был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

def integrtermclock():
            global banner
            global banner2
            global banner3
            global banner4
            global banner5
            global banner6
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Integration-Terminal-Clock-in-Windows.zip', "wb")
                ufr = get("https://github.com/AvenCores/Integration-Terminal-Clock-in-Windows/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nIntegration-Terminal-Clock-in-Windows modules был сохранен в папку $HOME\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Integration-Terminal-Clock-in-Windows.zip', "wb")
                ufr = get("https://github.com/AvenCores/Integration-Terminal-Clock-in-Windows/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nIntegration-Terminal-Clock-in-Windows был сохранен в папку C:\HZF Project.\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
                input()   

def info():
    global banner
    global banner2
    global banner3
    global banner4
    global banner5
    global banner6
    print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "HZF Download Manager - это простая утилита для скачивания всех утилит от HZF (avencores)." + "\n\nАвтор данной утилиты не несет никакой ответственности за проделлание вами действия, все продукт команды HZF предостовляются только в ознакомительных целях!\n\n" + "Разрабочик: avencores\n\n" + "Интерфейс: Terminal\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
    input()

while True:
    removelasttxt()
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
    menu = input(colored("Неподдерживаемое\n", "red") + colored("1 ", "cyan") + "- Скачать HZF Bomber V1.4\n" + colored("2 ", "cyan") + "- Скачать HZF Email Bomber V1.1\n" + colored("3 ", "cyan") + "- Скачать HZF_VK_DIALOG_TOKEN\n" + colored("4 ", "cyan") + "- Скачать HZF Windows Control V1.0\n" + colored("5 ", "cyan") + "- Скачать HZF csgo external cheats V1.1\n" + colored("6 ", "cyan") + "- Скачать HZF Weather in your city V2.0\n\n" + colored("Поддерживаемое\n", "blue") + colored("7 ", "cyan") +  "- Скачать HZF Downloader Proxy V2.0\n" + colored("8 ", "cyan") + "- Скачать HZF ORION Bomber V1.5.5 (LTS)\n"  + colored("9 ", "cyan") + "- Скачать Upgrade pip modules V3.2\n" + colored("10 ", "cyan") +  "- Скачать HZF Tk Clock V2.7\n" + colored("11 ", "cyan") +  "- Скачать TG AVA DOWNLOAD V3.0\n" + colored("12 ", "cyan") + "- Скачать Integration Upgrade pip modules V3.2\n" + colored("13 ", "cyan") + "- Скачать Activator WinRAR V4.3.1\n" + colored("14 ", "cyan") + "- Скачать Windows Cleaner\n" + colored("15 ", "cyan") + "- Скачать Terminal Clock\n" + colored("16 ", "cyan") + "- Скачать Auto install pip modules\n" + colored("17 ", "cyan") + "- Скачать GiveMeBadgeRUS\n" + colored("18 ", "cyan") + "- Скачать Denis-LeadER-TV-Minecraft-Server-check\n" + colored("19 ", "cyan") + "- Скачать Integration-Terminal-Clock-in-Windows V1.0" + "\n\n" + colored("88 ", "cyan") + "- Проверить обновления" + "\n\n" + colored("99 ", "cyan") + "- Важная информация!\n\n" + colored("0 ", "cyan") + "- Выход\n\n" + colored("HZF DOWNLOAD MANAGER ##>>", "red"))
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
    if menu == "13": installwinrarcrack()
    if menu == "14": windowscleaner()
    if menu == "15": terminalclock()
    if menu == "16": Autoinstallpipmodules()
    if menu == "17": GiveMeBadgeRUS()
    if menu == "18": DenisLeadERTVMinecraftServercheck()
    if menu == "19": integrtermclock()
    if menu == "88": autoupdate()
    if menu == "99": info()
    if menu == "0": exit()