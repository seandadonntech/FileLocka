import os

task = input("Do you want to install all packages require for this repo? type help to see commands[+]\n")

if task =="1":
    os.system("pip install click")
    os.system("pip install inquirer")
    os.system("pip install cryptography")
    os.system("pip install os")
    print("All set all packages installed !")
if task =="2":
 print("ok you dont want to install program closed")

if task == "3":
 os.system("pip uninstall click")
 os.system("pip uninstall inquirer")
 os.system("pip uninstall cryptography")
 os.system("pip uninstall os")
 print("ok everything uninstalled")
elif task =="help":
 print("Enter 1 to install packages 2 you dont and 3 for help ")

else:
 print("invalid command")
#this program will install the need requirements