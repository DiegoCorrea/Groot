from data.setHandle import load_data_users, load_data_songs, extractSet
from statisticalOverview import statisticalOverview
from decisionTree import make_set_to_process, preprocessing_data, plant_the_tree
from similarity import get_song_distance
from radio import Radio
from simulated import environment
from interface import interface_menu, random_choice
from graphics import plot_feature_importance, plot_evaluations, plot_similarity, plot_final_state, plot_nodes
import pandas as pd
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


def experiment_cicles(cicles=5, set_size=500):
    weight_df = pd.DataFrame(columns=list([]))
    evaluate_df = pd.DataFrame(columns=list([]))
    similarity_df = pd.DataFrame(columns=list())
    for i in range(cicles):
        print('- * - Iniciando o Ciclo: ', str(i))
        print("+ Extraindo " + str(set_size) + " músicas")
        extractSet(set_size=set_size)
        print('+ Carregando dados no sistema')
        groot = Radio(load_data_songs(), load_data_users())
        print('+ Processando dados')
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
        print('+ Treinando a árvore')
        classifier, evaluate_results = plant_the_tree(
                set_to_process=preprocessing_data(
                    data_set=groot.get_preference_set(),
                    all_features=groot.get_all_features(),
                    DEBUG=False
                ),
                features=groot.get_song_features(),
                important_feature=groot.get_important_feature(),
                DEBUG=False,
                ADMIN=False
            )
        groot.post_classifier(
            new_classifier=classifier
        )
        print('+ Obtendo similaridade entre as músicas')
        groot.post_distance_matrix(
            new_distance_matrix=get_song_distance(
                song_set=groot.get_song_set(),
                song_features=groot.get_song_features(),
                classifier_important=groot.get_feature_weight(),
                DEBUG=False
            )
        )
        print('+ Iniciando a busca')
        similarity = environment(
            groot=groot,
            song_stages=random_choice(groot=groot),
            DEBUG=False
        )
        print('+ Busca Terminada')
        print('Salvando informações')
        #
        weight_df = pd.concat([weight_df, pd.DataFrame(
            [[i for i in list(groot.get_classifier().feature_importances_)]],
            columns=[i for i in list(groot.get_song_features())],
        )])
        #
        evaluate_df = pd.concat([evaluate_df, pd.DataFrame(
            [[i for i in evaluate_results.values()]],
            columns=[x for x in evaluate_results],
        )])
        #
        similarity_df = pd.concat([similarity_df,
                  pd.DataFrame(
                      [[i for i in similarity.values()]],
                      columns=[x for x in similarity],
                  )])
    plot_feature_importance(weight_df)
    plot_evaluations(evaluate_df)
    plot_similarity(similarity_df['similaridade'].tolist())
    plot_final_state(similarity_df['final_state'].tolist())
    plot_nodes(similarity_df['total_visitas'].tolist())


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
    print('+ Treinando a árvore')
    classifier, evaluate_results = plant_the_tree(
        set_to_process=preprocessing_data(
            data_set=groot.get_preference_set(),
            all_features=groot.get_all_features(),
            DEBUG=False
        ),
        features=groot.get_song_features(),
        important_feature=groot.get_important_feature(),
        DEBUG=True,
        ADMIN=False
    )
    groot.post_classifier(
        new_classifier=classifier
    )
    print('+ Obtendo similaridade entre as músicas')
    groot.post_distance_matrix(
        new_distance_matrix=get_song_distance(
            song_set=groot.get_song_set(),
            song_features=groot.get_song_features(),
            classifier_important=groot.get_feature_weight(),
            DEBUG=True
        )
    )
    print('+ Rádio Groot - Iniciando')
    time.sleep(3)
    os.system('clear||cls')
    start_and_end = interface_menu(groot)
    environment(
        groot=groot,
        song_stages=start_and_end
    )


def admin_experiment(set_size=2000):
    print("+ Extraindo " + str(set_size) + " músicas")
    extractSet(set_size=set_size)
    print('+ Carregando dados no sistema')
    groot = Radio(load_data_songs(), load_data_users())
    print('+ Processando dados')
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
    print('+ Treinando a árvore')
    classifier, evaluate_results = plant_the_tree(
        set_to_process=preprocessing_data(
            data_set=groot.get_preference_set(),
            all_features=groot.get_all_features(),
            DEBUG=True
        ),
        features=groot.get_song_features(),
        important_feature=groot.get_important_feature(),
        DEBUG=True,
        ADMIN=True
    )
    groot.post_classifier(
        new_classifier=classifier
    )
    print('+ Obtendo similaridade entre as músicas')
    groot.post_distance_matrix(
        new_distance_matrix=get_song_distance(
            song_set=groot.get_song_set(),
            song_features=groot.get_song_features(),
            classifier_important=groot.get_feature_weight(),
            DEBUG=True
        )
    )
    print('+ Iniciando a busca')
    similarity = environment(
        groot=groot,
        song_stages=random_choice(groot=groot),
        DEBUG=True
    )
    print('+ Busca Terminada')


if __name__ == "__main__":
    experiment_choice = menu()
    if int(experiment_choice) == 1:
        admin_experiment()
    elif int(experiment_choice) == 2:
        experiment_cicles(
            cicles=int(input('Quantos ciclos deseja testar a aplicação? ')),
            set_size=int(input('Quantas músicas deseja extrair? '))
        )
    else:
        user_experiment()
