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
        """
        default setting for ax
        :param ax: ax
        :param title: the title of this graph
        :return: no returns
        """
        ax.set_title(title, fontsize=BasicGraphSet.title_fontsize)
        ax.xaxis.set_ticks(BasicGraphSet.x_ticks)
        ax.yaxis.set_ticks(BasicGraphSet.y_ticks)
        ax_line_width = BasicGraphSet.line_width
        ax_line_color = BasicGraphSet.line_color
        for pos in ['bottom', 'top', 'left', 'right']:
            ax.spines[pos].set_linewidth(ax_line_width)
            ax.spines[pos].set_color(ax_line_color)

    @staticmethod
    def basic_draw(g, ax):
        nx.draw_networkx(g, pos=nx.circular_layout(g), ax=ax, with_labels=BasicGraphSet.with_labels,
                         node_size=BasicGraphSet.node_size, node_color=BasicGraphSet.node_color,
                         alpha=BasicGraphSet.alpha, width=BasicGraphSet.width,
                         edge_color=BasicGraphSet.edge_color, font_size=BasicGraphSet.font_size)

    @staticmethod
    def set_property_for_edges(graph_edges, match_edges, g_prop, m_prop):
        """
        set special property value (m_prop) for match_edges, while common
        property value (g_prop) for all other edges in a graph
        :param graph_edges: graph edges
        :param match_edges: tuple, list or dict
        :param g_prop: common property value, like 'white'
        :param m_prop: special property value, like 'red'
        :return: a list of property values followed the sequence of edges in a graph
        """
        prop_list = []
        for node_one, node_two in graph_edges:
            if (node_one, node_two) in match_edges:
                prop_list.append(m_prop)
            else:
                prop_list.append(g_prop)
        return prop_list


def draw_directed_graph(ax):
    BasicGraphSet.ax_set(ax, 'Directed Graph')
    g = nx.DiGraph()

    g.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd')])
    g.add_edges_from([('e', 'f'), ('f', 't'), ('e', 't')])
    BasicGraphSet.basic_draw(g, ax)


def draw_connected_compo(ax):
    """
    draw connected component
    :param ax: ax
    :return: no returns
    """
    BasicGraphSet.ax_set(ax, 'Connected Component')
    g = nx.Graph()

    # this graph has two connected components
    g.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd')])
    g.add_edges_from([('e', 'f'), ('f', 't'), ('e', 't')])

    # draw this graph
    BasicGraphSet.basic_draw(g, ax)
    print('this graph has ', nx.number_connected_components(g), 'connected components')

    # print each connected components
    for comp in nx.connected_components(g):
        print(comp)


def draw_minimal_spanning_tree(ax):
    BasicGraphSet.ax_set(ax, 'Minimal Spanning Tree')
    g = nx.Graph()
    g.add_edges_from([
        ('a', 'b', {'weight': 2}),
        ('a', 'c', {'weight': 4}),
        ('a', 'e', {'weight': 3}),
        ('b', 'd', {'weight': 6}),
        ('c', 'e', {'weight': 7}),
        ('d', 'e', {'weight': 5})
    ])
    spanning_tree = nx.minimum_spanning_tree(g)
    edge_colors = BasicGraphSet.set_property_for_edges(g.edges, spanning_tree,
                                                       'yellow', 'black')
    nx.draw_networkx(g, pos=nx.circular_layout(g), ax=ax, with_labels=BasicGraphSet.with_labels,
                     node_size=BasicGraphSet.node_size, node_color=BasicGraphSet.node_color,
                     alpha=BasicGraphSet.alpha, width=BasicGraphSet.width,
                     edge_color=edge_colors, font_size=BasicGraphSet.font_size)


def draw_bipartite_matching(ax):
    BasicGraphSet.ax_set(ax, 'maximal matching')
    g = nx.Graph()
    g.add_edges_from([
        ('a', 'b'),
        ('a', 'c'),
        ('a', 'e'),
        ('b', 'd'),
        ('d', 'e')
    ])
    node_colors = []
    if nx.bipartite.is_bipartite(g):
        print('This graph is bipartite')
        l, r = nx.bipartite.sets(g)
        for node in g.nodes:
            if node in l:
                g.nodes[node]['color'] = 'green'
                node_colors.append('green')
            else:
                g.nodes[node]['color'] = 'yellow'
                node_colors.append('yellow')
    max_matching = nx.maximal_matching(g)  # a dict, eg {('a', 'b'), ('b', 'c)}
    edge_colors = BasicGraphSet.set_property_for_edges(g.edges, max_matching, 'r', 'black')
    nx.draw_networkx(g, pos=nx.circular_layout(g), ax=ax, with_labels=BasicGraphSet.with_labels,
                     node_size=BasicGraphSet.node_size, node_color=node_colors,
                     alpha=BasicGraphSet.alpha, width=BasicGraphSet.width,
                     edge_color=edge_colors, font_size=BasicGraphSet.font_size)


if __name__ == '__main__':
    # set figure
    fig = plt.figure(num='fig', figsize=(8, 12))

    # draw connected components
    ax1 = fig.add_subplot(321)
    draw_connected_compo(ax1)

    # draw directed graph
    ax2 = fig.add_subplot(322)
    draw_directed_graph(ax2)

    # draw minimal spanning tree
    ax3 = fig.add_subplot(323)
    draw_minimal_spanning_tree(ax3)

    # draw bipartite max matching
    ax4 = fig.add_subplot(324)
    draw_bipartite_matching(ax4)

    # print all graphs
    plt.show()
