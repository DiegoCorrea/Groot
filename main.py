from data.setHandle import load_data_users, load_data_songs, extractSet
from statisticalOverview import statisticalOverview
from decisionTree import make_set_to_process, preprocessing_data, tree_execute
from similarity import get_song_distance
from radio import Radio


def restartSet():
    extractSet()
    main()


def main():
    groot = Radio(load_data_songs(), load_data_users())
    groot.post_preference_set(
        make_set_to_process(
            groot.get_song_set(),
            statisticalOverview(
                groot.get_song_set(),
                groot.get_preference_set()
            )
        )
    )
    groot.post_classifier(
        tree_execute(
            preprocessing_data(groot.get_preference_set())
        )
    )
    groot.post_classifier(get_song_distance(groot.get_song_set()))


if __name__ == "__main__":
    if input("Deseja extrair novos dados? (Y/N): ") == 'Y':
        restartSet()
    main()
