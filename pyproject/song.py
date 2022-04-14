try:

    input_total_song = int(input('How Many Song : '))
    song = {}
    song_name = None
    fav_song = []

    if input_total_song > 0:
        for _ in range(input_total_song):
            input_song = input('Song Name : ')
            input_total_played = int(input('Total Songs Played : '))
            print()
            song.update({input_song:input_total_played})
            song_name = list(song.keys())
            sorted_song = sorted(song.items(),key=lambda x: x[1],reverse=True)
        
    else:
        print("Song Can't Be Less Than One!")

    print(*song_name,sep='\n')
    for i in sorted_song:
        fav_song.append(i[0])
    print(f'Favorite Song : {fav_song[0]}')


except ValueError:
    print('Value Error')
