#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import random

import SupplementaryFiles.LineEquation
from SupplementaryFiles.Utils import Utils
from SupplementaryFiles.Enums import Colours, Shapes
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.NodeObject import NodeObject


def create_rand_graph(config_file):
    """

    :param config_file:
    :return:
    """
    new_graph = GraphObject(config_file)
    config = Utils.read_game_config_file(config_file)

    for i in range(config.getint("GeneralParams", "NodeCount")):
        while True:
            xRandom = random.randint(config.getint("NodeData", "NodeSize"),
                                     config.getint("GeneralParams", "GraphSizeX") - config.getint("NodeData",
                                                                                                  "NodeSize"))
            yRandom = random.randint(config.getint("NodeData", "NodeSize"),
                                     config.getint("GeneralParams", "GraphSizeY") - config.getint("NodeData",
                                                                                                  "NodeSize"))
            if not check_collisions(xRandom, yRandom,
                                    new_graph,
                                    config.getint("NodeData", "NodeSize"),
                                    config.getint("NodeData", "ExtraDistance")):
                break
        randColor = random.choice(Colours.values())
        new_graph.add_node(xRandom, yRandom, randColor, Shapes['circle'], config.getint("NodeData", "NodeSize"))
    connect_graph(new_graph, config.getint("NodeData", "MaxNeighbors"), config.getint("NodeData", "MinNeighbors"))
    return new_graph


def connect_graph(graph, max_connections, min_connections):
    # Get possible connections for each node
    for node in graph.node_list:
        graph.get_possible_connections(node.serial_num)

    # Connect nodes
    for node in graph.node_list:
        # makes sure we don't exceed the maximum connections allowed
        max_possible_connections = min(max_connections-1, len(node.possible_neighbors) + len(node.neighbors)) - len(node.neighbors)
        if max_possible_connections > 0:
            # Determine how many connections the specific node will have
            connections = random.randint(min_connections, max_possible_connections)
            logging.debug("Connecting node '{}' to {} nodes".format(node.serial_num, connections))
            for i in range(connections):
                possible_node = graph.get_best_connection(node)
                graph.connect_nodes(node, graph.get_node_by_serial(possible_node))
    return graph


def connect_graph_2(graph, max_connections=5, min_connections=1):
    # Option B for connecting the graph. not allow crossing
    for node in graph.node_list:
        graph.get_possible_connections(node.serial_num)


def check_cross(graph, serial1, serial2):
    line_equation = graph.create_equation(graph.get_node_by_serial(serial1), graph.get_node_by_serial(serial2))
    cross = False
    for connection in graph.get_connections():
        new_equation = graph.create_equation(graph.get_node_by_serial(connection[0]),
                                             graph.get_node_by_serial(connection[1]))
        print(line_equation.edge1, line_equation.edge2, new_equation.edge1, new_equation.edge2)
        if SupplementaryFiles.LineEquation.check_collision_point(line_equation, new_equation):
            return True
    return cross


def check_collisions(x_location, y_location, graph, node_size, extra_space):
    """

    :param x_location:
    :param y_location:
    :param graph:
    :param node_size:
    :param extra_space:
    :return:
    """
    temp_node = NodeObject('0', {'x': x_location, 'y': y_location}, node_size)
    collision = False
    for node in graph.node_list:
        if temp_node.distance(node) < node_size + node.size + extra_space * 2:
            collision = True
    return collision


def test_random_graph():
    create_rand_graph("graph_config.txt")


if __name__ == '__main__':
    test_random_graph()