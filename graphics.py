import matplotlib.pyplot as plt
import os


def plot_feature_importance(df):
    print(df)
    directory = str(
        'results/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.xlabel('Rodada')
    plt.ylabel('Peso')
    for feature in df.dtypes.index:
        plt.plot(
            [i + 1 for i in range(df[feature].count())],
            df[feature].tolist(),
            label=feature
        )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'feature_importance.png'
    )
    plt.close()
