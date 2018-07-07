from data.setHandle import load_data_users, load_data_songs, extractSet
from statisticalOverview import statisticalOverview


def restartSet():
    extractSet()
    main()


def main():
    SONGSET = load_data_songs()
    PREFERENCESET = load_data_users()
    statisticalOverview(SONGSET, PREFERENCESET)


if __name__ == "__main__":
    main()
