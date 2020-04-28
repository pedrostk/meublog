# Libraries
import math

# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import pandas as pd
from math import pi


def plotagem(a, b, c):
    # Set data
    df = pd.DataFrame({
        'group': ['A'],
        'Ed': [a],
        'Hhd': [b],
        'Nd': [c],
    })

    # number of variable
    categories = list(df)[1:]
    N = len(categories)

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values = df.loc[0].drop('group').values.flatten().tolist()
    values += values[:1]
    values

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='red', size=20)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([0.25, 0.5, 0.75], ["0.25", "0.5", "0.75"], color="black", size=7)
    plt.ylim(0, 1)

    # Plot data
    ax.plot(angles, values, linewidth=3, linestyle='solid')

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)

    # ab, lado 1
    c1 = (a ** 2 + b ** 2 + a * b) ** (1 / 2)
    # bc, lado 2
    c2 = (b ** 2 + c ** 2 + b * c) ** (1 / 2)
    # ca, lado 3
    c3 = (c ** 2 + a ** 2 + a * c) ** (1 / 2)
    print(c1, c2, c3)
    p = c1 + c2 + c3
    sp = p / 2
    s = (sp * (sp - c1) * (sp - c2) * (sp - c3)) ** (1 / 2)
    print(f'A área da tríade tem valor de {s:.2f}')
    plt.show()

# Data input ###MAIN PROGRAM
a = float(input('Type the environmental index: '))
b = float(input('Type the health index: '))
c = float(input('Type the nutrition index: '))

print(plotagem(a, b, c))
