from collections import Counter
import sys
from functools import reduce, partial
import multiprocessing
sys.path.append('..')


def normalizeCount(down, top):
    return "{0:.2f}".format(top/down)



def songPlayCount(preferenceSet):
    playList = []
    for song in preferenceSet.song_id.unique():
        lines = preferenceSet.loc[preferenceSet['song_id'] == song]
        playList.append(reduce(lambda x, y: x + y, lines['play_count'].tolist()))
    divisor = max(playList)
    pool = multiprocessing.Pool()
    func = partial(normalizeCount, divisor)
    playListNormalized = pool.map(func, playList)
    pool.close()
    pool.join()
    return playListNormalized


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
    countedPreferenceList = Counter(preferenceSet["song_id"].tolist()).values()
    divisor = max(countedPreferenceList)
    pool = multiprocessing.Pool()
    func = partial(normalizeCount, divisor)
    listNormalized = pool.map(func, countedPreferenceList)
    pool.close()
    pool.join()
    return listNormalized


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
    countedPreferenceList = Counter(preferenceSet["user_id"].tolist()).values()
    divisor = max(countedPreferenceList)
    pool = multiprocessing.Pool()
    func = partial(normalizeCount, divisor)
    listNormalized = pool.map(func, countedPreferenceList)
    pool.close()
    pool.join()
    return listNormalized


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
    saveSongPreferenceCount(songPreferenceCount(preferenceSet))
    userSongPreferenceCount(userPreferenceCount(preferenceSet))
    saveSongPlayCount(songPlayCount(preferenceSet))
    painelSongs(preferenceSet)
