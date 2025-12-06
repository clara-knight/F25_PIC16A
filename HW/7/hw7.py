import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def create_data(n, n_groups):
    """
    generate a set of fake data with group labels.
    n data points and group labels are generated.
    n_groups controls the number of distinct groups.
    Returns an np.array() of integer group labels and an
    np.array() of float data.
    """
    groups = np.random.randint(0, n_groups, n)
    data = np.sin(groups) + np.random.randn(n)
    return groups, data


def facet_hist(groups, data, m_rows, m_cols, figsize):
    unique_groups = np.unique(groups)
    total_groups = m_rows * m_cols

    if total_groups != (len(unique_groups)):
        raise ValueError("Size mismatch.")
    fig, axarr = plt.subplots(nrows=m_rows, ncols=m_cols)
    fig.figsize = figsize
    flat_axs = axarr.flatten(order="F")

    for grp in unique_groups:
        current_ax = flat_axs[grp]
        group_index = groups == grp
        data_points = data[group_index]
        if grp < m_rows:
            current_ax.set_ylabel("Density")
        if grp % m_rows == m_rows - 1:
            current_ax.set_xlabel("x")
        current_ax.set_title(f"Group {grp}")
        current_ax.hist(data_points)

    plt.tight_layout()
    plt.show()


#   groups, data = create_data(1000, 6)
#   facet_hist(groups, data, 3, 2, figsize=(4, 6))
#   groups, data = create_data(1000, 9)
#   facet_hist(groups, data, 3, 3, figsize=(4, 6))


# 3
#   url = "https://raw.githubusercontent.com/liaochunyang/PIC16/refs/heads/main/PIC16A/data/2019.csv"
#   happiness = pd.read_csv(url)
#   # # Warm up: generate scatterplot of overall score vs another column
#   x = happiness["Social support"]
#   y = happiness["Score"]
#   # plt.scatter(x, y)
#   # plt.xlabel("Social support")
#   # plt.ylabel("Score")
#   # plt.show()
happiness = []


cols = ["Score", "GDP per capita", "Social support"]


def scatterplot_matrix(cols):
    total_variables = len(cols)
    fig, axarr = plt.subplots(total_variables, total_variables)

    for i, colname in enumerate(cols):
        x = happiness[colname]
        for j, rowname in enumerate(cols):
            current_ax = axarr[i][j]
            current_ax.set(xlabel=colname)
            current_ax.set(ylabel=rowname)
            if i != j:
                y = happiness[rowname]
                current_ax.scatter(x, y)
    plt.tight_layout()
    plt.show()


def scatterplot_matrix_corr(cols):
    total_variables = len(cols)
    fig, axarr = plt.subplots(total_variables, total_variables)

    for i, colname in enumerate(cols):
        x = happiness[colname]
        for j, rowname in enumerate(cols):
            y = happiness[rowname]
            current_ax = axarr[i][j]
            rho = np.corrcoef(x, y)[0][1]
            current_ax.set(
                title=f"{colname}",
                xlabel=r"$\rho$ = " + str(np.round(rho, 3)),
                ylabel=f"{rowname}",
            )
            if i != j:
                current_ax.scatter(x, y)
    plt.tight_layout()
    plt.show()


# scatterplot_matrix_corr(cols)

url = "https://raw.githubusercontent.com/liaochunyang/PIC16/refs/heads/main/PIC16A/data/gapminder.csv"
gapminder = pd.read_csv(url)


def gapmider_visualization(gm):
    unique_continents = gapminder["continent"].unique()
    fig, axarr = plt.subplots(1, len(unique_continents))

    continents_dict = dict(zip(unique_continents, axarr))

    gm.set_index("year", inplace=True)

    gm.groupby("country").apply(plot_country, cdict=continents_dict)

    plt.tight_layout()
    plt.show()


def plot_country(gm_df, cdict):
    continent = gm_df["continent"].iloc[0]
    current_ax = cdict[continent]
    # gm_df['lifeExp'].plot
    current_ax.plot(gm_df["lifeExp"])


gapmider_visualization(gapminder)
