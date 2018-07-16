import matplotlib.pyplot as plt
import os


def plot_feature_importance(df):
    directory = str(
        'graphs/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('Pesos dos dados')
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


def plot_evaluations(df):
    directory = str(
        'graphs/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('Resultados da Arvore')
    plt.xlabel('Rodada')
    plt.ylabel('Valor')
    for feature in df.dtypes.index:
        plt.plot(
            [i + 1 for i in range(df[feature].count())],
            df[feature].tolist(),
            label=feature
        )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'evaluations.png'
    )
    plt.close()


def plot_similarity(df):
    directory = str(
        'graphs/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('Similaridade do percurso')
    plt.xlabel('Rodada')
    plt.ylabel('Valor')
    plt.plot(
        [i + 1 for i in range(len(df))],
        [float(i) for i in df]
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'similarity.png'
    )
    plt.close()


def plot_final_state(df):
    directory = str(
        'graphs/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('Rodadas que chegaam ao fim')
    plt.xlabel('Rodada')
    plt.ylabel('Valor')
    plt.plot(
        [i + 1 for i in range(len(df))],
        df
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'final_state.png'
    )
    plt.close()


def plot_nodes(df):
    directory = str(
        'graphs/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('Total de Nós visitados')
    plt.xlabel('Rodada')
    plt.ylabel('Valor')
    plt.plot(
        [i + 1 for i in range(len(df))],
        df
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'know_nodes.png'
    )
    plt.close()