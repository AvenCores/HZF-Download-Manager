import os
from tkinter import *
from tkinter import messagebox
from sys import platform
import pip._vendor.requests 
import requests
from pathlib import Path

root = Tk()
root.title('Download Manager V3.4')
root.geometry('600x374')
root.resizable(width=False, height=False)

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
                messagebox.showinfo(title="Удачно", message='HZF SMS Bomber был загружен в папку $HOME\HZF Project')   
            
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
                messagebox.showinfo(title="Удачно", message='SMS Bomber был загружен в папку C:\HZF Project')

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
                messagebox.showinfo(title="Удачно", message='Token Manager был загружен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Удачно", message='Token Manager был загружен в папку C:\HZF Project')

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
                messagebox.showinfo(title="Удачно", message='Email Bomber был загружен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Удачно", message='Email Bomber был загружен в папку C:\HZF Project')

def installWinControl():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                messagebox.showinfo(title="Ошибка", message='Windows Control не поддерживает ваше систему!')

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
                messagebox.showinfo(title="Удачно", message='Windows Control был загружен в папку C:\HZF Project')

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
                messagebox.showinfo(title="Удачно", message='Weather in your city был загружен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Удачно", message='Weather in your city был загружен в папку C:\HZF Project')

def installproxyinst():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                messagebox.showinfo(title="Ошибка", message='Windows Control не поддерживает ваше систему!')

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
                messagebox.showinfo(title="Удачно", message='HZF Downloader Proxy был загружен в папку C:\HZF Project')

def installCsExCheat():
            if platform == "linux" or platform == "linux2" or platform == "unix":
                messagebox.showinfo(title="Ошибка", message='Windows Control не поддерживает ваше систему!')
                
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
                messagebox.showinfo(title="Удачно", message='HZF csgo external cheats был загружен в папку C:\HZF Project')

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
                messagebox.showinfo(title="Удачно", message='HZF ORION Bomber был загружен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Удачно", message='HZF ORION Bomber был загружен в папку C:\HZF Project')     

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
                messagebox.showinfo(title="Удачно", message='Upgrade pip modules был загружен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Удачно", message='Upgrade pip modules был загружен в папку C:\HZF Project')     

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
                messagebox.showinfo(title="Удачно", message='HZF Tk Clock был загружен в папку $HOME\HZF Project')   

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
                messagebox.showinfo(title="Удачно", message='HZF Tk Clock был загружен в папку C:\HZF Project')    

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
                messagebox.showinfo(title="Удачно", message='TG AVA DOWNLOAD был загружен в папку $HOME\HZF Project')    

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
                messagebox.showinfo(title="Удачно", message='TG AVA DOWNLOAD был загружен в папку C:\HZF Project')    

poetry = 'Неподдерживаемое'
label3 = Label(text=poetry, font='bold', fg='red', justify=CENTER)
label3.place(x=11, y=20)

poetry = 'Поддерживаемое'
label3 = Label(text=poetry, font='bold', fg='blue', justify=CENTER)
label3.place(x=330, y=20)

file = Button(text='Скачать HZF Bomber V1.4', command=installSMS)
file.place(x=11, y=60)

file = Button(text='Скачать HZF Email Bomber V1.1', command=installEmail)
file.place(x=11, y=100)

file = Button(text='Скачать HZF_VK_DIALOG_TOKEN', command=installVkTok)
file.place(x=11, y=140)

file = Button(text='HZF Windows Control V1.0', command=installWinControl)
file.place(x=11, y=180)

file = Button(text='HZF Weather in your city V2.0', command=installWeather)
file.place(x=330, y=100)

file = Button(text='Скачать HZF Downloader Proxy V1.0', command=installproxyinst)
file.place(x=330, y=140)

file = Button(text='Скачать HZF csgo external cheats V1.1', command=installCsExCheat)
file.place(x=11, y=220)

file = Button(text='Скачать HZF ORION Bomber V1.5', command=installHZFORIONBomber)
file.place(x=330, y=60)

file = Button(text='Скачать Upgrade pip modules V1.0', command=installpipupgrade)
file.place(x=330, y=180)

file = Button(text='Скачать HZF Tk Clock V1.0', command=installhzftkclock)
file.place(x=330, y=220)

file = Button(text='Скачать TG AVA DOWNLOAD V1.0', command=installtgavadwnld)
file.place(x=330, y=260)

poetry = 'Downloader Manager V3.4 by HZF'
label3 = Label(text=poetry, justify=CENTER)
label3.place(x=160, y=350)
root.mainloop()
