# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import (classification_report,
                             confusion_matrix,
                             mean_absolute_error,
                             mean_squared_error,
                             precision_recall_fscore_support)
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


def make_set_to_process(song_set, dict_set, DEBUG=True):
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
    if DEBUG is True:
        data_information(set_to_process)
    return set_to_process


def print_tree_evaluate(y_test, y_pred):
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


def plant_the_tree(set_to_process, features, important_feature, DEBUG):
    y = set_to_process[important_feature]
    x = set_to_process[features]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
    classifier = DecisionTreeClassifier()
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    evaluate_values = dict()
    evaluate_values['RMSE'] = np.sqrt(mean_squared_error(y_test, y_pred))
    precision, recall, fscore, support = precision_recall_fscore_support(y_test, y_pred)
    evaluate_values['Precision NR'] = precision[0]
    evaluate_values['Precision R'] = precision[1]
    evaluate_values['Recall NR'] = recall[0]
    evaluate_values['Recall R'] = recall[1]
    if DEBUG is True:
            print_tree_evaluate(y_test, y_pred)
            tree_information(classifier)
            dot_data = export_graphviz(
                classifier,
                out_file=None,
                feature_names=features,
                class_names=important_feature,
                filled=True,
                rounded=True,
                special_characters=True
            )
            graph = graphviz.Source(dot_data)
            graph.view()
            os.system("dot -Tpng Source.gv -o decision-tree.png")
    return classifier, evaluate_values


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


def preprocessing_data(data_set, all_features, DEBUG):
    if DEBUG is True:
        print('=' * 50)
        print('=' * 7 + 'Pre-Processamento: Enumerando dados' + '=' * 8)
        print('=' * 50)
    clean_data_set, album_targets = encode_target(data_set, all_features[0])
    for feature in all_features[1:]:
        clean_data_set, target = encode_target(clean_data_set, feature)
        if DEBUG is True:
            print_preprocessing_data(clean_data_set, feature, target)
    return clean_data_set


def print_preprocessing_data(clean_data_set, feature, target):
    print("* head()", clean_data_set[[feature]].head(),
          sep="\n", end="\n\n")
    print("* tail()", clean_data_set[[feature]].tail(),
          sep="\n", end="\n\n")
    print("* Song Id", target, sep="\n", end="\n\n")