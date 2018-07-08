import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, mean_absolute_error, mean_squared_error


def data_information(pd_dict_set):
    print('*'*60)
    print(pd_dict_set.shape)
    print(pd_dict_set.describe())
    print(pd_dict_set.info())


def make_set_to_process(song_set, dict_set):
    set_to_process = pd.DataFrame()
    set_to_process['user_id'] = dict_set['user_id']
    set_to_process['song_id'] = dict_set['song_id']
    set_to_process['relevance_global_play'] = dict_set['relevance_global_play']
    set_to_process['title'] = ''
    set_to_process['album'] = ''
    set_to_process['artist'] = ''
    for item in set(set_to_process['song_id']):
        song = song_set.loc[song_set['id'] == item]
        set_to_process.loc[(set_to_process['song_id'].str.contains(item)), 'title'] = str(song['title'].tolist()[0])
        set_to_process.loc[(set_to_process['song_id'].str.contains(item)), 'album'] = str(song['album'].tolist()[0])
        set_to_process.loc[(set_to_process['song_id'].str.contains(item)), 'artist'] = str(song['artist'].tolist()[0])
    data_information(set_to_process)
    return set_to_process


def tree_execute(set_to_process):
    features = list(['title', 'artist', 'album', 'user_id', 'song_id'])
    y = set_to_process["relevance_global_play"]
    X = set_to_process[features]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print('Mean Absolute Error:', mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y_test, y_pred)))


def encode_target(df, target_column):
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod[target_column] = df[target_column].replace(map_to_int)
    return (df_mod, targets)


def preprocessing_data(data_set):
    clean_data_set, album_targets = encode_target(data_set, "album")
    print("* df2.head()", clean_data_set[["album"]].head(),
          sep="\n", end="\n\n")
    print("* df2.tail()", clean_data_set[["album"]].tail(),
          sep="\n", end="\n\n")
    print("* targets", album_targets, sep="\n", end="\n\n")
    #
    clean_data_set, artist_targets = encode_target(clean_data_set, "artist")
    print("* df2.head()", clean_data_set[["artist"]].head(),
          sep="\n", end="\n\n")
    print("* df2.tail()", clean_data_set[["artist"]].tail(),
          sep="\n", end="\n\n")
    print("* targets", artist_targets, sep="\n", end="\n\n")
    #
    clean_data_set, title_targets = encode_target(clean_data_set, "title")
    print("* df2.head()", clean_data_set[["title"]].head(),
          sep="\n", end="\n\n")
    print("* df2.tail()", clean_data_set[["title"]].tail(),
          sep="\n", end="\n\n")
    print("* targets", title_targets, sep="\n", end="\n\n")
    #
    clean_data_set, relevance_global_targets = encode_target(clean_data_set, "relevance_global_play")
    print("* df2.head()", clean_data_set[["relevance_global_play"]].head(),
          sep="\n", end="\n\n")
    print("* df2.tail()", clean_data_set[["relevance_global_play"]].tail(),
          sep="\n", end="\n\n")
    print("* targets", relevance_global_targets, sep="\n", end="\n\n")
    #
    clean_data_set, user_targets = encode_target(clean_data_set, "user_id")
    print("* df2.head()", clean_data_set[["user_id"]].head(),
          sep="\n", end="\n\n")
    print("* df2.tail()", clean_data_set[["user_id"]].tail(),
          sep="\n", end="\n\n")
    print("* targets", user_targets, sep="\n", end="\n\n")
    #
    clean_data_set, song_targets = encode_target(clean_data_set, "song_id")
    print("* df2.head()", clean_data_set[["song_id"]].head(),
          sep="\n", end="\n\n")
    print("* df2.tail()", clean_data_set[["song_id"]].tail(),
          sep="\n", end="\n\n")
    print("* targets", song_targets, sep="\n", end="\n\n")
    return clean_data_set