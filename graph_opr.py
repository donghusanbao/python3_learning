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
        """
        Default setting for drawing a graph
        :param g: graph
        :param ax: matplotlib ax
        :return: none
        """
        nx.draw_networkx(g, pos=nx.circular_layout(g), ax=ax, with_labels=BasicGraphSet.with_labels,
                         node_size=BasicGraphSet.node_size, node_color=BasicGraphSet.node_color,
                         alpha=BasicGraphSet.alpha, width=BasicGraphSet.width,
                         edge_color=BasicGraphSet.edge_color, font_size=BasicGraphSet.font_size)

    @staticmethod
    def basic_draw_color(g, ax, edge_colors=None, node_colors=None):
        """
        Default setting for drawing a graph except the color settings of edges or nodes
        :param g: graph
        :param ax:  ax
        :param edge_colors: a sequence of the colors of edges
        :param node_colors: a sequence of the colors of nodes
        :return: None
        """
        if not (edge_colors or node_colors):
            BasicGraphSet.basic_draw(g, ax)
        edge_colors_modified = edge_colors if edge_colors else BasicGraphSet.edge_color
        node_colors_modified = node_colors if node_colors else BasicGraphSet.node_color
        nx.draw_networkx(g, pos=nx.circular_layout(g), ax=ax, with_labels=BasicGraphSet.with_labels,
                         node_size=BasicGraphSet.node_size, node_color=node_colors_modified,
                         alpha=BasicGraphSet.alpha, width=BasicGraphSet.width,
                         edge_color=edge_colors_modified, font_size=BasicGraphSet.font_size)

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

    @staticmethod
    def set_property_for_nodes(graph_nodes, match_nodes, g_prop, m_prop):
        """
        set special property value (m_prop) for match nodes, while common
        property value (g_prop) for all other nodes in a graph
        :param graph_nodes: graph edges
        :param match_nodes: tuple, list or dict
        :param g_prop: common property value, like 'white'
        :param m_prop: special property value, like 'red'
        :return: a list of property values followed the sequence of nodes in a graph
        """
        prop_list = []
        for node in graph_nodes:
            if node in match_nodes:
                prop_list.append(m_prop)
            else:
                prop_list.append(g_prop)
        return prop_list

    @staticmethod
    def set_edges_prop_by_nodes(graph_edges, match_nodes, g_prop, m_prop):
        """
        set special property value (m_prop) for matching edges whose vertices
        are in match_nodes, while common property value (g_prop) for all other
        edges in a graph
        :param graph_edges: all edges in a graph
        :param match_nodes:  matching vertices which are connected by matching edges
        :param g_prop: common property value
        :param m_prop: matching property value
        :return: None
        """
        prop_list = []
        for u, v in graph_edges:
            if u in match_nodes and v in match_nodes:
                prop_list.append(m_prop)
            else:
                prop_list.append(g_prop)
        return prop_list


def draw_directed_graph(ax):
    """
    Draw directed graph
    :param ax: ax
    :return: None
    """
    BasicGraphSet.ax_set(ax, 'Directed Graph')
    g = nx.DiGraph()
    g.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd')])
    g.add_edges_from([('e', 'f'), ('f', 't'), ('e', 't')])
    BasicGraphSet.basic_draw(g, ax)


def draw_connected_compo(ax):
    """
    count and draw connected components in a graph
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
    """
    Draw minimal spanning tree of a graph
    :param ax: ax
    :return:
    """
    BasicGraphSet.ax_set(ax, 'Minimal Spanning Tree')
    g = nx.Graph()
    ''''
    g.add_edges_from([
        ('a', 'b', {'weight': 2}),
        ('a', 'c', {'weight': 4}),
        ('a', 'e', {'weight': 3}),
        ('b', 'd', {'weight': 6}),
        ('c', 'e', {'weight': 7}),
        ('d', 'e', {'weight': 5})
    ])
    '''
    g.add_weighted_edges_from([('0', '1', 2), ('0', '2', 7), ('1', '2', 3),
                              ('1', '3', 8), ('1', '4', 5), ('2', '3', 1), ('3', '4', 4)])
    edge_labels = nx.get_edge_attributes(g, 'weight')  # dict
    # to do, something wrong in generating spanning tree
    spanning_tree = nx.minimum_spanning_tree(g, algorithm='kruskal')
    print('spanning tree is ', spanning_tree)
    edge_colors = BasicGraphSet.set_property_for_edges(g.edges, spanning_tree, 'black', 'yellow')
    BasicGraphSet.basic_draw_color(g, ax, edge_colors=edge_colors)
    nx.draw_networkx_edge_labels(g, pos=nx.circular_layout(g), ax=ax, edge_labels=edge_labels,
                                 font_size=20, font_color='r', label_pos=0.5)


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
    if not nx.bipartite.is_bipartite(g):
        print('This graph is not bipartite')
        return
    print('This graph is bipartite')
    l, r = nx.bipartite.sets(g)
    node_colors = BasicGraphSet.set_property_for_nodes(g.nodes, l, 'green', 'yellow')
    max_matching = nx.maximal_matching(g)  # a dict, eg {('a', 'b'), ('b', 'c)}
    edge_colors = BasicGraphSet.set_property_for_edges(g.edges, max_matching, 'black', 'r')
    BasicGraphSet.basic_draw_color(g, ax, edge_colors=edge_colors, node_colors=node_colors)


def draw_independent_set(ax):
    BasicGraphSet.ax_set(ax, 'Max Independent Set')
    g = nx.Graph()
    g.add_edges_from([
        ('a', 'b'),
        ('b', 'c'),
        ('b', 'd'),
        ('c', 'd'),
        ('d', 'a'),
        ('c', 'e'),
        ('e', 'a'),
        ('b', 'e'),
        ('a', 'c')
    ])
    # only one maximal independent set, e must be in this independent set
    indep_set = nx.maximal_independent_set(g, ['e'])
    node_colors = BasicGraphSet.set_property_for_nodes(g.nodes, indep_set, 'r', 'g')
    BasicGraphSet.basic_draw_color(g, ax, node_colors=node_colors)


def draw_clique(ax):
    BasicGraphSet.ax_set(ax, 'Max Clique')
    g = nx.Graph()
    g.add_edges_from([
        ('a', 'b'),
        ('b', 'c'),
        ('b', 'd'),
        ('c', 'd'),
        ('d', 'a'),
        ('c', 'e'),
        ('e', 'a'),
        ('b', 'e'),
        ('a', 'c')
    ])
    '''
    Describe: iterate all cliques in a graph, each clique is a list of nodes
    Codes:
    for clique in nx.enumerate_all_cliques(g):
        print('clique is ', clique)
    '''

    # Description: all maximal cliques in a graph
    cliques = nx.find_cliques(g)
    max_clique = None

    # networkx sometimes can not find the largest clique among all maximal cliques
    for clique in cliques:
        if not max_clique:
            max_clique = clique
        else:
            if len(clique) > len(max_clique):
                max_clique = clique
    node_colors = BasicGraphSet.set_property_for_nodes(g.nodes, max_clique, 'r', 'g')
    edge_colors = BasicGraphSet.set_edges_prop_by_nodes(g.edges, max_clique, 'r', 'g')
    BasicGraphSet.basic_draw_color(g, ax, edge_colors=edge_colors, node_colors=node_colors)


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

    # draw cliques
    ax5 = fig.add_subplot(325)
    draw_clique(ax5)

    # draw independent set
    ax6 = fig.add_subplot(326)
    draw_independent_set(ax6)

    # print all graphs
    plt.show()
