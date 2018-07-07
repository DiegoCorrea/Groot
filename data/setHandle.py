import csv
import pandas as pd
from random import sample


def extract_Data_Songs(sizeCut=1000):
    songTable = csv.DictReader(
        open(
            'data/oneMillionSongs/songs.csv',
            'r+'
        )
    )
    return sample(list(songTable), sizeCut)


def extract_Data_Users(songListID):
    playCountCSV = csv.DictReader(
        open(
            'data/oneMillionSongs/playCount.csv',
            'r+'
        )
    )
    preferenceTable = []
    for preference in playCountCSV:
        if preference['song_id'] in songListID:
            preferenceTable.append(preference)
    return preferenceTable


def saveSongSet(songSet):
    toSaveSong = open(
        'data/set/songSet.csv',
        'w+'
    )
    toSaveSong.write('id,title,album,artist,year\n')
    for line in songSet:
        toSaveSong.write(
            str(line['id'])
            + ','
            + str(line['title'])
            + ','
            + str(line['album'])
            + ','
            + str(line['artist'])
            + ','
            + str(line['year'])
            + '\n'
        )
    toSaveSong.close()


def savePreferenceSet(preferenceSet):
    toSaveSong = open(
        'data/set/preferenceSet.csv',
        'w+'
    )
    toSaveSong.write('user_id,song_id,play_count\n')
    for line in preferenceSet:
        toSaveSong.write(
            str(line['user_id'])
            + ','
            + str(line['song_id'])
            + ','
            + str(line['play_count'])
            + '\n'
        )
    toSaveSong.close()


def extractSet(songSizeCut=2000, userSizeCut=10):
    songSet = extract_Data_Songs(songSizeCut)
    saveSongSet(songSet)
    preferenceSet = extract_Data_Users([song['id'] for song in songSet])
    savePreferenceSet(preferenceSet)


def load_data_songs():
    return pd.read_csv('data/set/songSet.csv')


def load_data_users():
    return pd.read_csv('data/set/preferenceSet.csv')
