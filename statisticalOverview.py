# -*- coding: utf-8 -*-
from collections import Counter
from statistics import median, mean
import numpy as np
import pandas as pd
import sys
from functools import reduce, partial
import multiprocessing
sys.path.append('..')


def list_normalize(list_to_normalize):
    pool = multiprocessing.Pool()
    playListNormalized = pool.map(partial(normalizeCount, max(list_to_normalize)), list_to_normalize)
    pool.close()
    pool.join()
    return playListNormalized


def dictNormalize(dict_to_normalize):
    values = dict_to_normalize.values()
    divisor = max(values)
    pool = multiprocessing.Pool()
    playListNormalized = pool.map(partial(normalizeCount, divisor), values)
    pool.close()
    pool.join()
    dict_to_return = {}
    i = 0
    for item in dict_to_normalize:
        dict_to_return[item] = float(playListNormalized[i])
        i += 1
    return dict_to_return


def normalizeCount(down, top):
    return float("{0:.4f}".format(float(float(top)/float(down))))



def songPlayCount(preferenceSet):
    playList = {}
    for song in preferenceSet.song_id.unique():
        lines = preferenceSet.loc[preferenceSet['song_id'] == song]
        playList[song] = float(reduce(lambda x, y: x + y, lines['play_count'].tolist()))
    return playList


def saveSongPlayCount(playList):
    toSaveFile = open(
        'data/overview/songPlayCount.csv',
        'w+'
    )
    toSaveFile.write('id,song_play_count\n')
    for song in playList:
        toSaveFile.write(str(song) + ',' + str(playList[song]) + '\n')
    toSaveFile.close()


def songPreferenceCount(preferenceSet):
    return Counter(preferenceSet["song_id"].tolist())


def saveSongPreferenceCount(preferenceList):
    toSaveFile = open(
        'data/overview/songPreferenceCount.csv',
        'w+'
    )
    toSaveFile.write('id,song_preference_count\n')
    for song in preferenceList:
        toSaveFile.write(str(song) + ',' + str(preferenceList[song]) + '\n')
    toSaveFile.close()


def userPreferenceCount(preferenceSet):
    return Counter(preferenceSet["user_id"].tolist())


def userSongPreferenceCount(preferenceList):
    toSaveFile = open(
        'data/overview/userPreferenceCount.csv',
        'w+'
    )
    toSaveFile.write('id,user_preference_count\n')
    for user in preferenceList:
        toSaveFile.write(str(user) + ',' + str(preferenceList[user]) + '\n')
    toSaveFile.close()


def painelSongs(songSet, preferenceSet, song_play_set_normalized, song_play_set_counted, song_preference_set_normalized, user_preference_set_normalized, dic_preference_with_class):
    print('=' * 50)
    print('=' * 10 + 'Analise estatistica do dataset' + '=' * 10)
    print('=' * 50)
    print('+ Total de musicas:              ', len(set(songSet["song_id"].tolist())))
    print('+ + Nunca escultadas:            ', str(len(set(songSet["song_id"].tolist())) - len(song_preference_set_normalized)))
    print('+ + Escultadas pelos usuarios:   ', str(len(song_preference_set_normalized)))
    print('')
    #
    print('+ + As ' + str(len(song_preference_set_normalized)) + ' foram adicionandas como preferencia: ', str(len(preferenceSet)))
    print('+ + + Mediana de adicionada nas preferencias:  ', median([float(song_preference_set_normalized[value]) for value in song_preference_set_normalized]))
    print('+ + + Media de adicionada nas preferencias:    ', mean([float(song_preference_set_normalized[value]) for value in song_preference_set_normalized]))
    print('')
    #
    print('+ + Reproduções por usuario - Total de reproduções de uma música individualmente favoritada pelo usuario... tripla(user_id, song_id, play_count)')
    print('+ + + Mediana inteira - O usuario ouve uma música:   ', int(median([float(value) for value in dic_preference_with_class['play_count']])))
    print('+ + + Mediana normalizada:                           ', median([float(value) for value in dic_preference_with_class['global_play_count_normalize']]))
    print('+ + + Media inteira  - O usuario ouve uma música:    ', int(mean([float(value) for value in dic_preference_with_class['play_count']])))
    print('+ + + Media normalizada:                             ', mean([float(value) for value in dic_preference_with_class['global_play_count_normalize']]))
    print('+ + + Maior inteira:                                 ', int(max([float(value) for value in dic_preference_with_class['play_count']])))
    print('+ + + Maior normalizada:                             ', max([float(value) for value in dic_preference_with_class['global_play_count_normalize']]))
    print('+ + + Menor inteira:                                 ', int(min([float(value) for value in dic_preference_with_class['play_count']])))
    print('+ + + Menor normalizada:                             ', min([float(value) for value in dic_preference_with_class['global_play_count_normalize']]))
    print('')
    #
    print('+ + Reproduções por música - Total de vezes que UMA música foi reproduzida')
    print('+ + + Mediana inteira:       ', int(median(song_play_set_counted.values())))
    print('+ + + Mediana normalizada:   ', median(song_play_set_normalized.values()))
    print('+ + + Media inteira:         ', int(mean(song_play_set_counted.values())))
    print('+ + + Media normalizada:     ', mean(song_play_set_normalized.values()))
    print('+ + + Maior inteira:         ', int(max(song_play_set_counted.values())))
    print('+ + + Maior normalizada:     ', max(song_play_set_normalized.values()))
    print('+ + + Menor inteira:         ', int(min(song_play_set_counted.values())))
    print('+ + + Menor normalizada:     ', min(song_play_set_normalized.values()))
    print('')
    #
    print('+ + Relevante são músicas maiores que: ', median([float(value) for value in dic_preference_with_class['global_play_count_normalize']]))
    print('+ + + Relevent', len(dic_preference_with_class.loc[dic_preference_with_class['relevance_global_play'] == 'relevant']))
    print('+ + + Not Relevent',
          len(dic_preference_with_class.loc[dic_preference_with_class['relevance_global_play'] == 'not relevant']))
    print('')
    print('+ Total de usuarios: ', len(set(preferenceSet["user_id"].tolist())))
    print('+ + Total de preferencias: ', str(len(preferenceSet)))
    print('+ + + Mediana: ',
          median([float(user_preference_set_normalized[value]) for value in user_preference_set_normalized]))
    print('+ + + Media: ',
          mean([float(user_preference_set_normalized[value]) for value in user_preference_set_normalized]))


def statisticalOverview(songSet, preferenceSet, DEBUG=True):
    #
    song_preference_set_counted = songPreferenceCount(preferenceSet)
    song_preference_set_normalized = dictNormalize(song_preference_set_counted)
    saveSongPreferenceCount(song_preference_set_normalized)
    #
    user_preference_set_counted = userPreferenceCount(preferenceSet)
    user_preference_set_normalized = dictNormalize(user_preference_set_counted)
    userSongPreferenceCount(user_preference_set_normalized)
    #
    song_play_set_counted = songPlayCount(preferenceSet)
    song_play_set_normalized = dictNormalize(song_play_set_counted)
    saveSongPlayCount(song_play_set_normalized)
    #
    dic_preference_with_class = classify_relevance(preferenceSet)
    #
    if DEBUG is True:
        painelSongs(
            songSet,
            preferenceSet,
            song_play_set_normalized,
            song_play_set_counted,
            song_preference_set_normalized,
            user_preference_set_normalized,
            dic_preference_with_class
        )
    #
    return dic_preference_with_class


def classify_relevance(dict_set):
    set_normalized = list_normalize(dict_set['play_count'].tolist())
    dict_set['global_play_count_normalize'] = pd.Series(set_normalized).values
    lim = float(median(set_normalized))
    dict_set['relevance_global_play'] = np.where(dict_set['global_play_count_normalize'] > lim, 'relevant', 'not relevant')
    return dict_set
