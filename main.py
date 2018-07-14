from data.setHandle import load_data_users, load_data_songs, extractSet
from statisticalOverview import statisticalOverview
from decisionTree import make_set_to_process, preprocessing_data, plant_the_tree
from similarity import get_song_distance
from radio import Radio
from simulated import environment
from interface import interface_menu
import os
import time


def menu():
    os.system('clear||cls')
    print('+' * 50)
    print('+' * 20 + 'I am Groot' + '+' * 20)
    print('+' * 50)
    print('1- Experimento com DEBUG Mode True')
    print('2- Experimento com Ciclos')
    print('3- Experimento como Usuário')
    print('+' * 50)
    try:
        return input('Escolha: ')
    except Exception:
        return 3


def experiment_cicles(cicles=10, set_size=2000):
    for i in range(cicles):
        extractSet(set_size=set_size)
        groot = Radio(load_data_songs(), load_data_users())
        print('+ Carregando Dados')
        groot.post_preference_set(
            preference_set=make_set_to_process(
                song_set=groot.get_song_set(),
                dict_set=statisticalOverview(
                    songSet=groot.get_song_set(),
                    preferenceSet=groot.get_preference_set(),
                    DEBUG=False
                ),
                DEBUG=False
            )
        )
        print('+ Treinando a arvore')
        groot.post_classifier(
            new_classifier=plant_the_tree(
                set_to_process=preprocessing_data(
                    data_set=groot.get_preference_set(),
                    all_features=groot.get_all_features(),
                    DEBUG=False
                ),
                features=groot.get_song_features(),
                important_feature=groot.get_important_feature(),
                DEBUG=False
            )
        )


def user_experiment():
    groot = Radio(load_data_songs(), load_data_users())
    print('+ Carregando Dados')
    groot.post_preference_set(
        preference_set=make_set_to_process(
            song_set=groot.get_song_set(),
            dict_set=statisticalOverview(
                songSet=groot.get_song_set(),
                preferenceSet=groot.get_preference_set(),
                DEBUG=False
            ),
            DEBUG=False
        )
    )
    print('+ Treinando a arvore')
    groot.post_classifier(
        new_classifier=plant_the_tree(
            set_to_process=preprocessing_data(
                data_set=groot.get_preference_set(),
                all_features=groot.get_all_features(),
                DEBUG=False
            ),
            features=groot.get_song_features(),
            important_feature=groot.get_important_feature(),
            DEBUG=False
        )
    )
    groot.post_distance_matrix(
        get_song_distance(
            groot.get_song_set(),
            groot.get_song_features(),
            groot.get_classifier().feature_importances_
        )
    )
    print('+ Rádio Groot - Iniciando')
    time.sleep(3)
    os.system('clear||cls')
    start_and_end = interface_menu(groot)
    environment(
        groot,
        start_and_end
    )


def admin_experiment():
    groot = Radio(load_data_songs(), load_data_users())
    groot.post_preference_set(
        preference_set=make_set_to_process(
            song_set=groot.get_song_set(),
            dict_set=statisticalOverview(
                songSet=groot.get_song_set(),
                preferenceSet=groot.get_preference_set(),
                DEBUG=True
            ),
            DEBUG=True
        )
    )
    groot.post_classifier(
        new_classifier=plant_the_tree(
            set_to_process=preprocessing_data(
                data_set=groot.get_preference_set(),
                all_features=groot.get_all_features(),
                DEBUG=True
            ),
            features=groot.get_song_features(),
            important_feature=groot.get_important_feature(),
            DEBUG=True
        )
    )
    groot.post_distance_matrix(
        get_song_distance(
            groot.get_song_set(),
            groot.get_song_features(),
            groot.get_classifier().feature_importances_
        )
    )
    start_and_end = interface_menu(groot)
    environment(
        groot,
        start_and_end
    )


if __name__ == "__main__":
    experiment_choice = menu()
    if int(experiment_choice) == 1:
        admin_experiment()
    elif int(experiment_choice) == 2:
        experiment_cicles()
    else:
        user_experiment()
