from tkinter import Tk,Label,CENTER,Button,messagebox
from os import system,mkdir,name
from sys import platform
from requests import get
from pathlib import Path
import ctypes as ct

version = "5.7"

root = Tk()
root.title('Download Manager ' + str(version))
root.geometry('750x545')
root.resizable(width=False, height=False)

if platform == "win32":
    root.configure(bg='#000000')

elif platform == "linux" or platform == "linux2" or platform == "unix":
    pass


if platform == "win32":
    root.iconify()
    root.update()
    DWWMA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(root.winfo_id())
    renduring_policy = DWWMA_USE_IMMERSIVE_DARK_MODE
    value = 1
    value = ct.c_int(value)
    set_window_attribute(hwnd, renduring_policy, ct.byref(value), ct.sizeof(value))
    root.update_idletasks()

elif platform == "linux" or platform == "linux2" or platform == "unix":
    pass


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
                messagebox.showinfo(title="Успешно", message='HZF SMS Bomber был сохранен в папку $HOME\HZF Project')   
            
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
                messagebox.showinfo(title="Успешно", message='SMS Bomber был сохранен в папку C:\HZF Project')

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
                messagebox.showinfo(title="Успешно", message='Token Manager был сохранен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Успешно", message='Token Manager был сохранен в папку C:\HZF Project')

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
                messagebox.showinfo(title="Успешно", message='Email Bomber был сохранен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Успешно", message='Email Bomber был сохранен в папку C:\HZF Project')

def installWinControl():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                messagebox.showerror(title="Unsupported system", message="Ваша система не поддерживается!")

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
                messagebox.showinfo(title="Успешно", message='Windows Control был сохранен в папку C:\HZF Project')

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
                messagebox.showinfo(title="Успешно", message='Weather in your city был сохранен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Успешно", message='Weather in your city был сохранен в папку C:\HZF Project')

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
                messagebox.showinfo(title="Успешно", message='HZF Downloader Proxy был сохранен в папку $HOME\HZF Project')

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF Downloader Proxy.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Downloader-Proxy/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("pip3 install --upgrade pip")
                bib = ["requests", "termcolor"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                messagebox.showinfo(title="Успешно", message='HZF Downloader Proxy был сохранен в папку C:\HZF Project')

def installCsExCheat():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                messagebox.showerror(title="Unsupported system", message="Ваша система не поддерживается!")
                
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
                messagebox.showinfo(title="Успешно", message='HZF csgo external cheats был сохранен в папку C:\HZF Project')

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
                messagebox.showinfo(title="Успешно", message='HZF ORION Bomber был сохранен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Успешно", message='HZF ORION Bomber был сохранен в папку C:\HZF Project')     

def installpipupgrade():
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
                messagebox.showinfo(title="Успешно", message='Upgrade pip modules был сохранен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Успешно", message='Upgrade pip modules был сохранен в папку C:\HZF Project')     

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
                messagebox.showinfo(title="Успешно", message='HZF Tk Clock был сохранен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Успешно", message='HZF Tk Clock был сохранен в папку C:\HZF Project')    

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
                messagebox.showinfo(title="Успешно", message='TG AVA DOWNLOAD был сохранен в папку $HOME\HZF Project')    

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
                messagebox.showinfo(title="Успешно", message='TG AVA DOWNLOAD был сохранен в папку C:\HZF Project')    

def interupgrdmodules():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Integration-Upgrade-pip-modules-in-Windows.zip', "wb")
                ufr = get("https://github.com/AvenCores/Integration-Upgrade-pip-modules-in-Windows/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                messagebox.showinfo(title="Успешно", message='Integration Upgrade pip modules in Windows был сохранен в папку $HOME\HZF Project')    

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
                messagebox.showinfo(title="Успешно", message='Integration Upgrade pip modules in Windows был сохранен в папку C:\HZF Project')    

def installwinrarcrack():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Activator-WinRAR-crack.zip', "wb")
                ufr = get("https://github.com/AvenCores/Activator-WinRAR-crack/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("pip3 install --upgrade pip")
                bib = ["tk"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                system("mv HZF\ Project $HOME")
                messagebox.showinfo(title="Успешно", message='Activator WinRAR был сохранен в папку $HOME\HZF Project')  

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
                system("pip3 install --upgrade pip")
                bib = ["tk"]
                for i in range(len(bib)):
                    system("pip3 install "+bib[i])
                system('cls' if name == 'nt' else 'clear')
                messagebox.showinfo(title="Успешно", message='Activator WinRAR in Windows был сохранен в папку C:\HZF Project')    

def windowscleaner():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Windows-Cleaner.zip', "wb")
                ufr = get("https://github.com/AvenCores/Windows-Cleaner/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                messagebox.showinfo(title="Успешно", message='Windows Cleaner был сохранен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Успешно", message='Windows Cleaner in Windows был сохранен в папку C:\HZF Project')   

def terminalclock():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/HZF-Terminal-Clock.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Terminal-Clock/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                messagebox.showinfo(title="Успешно", message='Terminal Clock был сохранен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Успешно", message='Terminal Clock in Windows был сохранен в папку C:\HZF Project')   

def Autoinstallpipmodules():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Auto-install-pip-modules.zip', "wb")
                ufr = get("https://github.com/AvenCores/HZF-Auto-install-pip-modules/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                messagebox.showinfo(title="Успешно", message='Auto install pip modules был сохранен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Успешно", message='Auto install pip modules был сохранен в папку C:\HZF Project')   

def GiveMeBadgeRUS():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/GiveMeBadge-RUS', "wb")
                ufr = get("https://github.com/AvenCores/GiveMeBadge-RUS/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                messagebox.showinfo(title="Успешно", message='GiveMeBadge-RUS был сохранен в папку $HOME\HZF Project')   

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/GiveMeBadge-RUS', "wb")
                ufr = get("https://github.com/AvenCores/GiveMeBadge-RUS/archive/refs/heads/master.zip")
                f.write(ufr.content)
                f.close()
                messagebox.showinfo(title="Успешно", message='GiveMeBadge-RUS modules был сохранен в папку C:\HZF Project')   

def DenisLeadERTVMinecraftServercheck():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                Path("HZF Project").mkdir(parents=True, exist_ok=True)
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Denis-LeadER-TV-Minecraft-Server-check', "wb")
                ufr = get("https://github.com/AvenCores/Denis-LeadER-TV-Minecraft-Server-check/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                system("mv HZF\ Project $HOME")
                messagebox.showinfo(title="Успешно", message='Denis-LeadER-TV-Minecraft-Server-check был сохранен в папку $HOME\HZF Project')   

            elif platform == "win32":
                path = 'c:/HZF Project'
                try:
                    mkdir(path)
                except OSError as error:
                    False
                system('cls' if name == 'nt' else 'clear')
                f=open(r'c:/HZF Project/Denis-LeadER-TV-Minecraft-Server-check', "wb")
                ufr = get("https://github.com/AvenCores/Denis-LeadER-TV-Minecraft-Server-check/archive/refs/heads/main.zip")
                f.write(ufr.content)
                f.close()
                messagebox.showinfo(title="Успешно", message='Denis-LeadER-TV-Minecraft-Server-check modules был сохранен в папку C:\HZF Project') 

if platform == "win32":
    poetry = 'Поддерживаемое'
    label3 = Label(text=poetry, font="Ubuntu 12 bold", bg="#000000", fg='blue', justify=CENTER)
    label3.place(x=327, y=20)

    poetry = 'Неподдерживаемое'
    label3 = Label(text=poetry, font="Ubuntu 12 bold", bg="#000000", fg='red', justify=CENTER)
    label3.place(x=7, y=20)


elif platform == "linux" or platform == "linux2" or platform == "unix":
    poetry = 'Поддерживаемое'
    label3 = Label(text=poetry, font="Ubuntu 12 bold", fg='blue', justify=CENTER)
    label3.place(x=327, y=20)

    poetry = 'Неподдерживаемое'
    label3 = Label(text=poetry, font="Ubuntu 12 bold", fg='red', justify=CENTER)
    label3.place(x=7, y=20)

file = Button(text='Скачать HZF Bomber V1.4', command=installSMS)
file.place(x=10, y=60)

file = Button(text='Скачать HZF Email Bomber V1.1', command=installEmail)
file.place(x=10, y=100)

file = Button(text='Скачать HZF_VK_DIALOG_TOKEN', command=installVkTok)
file.place(x=10, y=140)

file = Button(text='HZF Windows Control V1.0', command=installWinControl)
file.place(x=10, y=180)

file = Button(text='HZF Weather in your city V2.0', command=installWeather)
file.place(x=10, y=260)

file = Button(text='Скачать HZF Downloader Proxy V2.0', command=installproxyinst)
file.place(x=330, y=140)

file = Button(text='Скачать HZF csgo external cheats V1.1', command=installCsExCheat)
file.place(x=10, y=220)

file = Button(text='Скачать HZF ORION Bomber V1.5.5 (LTS)', command=installHZFORIONBomber)
file.place(x=330, y=60)

file = Button(text='Скачать Upgrade pip modules V1.1', command=installpipupgrade)
file.place(x=330, y=180)

file = Button(text='Скачать HZF Tk Clock V2.6.1', command=installhzftkclock)
file.place(x=330, y=220)

file = Button(text='Скачать TG AVA DOWNLOAD V3.0', command=installtgavadwnld)
file.place(x=330, y=260)

file = Button(text='Скачать Integration Upgrade pip modules in Windows V3.3', command=interupgrdmodules)
file.place(x=330, y=300)

file = Button(text='Скачать Activator WinRAR V4.3', command=interupgrdmodules)
file.place(x=330, y=340)

file = Button(text='Скачать Windows Cleaner', command=windowscleaner)
file.place(x=330, y=380)

file = Button(text='Скачать Terminal Clock', command=terminalclock)
file.place(x=330, y=420)

file = Button(text='Скачать Auto install pip modules', command=Autoinstallpipmodules)
file.place(x=330, y=460)

file = Button(text='Скачать GiveMeBadge-RUS', command=GiveMeBadgeRUS)
file.place(x=330, y=100)

file = Button(text='Скачать Denis-LeadER-TV-Minecraft-Server-check', command=DenisLeadERTVMinecraftServercheck)
file.place(x=330, y=500)


if platform == "win32":
    poetry = 'Powered by HZF❤️'
    label3 = Label(text=poetry, justify=CENTER, bg="#000000", fg="white", font="Ubuntu 10 bold")
    label3.place(x=5, y=520)

elif platform == "linux" or platform == "linux2" or platform == "unix":
    poetry = 'Powered by HZF❤️'
    label3 = Label(text=poetry, justify=CENTER, font="Ubuntu 10 bold")
    label3.place(x=5, y=520)


if platform == "win32":
    root.deiconify()

elif platform == "linux" or platform == "linux2" or platform == "unix":
    pass

root.mainloop()
