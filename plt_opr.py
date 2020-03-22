import numpy as np
import matplotlib.pyplot as plt


def draw_line(ax1):
    ax1.set_title('Pic 1', fontsize=30)
    ax1.set_xlabel('x', fontsize=25, fontfamily='sans-serif', fontstyle='italic')
    ax1.set_ylabel('y', fontsize=25, fontstyle='oblique')
    x = np.arange(5)
    y1 = x ** 2
    y2 = x
    y3 = x ** 1.5
    y4 = np.log(2 * x + 1)
    ax1.set_xlim(0, 4)
    ax1.set_ylim(0, 16)

    ax1.tick_params(axis="x", labelsize=20, labelrotation=-20, labelcolor='r', color='g', length=10, width=4,
                    gridOn=True)
    ax1.tick_params(axis="y", labelsize=20, length=10, width=4)
    ax1.xaxis.set_ticks(np.linspace(0, 4, 9, endpoint=True))
    ax1.yaxis.set_ticks(np.linspace(0, 16, 9, endpoint=True))

    ax1.plot(x, y1, marker='s', ls='-', label='first', c='g', linewidth=8, ms=15, mfc='w', mec='g', mew=4)
    ax1.plot(x, y2, marker='o', ls='-', label='second', c='b', linewidth=6, ms=15, mfc='w', mec='b', mew=4)
    ax1.plot(x, y3, marker='^', ls='-', label='third', c='black', linewidth=6, ms=15, mfc='w', mec='black', mew=4)
    ax1.plot(x, y4, marker='>', ls='-', label='fourth', c='y', linewidth=6, ms=15, mfc='w', mec='y', mew=4)
    leg = ax1.legend(loc='upper left', fontsize=20, markerscale=1.5, frameon=True, ncol=2, borderpad=1,
                     labelspacing=1, handlelength=3, handletextpad=1, borderaxespad=1, columnspacing=1)
    for line in leg.get_lines():
        line.set_linewidth(4.0)
    # change settings of axis
    ax1_line_width = 4
    ax1_line_color = 'red'
    for pos in ['bottom', 'top', 'left', 'right']:
        ax1.spines[pos].set_linewidth(ax1_line_width)
        ax1.spines[pos].set_color(ax1_line_color)
    plt.show()


def draw_scatter(ax1):
    n = 50
    x1 = np.random.rand(n)
    y1 = np.random.rand(n)
    size = (np.random.rand(n) * 40) ** 2
    color = np.random.rand(n)
    ax1.scatter(x1, y1, s=size, c=color, alpha=0.5, edgecolors='w', marker='o', label='circle')
    x2 = np.random.rand(n)
    y2 = np.random.rand(n)
    ax1.scatter(x2, y2, s=size, c=color, alpha=0.5, edgecolors='w', marker='s', label='space')
    x3 = np.random.rand(n)
    y3 = np.random.rand(n)
    ax1.scatter(x3, y3, s=size, c=color, alpha=0.5, edgecolors='w', marker='^', label='triangle')
    ax1.legend(bbox_to_anchor=(-0.04, 1.001), loc='lower left', fontsize=20, frameon=True, ncol=3, borderpad=1,
               labelspacing=1, handlelength=3, handletextpad=0.5, borderaxespad=1, columnspacing=1)
    ax1.grid(True)
    plt.show()


def draw_step(ax1):
    x = np.arange(5)
    y = x ** 2
    ax1.step(x, y, lw=2)
    plt.show()


def draw_bar(ax1):
    x = np.arange(5)
    y = x ** 2
    ax1.bar(x, y, align='center', width=0.4, alpha=0.5)
    plt.show()


def draw_fill(ax1):
    x = np.arange(5)
    y1 = x ** 2 + 1
    y2 = x ** 3 + 0.5
    ax1.fill_between(x, y1, y2, color='y', alpha=0.5)
    plt.show()


if __name__ == '__main__':
    fig = plt.figure(num='fig', figsize=(8, 8), dpi=75, facecolor='#FFFFFF')
    ax = fig.add_subplot(111)
    # draw_line(ax)
    draw_scatter(ax)
    # draw_step(ax)
    # draw_bar(ax)
    # draw_fill(ax)
