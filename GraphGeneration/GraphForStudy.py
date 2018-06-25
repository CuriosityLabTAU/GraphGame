from CreateRandGraph import *
from GraphValidator import *
import matplotlib.pyplot as plt
import numpy as np
from SupplementaryFiles.GraphSaveLoad import *
import networkx as nx
import matplotlib.pyplot as plt

# --- parameters ----
print('setting parameters')
Utils.read_graph_config_file('../graph_config.txt')
Utils.read_game_config_file('../game_config.txt')
config = Utils.graph_config_data

n_nodes = 11
min_neighbors = 1
max_neighbors = 4
buttons = np.array([1,2,4,3,4,2])
n_tries = 100

x_min = int(config["NodeData"]["NodeSize"])
x_max = 1500 # int(config["GeneralParams"]["GraphSizeX"]) - int(config["NodeData"]["NodeSize"])
y_min = int(config["NodeData"]["NodeSize"])
y_max = 1500 # int(config["GeneralParams"]["GraphSizeY"]) - int(config["NodeData"]["NodeSize"])


def graph_spring_layout(graph_):
    g = nx.Graph()
    for node in graph_.node_list:
        g.add_node(node.serial_num)
    g.add_edges_from(graph_.connections)
    pos = nx.spring_layout(g)
    for node_serial, node_pos in pos.items():
        for node in graph_.node_list:
            if node.serial_num == node_serial:
                node.x = int((node_pos[0] + 1.0) / 2.0 * (x_max - x_min) + x_min)
                node.y = int((node_pos[1] + 1.0) / 2.0 * (y_max - y_min) + y_min)
                break
    return graph_


def plot_graph(graph_, show=True):
    for node in graph_.node_list:
        plt.plot(node.x, node.y, 'x')
    for conn in graph_.connections:
        n1 = graph_.get_node_by_serial(conn[0])
        n2 = graph_.get_node_by_serial(conn[1])
        plt.plot([n1.x, n2.x], [n1.y, n2.y], '-')
    if show:
        plt.show()


def generate_graph():
    new_graph = GraphObject(max_x=2750, max_y=2850, node_count=15, max_neighbors=5, extra_distance=1)
    for i in range(n_nodes):
        x_random = random.randint(x_min, x_max)
        y_random = random.randint(y_min, y_max)
        rand_color = random.choice(Colours.values())
        new_graph.add_node(x_random, y_random, rand_color, Shapes['circle'], int(config["NodeData"]["NodeSize"]), serial='n%d' % i)
    new_graph = connect_graph(new_graph, max_neighbors, min_neighbors)
    return new_graph


candidate_graphs = []
while len(candidate_graphs) < 15:
    graph = generate_graph()

    graph = graph_spring_layout(graph)
    # plot_graph(graph, show=True)

    possible_graph = True
    try:
        answer, number_of_nodes_seen = run_buttons_on_graph(graph, buttons)
        print(number_of_nodes_seen)
    except:
        possible_graph = False
    if possible_graph:
        if answer:
            print('--------found %d----------' % len(candidate_graphs))
            print('found solvable graph')
            # check if others is also answer
            # first check if subgroup is also a solution
            answer_1, number_of_nodes_seen_1 = run_buttons_on_graph(graph, buttons[:-1])
            if not answer_1:
                # second check if others can give a solution
                no_other_answer = True
                for i_tries in range(n_tries):
                    try_buttons = np.random.choice(4,len(buttons),replace=True) + 1
                    if sum(np.power(try_buttons - buttons, 2.0)) > 0.0 :
                        try:
                            answer_2, number_of_nodes_seen_2 = run_buttons_on_graph(graph, try_buttons)
                            if answer_2:
                                no_other_answer = False
                                print('other solve it :(')
                                break
                        except:
                            pass
                    else:
                        print('same buttons')
                if no_other_answer:
                    print('found good graph!!!')
                    candidate_graphs.append((graph))
                    i_graph = len(candidate_graphs)
                    save_graph_json(graph, "Graph_study_n11_%d.json" % i_graph)
                    plt.clf()
                    plot_graph(graph, show=False)
                    plt.savefig("Graph_study_%d.png" % i_graph)
            else:
                print('solved by simpler button sequence :(')