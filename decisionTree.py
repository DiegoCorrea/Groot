# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, mean_absolute_error, mean_squared_error
import graphviz


def data_information(pd_dict_set):
    print('=' * 50)
    print('=' * 10 + 'Estrutura e dados do Data Frame' + '=' * 9)
    print('=' * 50)
    print('+ Dataframe Shape')
    print(pd_dict_set.shape)
    print('-' * 50)
    print('+ Dataframe Description')
    print(pd_dict_set.describe())
    print('-' * 50)
    print('+ Dataframe Information')
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
        song = song_set.loc[song_set['song_id'] == item]
        set_to_process.loc[(set_to_process['song_id'].str.contains(item)), 'title'] = str(song['title'].tolist()[0])
        set_to_process.loc[(set_to_process['song_id'].str.contains(item)), 'album'] = str(song['album'].tolist()[0])
        set_to_process.loc[(set_to_process['song_id'].str.contains(item)), 'artist'] = str(song['artist'].tolist()[0])
    data_information(set_to_process)
    return set_to_process


def tree_evaluate(y_test, y_pred):
    print('='*50)
    print('='*21 + 'Métricas' + '='*21)
    print('='*50)
    print('+ Confusion Matrix: ')
    print(confusion_matrix(y_test, y_pred))
    print('')
    print('+ Métricas')
    print(classification_report(y_test, y_pred))
    print('')
    print('+ Mean Absolute Error:', mean_absolute_error(y_test, y_pred))
    print('+ Mean Squared Error:', mean_squared_error(y_test, y_pred))
    print('+ Root Mean Squared Error:', np.sqrt(mean_squared_error(y_test, y_pred)))


def tree_information(classifier):
    feature_import = classifier.feature_importances_
    print('='*50)
    print('='*18 + 'Peso da Coluna' + '='*18)
    print('='*50)
    print('+ Title:   ' + str(feature_import[0]) + '\n')
    print('+ Artist:  ' + str(feature_import[1]) + '\n')
    print('+ Album:   ' + str(feature_import[2]) + '\n')
    print('+ Song_id: ' + str(feature_import[3]) + '\n')


def plant_the_tree(set_to_process, features):
    y = set_to_process["relevance_global_play"]
    x = set_to_process[features]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
    classifier = DecisionTreeClassifier()
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    tree_evaluate(y_test, y_pred)
    tree_information(classifier)
    dot_data = export_graphviz(
        classifier,
        out_file=None,
        feature_names=features,
        class_names='relevance_global_play',
        filled=True,
        rounded=True,
        special_characters=True
    )
    graph = graphviz.Source(dot_data)
    graph.view()
    os.system("dot -Tpng Source.gv -o decision-tree.png")
    return classifier


def new_data_predict(classifier, new_data, features):
    print('=' * 50)
    print('=' * 18 + 'Predizendo novos itens' + '=' * 18)
    print('=' * 50)
    return classifier.predict(new_data[features])


def encode_target(df, target_column):
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod[target_column] = df[target_column].replace(map_to_int)
    return df_mod, targets


def preprocessing_data(data_set, features):
    print('=' * 50)
    print('=' * 7 + 'Pre-Processamento: Enumerando dados' + '=' * 8)
    print('=' * 50)
    clean_data_set, album_targets = encode_target(data_set, "album")
    print("* head()", clean_data_set[["album"]].head(),
          sep="\n", end="\n\n")
    print("* tail()", clean_data_set[["album"]].tail(),
          sep="\n", end="\n\n")
    print("* Album", album_targets, sep="\n", end="\n\n")
    #
    clean_data_set, artist_targets = encode_target(clean_data_set, "artist")
    print("* head()", clean_data_set[["artist"]].head(),
          sep="\n", end="\n\n")
    print("* tail()", clean_data_set[["artist"]].tail(),
          sep="\n", end="\n\n")
    print("* Artists", artist_targets, sep="\n", end="\n\n")
    #
    clean_data_set, title_targets = encode_target(clean_data_set, "title")
    print("* head()", clean_data_set[["title"]].head(),
          sep="\n", end="\n\n")
    print("* tail()", clean_data_set[["title"]].tail(),
          sep="\n", end="\n\n")
    print("* Title", title_targets, sep="\n", end="\n\n")
    #
    clean_data_set, relevance_global_targets = encode_target(clean_data_set, "relevance_global_play")
    print("* head()", clean_data_set[["relevance_global_play"]].head(),
          sep="\n", end="\n\n")
    print("* tail()", clean_data_set[["relevance_global_play"]].tail(),
          sep="\n", end="\n\n")
    print("* Global Relevance", relevance_global_targets, sep="\n", end="\n\n")
    #
    clean_data_set, user_targets = encode_target(clean_data_set, "user_id")
    print("* head()", clean_data_set[["user_id"]].head(),
          sep="\n", end="\n\n")
    print("* tail()", clean_data_set[["user_id"]].tail(),
          sep="\n", end="\n\n")
    print("* User Id", user_targets, sep="\n", end="\n\n")
    #
    clean_data_set, song_targets = encode_target(clean_data_set, "song_id")
    print("* head()", clean_data_set[["song_id"]].head(),
          sep="\n", end="\n\n")
    print("* tail()", clean_data_set[["song_id"]].tail(),
          sep="\n", end="\n\n")
    print("* Song Id", song_targets, sep="\n", end="\n\n")
    return clean_data_set
