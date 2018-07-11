from data.setHandle import load_data_users, load_data_songs, extractSet
from statisticalOverview import statisticalOverview
from decisionTree import make_set_to_process, preprocessing_data, tree_execute

def restartSet():
    extractSet()
    main()


def main():
    SONGSET = load_data_songs()
    PREFERENCESET = load_data_users()
    dict_set = statisticalOverview(SONGSET, PREFERENCESET)
    data_set = make_set_to_process(SONGSET, dict_set)
    clean_data_set = preprocessing_data(data_set)
    tree_execute(clean_data_set)


if __name__ == "__main__":
    if input("Deseja extrair novos dados? (Y/N): ") == 'Y':
        restartSet()
    main()
