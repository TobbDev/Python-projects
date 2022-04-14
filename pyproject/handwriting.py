from platform import system
import pywhatkit as pw
import os


if system().lower() == "windows":
    inputFileName = input("File Name : ")
    destination = f"D:\\TobDev\\Handwriting\\{inputFileName}.png"
    text = []
    inputUser = int(input("How Many Line : "))
    for _ in range(inputUser):
        inputText = input('Text : ')
        text.append(f"{inputText}")
    text = "\n".join(text)
    pw.text_to_handwriting(text, save_to=f'{inputFileName}.png')
else:
    print('Your Operating System Must Be Windows')

os.replace(f'{inputFileName}.png',destination)
