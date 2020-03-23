import networkx as nx
import matplotlib.pyplot as plt


class BasicGraphSet(object):
    # graph setting
    with_labels = True
    node_size = 900
    node_color = 'r'
    alpha = 1
    width = 4  # edge width
    edge_color = 'black'
    font_size = 20
    font_color = 'w'

    # ax setting
    x_ticks = []
    y_ticks = []
    line_width = 4
    line_color = 'r'
    title_fontsize = 20

    @staticmethod
    def ax_set(ax, title):
        ax.set_title(title, fontsize=BasicGraphSet.title_fontsize)
        ax.xaxis.set_ticks(BasicGraphSet.x_ticks)
        ax.yaxis.set_ticks(BasicGraphSet.y_ticks)
        ax_line_width = BasicGraphSet.line_width
        ax_line_color = BasicGraphSet.line_color
        for pos in ['bottom', 'top', 'left', 'right']:
            ax.spines[pos].set_linewidth(ax_line_width)
            ax.spines[pos].set_color(ax_line_color)


def connected_compo(ax):
    BasicGraphSet.ax_set(ax, 'connected component')
    g = nx.Graph()
    # this graph has two connected components
    g.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd')])
    g.add_edges_from([('e', 'f'), ('f', 't'), ('e', 't')])
    # draw this graph
    nx.draw_networkx(g, pos=nx.circular_layout(g), ax=ax, with_labels=BasicGraphSet.with_labels,
                     node_size=BasicGraphSet.node_size, node_color=BasicGraphSet.node_color,
                     alpha=BasicGraphSet.alpha, width=BasicGraphSet.width,
                     edge_color=BasicGraphSet.edge_color, font_size=BasicGraphSet.font_size,
                     font_color=BasicGraphSet.font_color)
    print('this graph has ', nx.number_connected_components(g), 'connected components')
    # print each connected components
    for comp in nx.connected_components(g):
        print(comp)


if __name__ == '__main__':
    # set figure
    fig = plt.figure(num='fig', figsize=(8, 8))
    ax1 = fig.add_subplot(221)
    # draw connected components
    connected_compo(ax1)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    plt.show()
