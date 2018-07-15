from random import choice


def interface_menu(groot):
    songs_start_and_end = {}
    print('*' * 50)
    print('*' * 16 + 'Escolha das Músicas' + '*' * 15)
    print('*' * 50)
    print('+ Abre o arquivo e escolha duas músicas: data/set/songSet.csv')
    print('-' * 50)
    songs_start_and_end['start'] = groot.get_song_position(str(input('+ Digite a song_id da música de inicio: ')))
    while songs_start_and_end['start'] == '':
        print('+ + Música não encontrada!')
        songs_start_and_end['start'] = groot.get_song_position(str(input('+ Digite a song_id da música de inicio: ')))
    songs_start_and_end['end'] = groot.get_song_position(str(input('+ Digite a song_id da música de termino: ')))
    while songs_start_and_end['end'] == '':
        print('+ + Música não encontrada!')
        songs_start_and_end['end'] = groot.get_song_position(str(input('+ Digite a song_id da música de termino: ')))
    return songs_start_and_end


def random_choice(groot):
    songs_start_and_end = {}
    song_set = groot.get_song_set()['song_id']
    songs_start_and_end['start'] = groot.get_song_position(str(choice(song_set)))
    while songs_start_and_end['start'] == '':
        songs_start_and_end['start'] = groot.get_song_position(str(choice(song_set)))
    songs_start_and_end['end'] = groot.get_song_position(str(choice(song_set)))
    while songs_start_and_end['end'] == '':
        songs_start_and_end['end'] = groot.get_song_position(str(choice(song_set)))
    return songs_start_and_end
