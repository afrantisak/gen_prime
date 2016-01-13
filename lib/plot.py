import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def rainbow_range(maximum):
    return matplotlib.cm.rainbow(np.linspace(0, 1, len(maximum)))

def show_2d(x, y, c=None):
    max_x = max(x)
    max_y = max(y)
    edg_x = max_x * 0.05
    edg_y = max_y * 0.05
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    if c:
        ax.scatter(x, y, c=c)
    else:
        ax.scatter(x, y)
    ax.axis([-edg_x, max_x + edg_x, -edg_y, max_y + edg_y])
    plt.show()

