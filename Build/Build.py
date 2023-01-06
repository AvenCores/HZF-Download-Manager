from sys import platform
from os import system

ver = 5.2

system("pyinstaller --clean -F --uac-admin ..\HZF-Download-Manager-Terminal-V" + str(ver) + ".py")
system("pyinstaller --clean -F --uac-admin ..\HZF-Download-Manager-Tinker-V" + str(ver) + ".pyw")

if platform == "win32":
    system("del /q *.spec")
    system("rd /s /q build")

if platform == "linux" or platform == "linux2" or platform == "unix":
    print("Для данной системы не поддерживается автоматическая сборка (возможно в будущем добавлю)!")
    input()
