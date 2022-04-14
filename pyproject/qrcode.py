import qrcode
import os

img = qrcode.make(input('Input Link : '))
file_name = input('File Name : ')
destination = f"D:\\TobDev\\QrCode\\{file_name}.png" 

if img != None:
    img.save(f'{file_name}.png')

    if os.path.exists(destination):
        print(f'{file_name}.png is already exist')
    else:
        os.replace(f'{file_name}.png', destination)
        print(f'Data : "{file_name}.png" was added')
        img.show()
else:
    print('Wrong data input')
