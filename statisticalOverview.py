from collections import Counter
import sys
from functools import reduce, partial
import multiprocessing
sys.path.append('..')


def listNormalize(listToNormalize):
    divisor = max(listToNormalize)
    pool = multiprocessing.Pool()
    func = partial(normalizeCount, divisor)
    playListNormalized = pool.map(func, listToNormalize)
    pool.close()
    pool.join()
    return playListNormalized


def normalizeCount(down, top):
    return "{0:.2f}".format(top/down)



def songPlayCount(preferenceSet):
    playList = {}
    for song in preferenceSet.song_id.unique():
        lines = preferenceSet.loc[preferenceSet['song_id'] == song]
        playList[song] = reduce(lambda x, y: x + y, lines['play_count'].tolist())
    return playList


def saveSongPlayCount(playList):
    toSaveFile = open(
        'data/overview/songPlayCount.csv',
        'w+'
    )
    toSaveFile.write('song_play_count\n')
    for song in playList:
        toSaveFile.write(str(song) + '\n')
    toSaveFile.close()


def songPreferenceCount(preferenceSet):
    return Counter(preferenceSet["song_id"].tolist())


def saveSongPreferenceCount(preferenceList):
    toSaveFile = open(
        'data/overview/songPreferenceCount.csv',
        'w+'
    )
    toSaveFile.write('song_preference_count\n')
    for song in preferenceList:
        toSaveFile.write(str(song) + '\n')
    toSaveFile.close()


def userPreferenceCount(preferenceSet):
    return Counter(preferenceSet["user_id"].tolist())


def userSongPreferenceCount(preferenceList):
    toSaveFile = open(
        'data/overview/userPreferenceCount.csv',
        'w+'
    )
    toSaveFile.write('user_preference_count\n')
    for user in preferenceList:
        toSaveFile.write(str(user) + '\n')
    toSaveFile.close()


def painelSongs(preferenceSet):
    print('Total de musicas diferentes ouvidas: ', len(set(preferenceSet["song_id"].tolist())))
    print('Total de usuarios diferentes: ', len(set(preferenceSet["user_id"].tolist())))


def statisticalOverview(songSet, preferenceSet):
    #
    song_preference_set_counted = songPreferenceCount(preferenceSet)
    song_preference_set_normalized = listNormalize(song_preference_set_counted.values())
    saveSongPreferenceCount(song_preference_set_normalized)
    #
    user_preference_set_counted = userPreferenceCount(preferenceSet)
    user_preference_set_normalized = listNormalize(user_preference_set_counted.values())
    userSongPreferenceCount(user_preference_set_normalized)
    #
    song_play_set_counted = songPlayCount(preferenceSet)
    song_play_set_normalized = listNormalize(song_play_set_counted.values())
    saveSongPlayCount(song_play_set_normalized)
    #
    painelSongs(preferenceSet)
