import numpy as np
import matplotlib.pyplot as plt

my_func = lambda x: x ** 2 + 5
v1 = np.linspace(-1, 1)
v2 = np.linspace(-6, 6)
v3 = np.linspace(0, 5)


def plot_func(x, y, title='', x_ax='', y_ax=''):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_ax)
    plt.ylabel(y_ax)
    plt.legend('linia')
    plt.show()


plot_func(v1, my_func(v1), '1', 'x axis', 'y axis')
plot_func(v2, my_func(v2), '2', 'x axis', 'y axis')
plot_func(v3, my_func(v3), '3', 'x axis', 'y axis')
