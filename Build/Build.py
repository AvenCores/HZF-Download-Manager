from sys import platform
from os import system

ver = 5.4

if platform == "win32":
    system("rd /s /q build")
    system("rd /s /q dist")
    system("del /q *.spec")
    system("pyinstaller --clean -F --uac-admin ..\HZF-Download-Manager-Terminal-V" + str(ver) + ".py")
    system("pyinstaller --clean -F --uac-admin ..\HZF-Download-Manager-Tinker-V" + str(ver) + ".pyw")
    system("del /q *.spec")
    system("rd /s /q build")
    system("rd /s /q %USERPROFILE%\AppData\Local\pyinstaller")
    system("explorer dist")

if platform == "linux" or platform == "linux2" or platform == "unix":
    print("Для данной системы не поддерживается автоматическая сборка (возможно в будущем добавлю)!")
    input()
