try:

    input_jumlah_lagu = int(input('Berapa total lagu yang kamu mainkan : '))
    lagu = {}
    nama_lagu = None
    lagu_favorit = []

    if input_jumlah_lagu > 0:
        for _ in range(input_jumlah_lagu):
            input_lagu = input('Nama Lagu : ')
            input_total_played = int(input('Total Lagu Dimainkan : '))
            print()
            lagu.update({input_lagu:input_total_played})
            nama_lagu = list(lagu.keys())
            sorted_value = sorted(lagu.items(),key=lambda x: x[1],reverse=True)
        
    else:
        print('Lagu tidak boleh kurang dari 1')

    print(*nama_lagu,sep='\n')
    for i in sorted_value:
        lagu_favorit.append(i[0])
    print(f'Lagu Favorit : {lagu_favorit[0]}')


except ValueError:
    print('Mohon memasukkan untuk memasukkan data berupa angka')