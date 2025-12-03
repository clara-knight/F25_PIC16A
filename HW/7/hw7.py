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
url = "https://raw.githubusercontent.com/liaochunyang/PIC16/refs/heads/main/PIC16A/data/2019.csv"
happiness = pd.read_csv(url)
# # Warm up: generate scatterplot of overall score vs another column
x = happiness["Social support"]
y = happiness["Score"]
plt.scatter(x, y)
plt.xlabel("Social support")
plt.ylabel("Score")
# plt.show()


cols = ["Score", "Social support", "GDP per capita"]


def scatterplot_matrix(cols):
    total_variables = len(cols)
    fig, axarr = plt.subplots(total_variables, total_variables)
    for i in range(total_variables):
        x = happiness[cols[i]]
        for j in range(total_variables):
            if i != j:
                y = happiness[cols[j]]
                axarr[i][j].scatter(x, y)
    plt.show()


scatterplot_matrix(cols)
