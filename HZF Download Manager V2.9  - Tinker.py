import os
from tkinter import *
from tkinter import messagebox
import requests

root = Tk()
root.title('Download Manager V2.9')
root.geometry('350x318')
root.resizable(width=False, height=False)
os.system('cls')

def installSMS():
            path = 'c:/HZF Project'
            try:
                os.mkdir(path)
            except OSError as error:
                False
            os.system('cls')
            f=open(r'c:/HZF Project/HZF Bomber.zip',"wb")
            ufr = requests.get("https://github.com/AvenCores/HZF-sms-bomber/releases/download/V1.4/HZF.SMS.BOMBER.V1.4.zip")
            f.write(ufr.content)
            f.close()

            os.system("pip3 install --upgrade pip")
            bib = ["tk", "colorama", "bs4", "termcolor", "Label", "colored", "requests"]
            for i in range(len(bib)):
                os.system("pip3 install "+bib[i])
            os.system('cls')
            messagebox.showinfo(title="Удачно", message='SMS Bomber был скачен в папку C:\HZF Project')

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
            messagebox.showinfo(title="Удачно", message='Token Manager был скачен в папку C:\HZF Project')

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
            messagebox.showinfo(title="Удачно", message='Email Bomber был скачен в папку C:\HZF Project')

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
            messagebox.showinfo(title="Удачно", message='Windows Control был скачен в папку C:\HZF Project')

def installWeather():
            path = 'c:/HZF Project'
            try:
                os.mkdir(path)
            except OSError as error:
                False
            os.system('cls')
            f=open(r'c:/HZF Project/HZF Weather in your city.zip', "wb")
            ufr = requests.get("https://github.com/AvenCores/HZF-Weather/releases/download/V2.0/HZF.Weather.V2.0.zip")
            f.write(ufr.content)
            f.close()

            os.system("pip3 install --upgrade pip")
            bib = ["pyowm"]
            for i in range(len(bib)):
                os.system("pip3 install "+bib[i])
            os.system('cls')
            messagebox.showinfo(title="Удачно", message='Weather in your city был скачен в папку C:\HZF Project')

def installproxyinst():
            path = 'c:/HZF Project'
            try:
                os.mkdir(path)
            except OSError as error:
                False
            os.system('cls')
            f=open(r'c:/HZF Project/HZF Downloader Proxy.zip', "wb")
            ufr = requests.get("https://github.com/AvenCores/HZF-Downloader-Proxy/releases/download/V1.0/HZF.Downloader.Proxy.V1.0.zip")
            f.write(ufr.content)
            f.close()

            os.system("pip3 install --upgrade pip")
            bib = ["requests"]
            for i in range(len(bib)):
                os.system("pip3 install "+bib[i])
            os.system('cls')
            messagebox.showinfo(title="Удачно", message='HZF Downloader Proxy был скачен в папку C:\HZF Project')

def installCsExCheat():
            path = 'c:/HZF Project'
            try:
                os.mkdir(path)
            except OSError as error:
                False
            os.system('cls')
            f=open(r'c:/HZF Project/HZF csgo external cheats.zip', "wb")
            ufr = requests.get("https://github.com/AvenCores/CS-GO-external-cheat/releases/download/V1.1/HZF.csgo.cheats.V1.1.zip")
            f.write(ufr.content)
            f.close()

            os.system("pip3 install --upgrade pip")
            bib = ["requests", "pymem", "keyboard"]
            for i in range(len(bib)):
                os.system("pip3 install "+bib[i])
            os.system('cls')
            messagebox.showinfo(title="Удачно", message='HZF csgo external cheats был скачен в папку C:\HZF Project')

file = Button(text='Скачать HZF Bomber V1.4', command=installSMS)
file.pack()
file.place(x=11, y=26)
file = Button(text='Скачать HZF Email Bomber V1.1', command=installEmail)
file.pack()
file.place(x=11, y=63)
file = Button(text='Скачать HZF_VK_DIALOG_TOKEN', command=installVkTok)
file.pack()
file.place(x=11, y=100)
file = Button(text='HZF Windows Control V1.0', command=installWinControl)
file.place(x=11, y=137)
file = Button(text='HZF Weather in your city V2.0', command=installWeather)
file.place(x=11, y=174)
file = Button(text='Скачать HZF Downloader Proxy V1.0', command=installproxyinst)
file.place(x=11, y=211)
file = Button(text='Скачать HZF csgo external cheats V1.1', command=installCsExCheat)
file.place(x=11, y=248)
poetry = 'Downloader Manager V2.9 by HZF'
label3 = Label(text=poetry, justify=CENTER)
label3.place(x=10, y=287)
root.mainloop()
