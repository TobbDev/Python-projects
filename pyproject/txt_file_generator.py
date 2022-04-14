import os

inputFileName = input('File Name : ') 
destination = f"D:\\TobDev\\TextGenerator\\{inputFileName}.txt"

with open(f"{inputFileName}.txt", "a") as fileGenerate:
    command = ''
    while command != 'Done':
        command = input('Input Command (Write / Done): ')
        if command == 'Done':
            break
        if command == 'Write':
            inputWord = input('Input Word : ')
            fileGenerate.write(f'{inputWord} \n')

os.replace(f'{inputFileName}.txt',destination)
