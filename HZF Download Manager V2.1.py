
import os
os.system("pip3 install tk requests")
from tkinter import *
from tkinter import messagebox
import time
import requests

root = Tk()
root.title('Download Manager V2.1')
root.geometry('350x170')
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
            ufr = requests.get("https://github.com/AvenCores/HZF-sms-bomber/releases/download/V1.2/HZF.SMS.BOMBER.V1.2.zip")
            f.write(ufr.content)
            f.close()

            os.system("pip3 install --upgrade pip")
            bib = ["tk", "colorama", "bs4", "as", "termcolor", "Label", "colored", "requests"]
            for i in range(len(bib)):
                os.system("pip3 install "+bib[i])
            os.system('cls')
            messagebox.showinfo(title="Удачно", message='SMS Bomber был скачен в папку C:\HZF Project')
            return "exit"

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
            messagebox.showinfo(title="Удачно", message='SMS Bomber был скачен в папку C:\HZF Project')
            return "exit"

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
            return "exit"

file = Button(text='Скачать HZF Bomber V1.2', command=installSMS)
file.pack()
file.place(x=11, y=26)
file = Button(text='Скачать HZF Email Bomber V1.1', command=installEmail)
file.pack()
file.place(x=11, y=63)
file = Button(text='Скачать HZF_VK_DIALOG_TOKEN', command=installVkTok)
file.pack()
file.place(x=11, y=100)
poetry = 'Downloader Manager V2.1 by HZF'
label3 = Label(text=poetry, justify=CENTER)
label3.place(x=10, y=145)
root.mainloop()
