from os import system,name
from sys import platform

if platform == "win32":
        print("Установка библиотек")
        system("pip3 install --upgrade pip")
        bib = ["requests","tk","pyinstaller","chardet"]
        for i in range(len(bib)):
                system("pip3 install "+bib[i])
        system('cls' if name == 'nt' else 'clear')
        print("Установка завершена!")
        print("\nНажмите Enter чтобы закрыть")
        input()

elif platform == "linux" or platform == "linux2" or platform == "unix":
        print("Установка библиотек")
        system("pip3 install --upgrade pip")
        bib = ["requests","pyinstaller","chardet"]
        for i in range(len(bib)):
                system("pip3 install "+bib[i])
        system('cls' if name == 'nt' else 'clear')
        print("Установка не полностью завершена, установите вручную tk!")
        print("\nНажмите Enter чтобы закрыть")
        input()
