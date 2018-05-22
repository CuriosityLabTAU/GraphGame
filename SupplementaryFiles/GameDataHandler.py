#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import namedtuple
import logging

from os import path
from SupplementaryFiles.GLogger import *
from SupplementaryFiles.Utils import Utils
from SupplementaryFiles.NodeObject import NodeObject
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.LineEquation import LineEquation, LINES_ALWAYS_MEET
LOG_LEVEL = logging.DEBUG
GRAPH_CONFIG_PATH = path.join("..", "GraphsData", "graph_config.txt")
"""
Handles all data return from the window. Constructs a new graph based on the supplied data.
"""


class GameDataHandler:
    graph = None

    def __init__(self, config, graph_size=None):
        # basic_config -
        self.edges = []
        self.graph = GraphObject(config)
        self.graph.size = graph_size if graph_size is not None else self.graph.size
        self.extra_edges = []
        self.new_edges = []
        self.edges_to_add = []
        self.log = logging.getLogger()
        self.config = Utils.graph_config_data
        self.log.setLevel(Utils.game_config_data['Default']['log_level'])

    def get_number_of_known_nodes(self):
        return len([real_node for real_node in self.graph.node_list if real_node.real])

    def add_view_to_db(self, view):
        """
        Go over the new view gotten from the game. For each new node add it to self.graph.node_list
        For each edge check both ends. if the node has real=False we know it's only a placeholder.
        Update the graph of BasicGamer
        :param view: A dictionary containing the data gotten from the screen
        :return: None
        """
        # Innumerate over the nodes
        for node in view['nodes']:
            if self.graph.get_node_by_serial(node.serial_num) is None:
                self.graph.add_node(node.x, node.y, node_colour=node.colour, node_size=node.size,
                                    serial=node.serial_num)
                num = self.graph.get_node_by_serial(node.serial_num).dummy_num
                #self.log.info("Adding node:  num="+ str(num)+ ", real=True", location="{}:{}".format(node.x, node.y),serial=node.serial_num)
        # Innumerate over the edges
        for edge in view['edges']:
            if self.graph.get_node_by_serial(edge[0].serial_num) is not None:
                node_0 = self.graph.get_node_by_serial(edge[0].serial_num)
            else:
                node_0 = self.graph.add_node(edge[0].x, edge[0].y, node_size=1, real=False,
                                             serial=edge[0].serial_num)
                num = self.graph.get_node_by_serial(node_0.serial_num).dummy_num
                GLogger.log(logging.DEBUG,Utils.format_log_msg("Adding node",num=num, real=False,
                              location="{}:{}".format(node_0.x, node_0.y), serial=node_0.serial_num))

            if self.graph.get_node_by_serial(edge[1].serial_num) is not None:
                node_1 = self.graph.get_node_by_serial(edge[1].serial_num)
            else:
                node_1 = self.graph.add_node(edge[1].x, edge[1].y, node_size=1, real=False,
                                             serial=edge[1].serial_num)
                num = self.graph.get_node_by_serial(node_1.serial_num).dummy_num
                GLogger.log(logging.DEBUG, Utils.format_log_msg("Adding node",num=num, real=False,
                              location="{}:{}".format(node_1.x, node_1.y), serial=node_1.serial_num))

            if node_1.serial_num not in node_0.possible_neighbors:
                node_0.possible_neighbors.add(node_1.serial_num)
            if node_0.serial_num not in node_1.possible_neighbors:
                node_1.possible_neighbors.add(node_0.serial_num)
            self.graph.connect_nodes(node_0, node_1, allow_overflow=True)

            if edge not in self.extra_edges:
                self.extra_edges.append(edge)

        self.edges_to_add = []
        GLogger.log(logging.DEBUG, "Triming data from graph")
        self.trim_data()
        GLogger.log(logging.DEBUG, "Adding extra edges to edge list")
        for item in self.edges_to_add:
            self.extra_edges.append(item)
        self.clear_empty_nodes()
        GLogger.log(logging.DEBUG, Utils.format_log_msg("Finished triming data:", num_of_node=len(self.graph.node_list),
                      num_real_node=(len([item for item in self.graph.node_list if item.is_real()])),
                      num_of_edges=len(self.extra_edges)))
        GLogger.log(logging.DEBUG, Utils.format_log_msg("edge list:", edges=self.extra_edges))

    def trim_data(self):
        """
        Goes over all of the data that is saved and trims nodes and edges.
        Connects fake nodes to real ones if we found the actual node
        connects open edges together if possible
        """
        slope_set = set()
        for edge in self.extra_edges:
            slope_set.add(edge[3].slope)

        sorted(slope_set)
        GLogger.log(logging.DEBUG,"Number of slops found = {}".format(len(slope_set)))
        for slope in list(slope_set):
            edges_to_check = []
            for edge in self.extra_edges:
                if edge[3].slope == slope:
                    edges_to_check.append(edge)
            GLogger.log(logging.DEBUG,Utils.format_log_msg("Number of edges in slope: ",slope="{} = {}".format(slope, len(edges_to_check)), edges=edges_to_check))
            if len(edges_to_check) > 1:
                # we have two edges with the same slope!
                # Removing all edges from list. We add only the relevant ones later on
                for item in edges_to_check:
                    self.extra_edges.remove(item)
                while True:
                    first_edge = edges_to_check.pop()
                    edge_reconstructed = False
                    for second_edge in edges_to_check:
                        if self.two_edges_are_one(first_edge, second_edge):
                            GLogger.log(logging.DEBUG, "two edges are one")
                            edge_reconstructed = True
                            edges_to_check.remove(second_edge)
                            edges_to_check.append(self.connect_edges(first_edge, second_edge))
                            break
                    if not edge_reconstructed:
                        # edge does not match any other on the list. We can leave it alone
                        self.edges_to_add.append(first_edge)
                    if len(edges_to_check) <= 1:
                        self.edges_to_add.append(edges_to_check[0])
                        break

    def two_edges_are_one(self, edge_1, edge_2):
        """
        Checks if the two edges are actually a single edge.
        :return: True if edges are 100% the same one
        """

        eq1 = LineEquation(slope=edge_1[3].slope,
                           const=edge_1[3].const,
                           edge1=edge_1[0],
                           edge2=edge_1[1])
        eq2 = LineEquation(slope=edge_2[3].slope,
                           const=edge_2[3].const,
                           edge1=edge_2[0],
                           edge2=edge_2[1])


        # Check collision point
        collision_point = LineEquation.get_equation_collision_point(eq1, eq2)
        GLogger.log(logging.DEBUG, Utils.format_log_msg("Found collision point of both edges", point=collision_point, eq1=eq1, eq2=eq2))
        if collision_point == LINES_ALWAYS_MEET:
            # Lines have the same slope + const. Big change they are the same one.
            if LineEquation.check_collision_point(eq1, eq2):
                GLogger.log(logging.DEBUG, "Lines meet and intersect with each other - They are the same line")
                return True
            else:
                GLogger.log(logging.DEBUG, "Lines have the same parameters but we are not sure if they meet")
                return False
        return False

    def connect_edges(self, edge_1, edge_2):
        """
        The longest distance in an edge is the distance between the real nodes of that edge.
        We clean all existing connections and then connect the two nodes that are furthest from each other.
        :param edge_1, edge_2: An edge defined by a tuple of NodeObjects
        :returns the new edge created
        """
        # Cleaning all existing connection
        # self.log.debug("Connecting edges", edge1=edge_1, edge2=edge_2)
        if edge_1 in self.extra_edges:
            GLogger.log(logging.DEBUG, "Removing edge from extra edges", removed_edge=edge_1)
            self.extra_edges.remove(edge_1)
        if edge_2 in self.extra_edges:
            GLogger.log(logging.DEBUG, "Removing edge from extra edges", removed_edge=edge_2)
            self.extra_edges.remove(edge_2)

        if edge_1[0] is None or edge_1[1] is None or edge_2[0] is None or edge_2[1] is None:
            raise Exception("Cleaning Nodes failed - At least one of the nodes does not exist")

        self.clean_connection(edge_1[0], edge_1[1])
        self.clean_connection(edge_1[1], edge_1[0])
        if edge_2[0] != edge_1[0] or edge_2[1] != edge_2[1]:
            self.clean_connection(edge_2[0], edge_2[1])
            self.clean_connection(edge_2[1], edge_2[0])

        node_1_serial, node_2_serial = self.get_furthest_nodes(edge_1[0], edge_1[1], edge_2[0], edge_2[1])
        node_1 = self.graph.get_node_by_serial(node_1_serial)
        node_2 = self.graph.get_node_by_serial(node_2_serial)

        # connect the right nodes
        self.connect_nodes(node_1, node_2)
        if node_1.x < node_2.x:
            new_edge = (node_1, node_2, edge_1[2],  LineEquation(slope=edge_1[3].slope,
                                                                 const=edge_1[3].const,
                                                                 edge1=node_1,
                                                                 edge2=node_2))
        else:
            new_edge = (node_2, node_1, edge_1[2],  LineEquation(slope=edge_1[3].slope,
                                                                 const=edge_1[3].const,
                                                                 edge1=node_2,
                                                                 edge2=node_1))
        #self.edges_to_add.append(new_edge)
        return new_edge

    def clean_connection(self, main_node, node_to_remove):
        """
        Removed all connection from main_node regarding node_to_remove
        :param node_to_remove: The node to remove - node object
        :param main_node: The node we want to remove data from - node object
        :return: 
        """
        GLogger.log(logging.DEBUG, Utils.format_log_msg("Cleaning connection to another node", main_node=main_node.dummy_num,
                       node_to_remove=node_to_remove.dummy_num))
        node = self.graph.get_node_by_serial(main_node.serial_num)
        if node is None:
            raise Exception("Node '{}' was not found in node list. Node list = {}"
                            .format(main_node.dummy_num,
                                    [found_nodes.dummy_num for found_nodes in self.graph.node_list]))
        if node_to_remove.serial_num in node.neighbors:
            node.neighbors.remove(node_to_remove.serial_num)
        if node_to_remove.serial_num in node.possible_neighbors:
            node.possible_neighbors.remove(node_to_remove.serial_num)

    def connect_nodes(self, first_node, second_node):
        """
        Connect the two nodes in the graph.
        """
        node_0 = self.graph.get_node_by_serial(first_node.serial_num)
        node_1 = self.graph.get_node_by_serial(second_node.serial_num)

        node_0.possible_neighbors.add(node_1.serial_num)
        node_1.possible_neighbors.add(node_0.serial_num)
        self.graph.connect_nodes(node_0, node_1, allow_overflow=True)

    @staticmethod
    def get_furthest_nodes(*args):
        """
        :param args: a list of NodeObjects
        :return: The serial numbers of the two furthest nodes from each of other.
        """

        node_list = {}
        DistanceTuple = namedtuple('Distance', ['point', 'distance'])
        for node in args:
            if type(node) != NodeObject:
                raise Exception("One of the arguments is not of type NodeObjects - {}".format(node))
            distance_list = []
            for other_node in args:
                if other_node != node:
                    distance_list.append(DistanceTuple(point=other_node, distance=node.distance(other_node)))
            node_list[node.serial_num] = distance_list

        best_distance = 0
        best_pair = ()
        for node in args:
            for other_node in node_list[node.serial_num]:
                if other_node.distance > best_distance:
                    best_pair = (node.serial_num, other_node[0].serial_num)
                    best_distance = other_node[1]
        return best_pair

    def clear_empty_nodes(self):
        """
        Go over node list and see if two nodes are the same.
        :return: 
        """
        remove_list = []
        GLogger.log(logging.DEBUG, "removing nodes with no neighbors")
        for node in self.graph.node_list:
            if len(node.neighbors) == 0:
                GLogger.log(logging.DEBUG, Utils.format_log_msg("Found node with no neighbors - deleting:", serial=node.serial_num, real=node.is_real()))
                remove_list.append(node.serial_num)
        for serial in remove_list:
            self.graph.node_list.remove(self.graph.get_node_by_serial(serial))
        GLogger.log(logging.DEBUG, "removed {} nodes".format(len(remove_list)))

    def cleaned_graph(self):
        """
        Called at the end of a run. Cleans the graph of none real connections
        This is really just a patch because we enter bad connections. We should probably fix the source of the issue
        :return: the cleaned graph
        """
        self.graph.connections = []
        for edge in self.extra_edges:
            if edge[0].is_real() and edge[1].is_real():
                self.graph.connections.append((min(edge[0].serial_num, edge[1].serial_num),
                                               max(edge[0].serial_num, edge[1].serial_num)))
            else:
                self.clean_connection(edge[0], edge[1])
                self.clean_connection(edge[1], edge[0])
        self.extra_edges = []
        real_nodes = []
        for node in self.graph.node_list:
            if node.is_real():
                nodes_to_remove = []
                for neightbor in node.neighbors:
                    if not self.graph.get_node_by_serial(neightbor).is_real():
                        nodes_to_remove.append(self.graph.get_node_by_serial(neightbor))
                for item in nodes_to_remove:
                    self.clean_connection(node, item)
                real_nodes.append(node)

        # Make sure we see only the same edge once
        self.graph.connections = list(set(self.graph.connections))
        GLogger.log(logging.DEBUG, Utils.format_log_msg("Finished cleaning graph before continuing:", num_of_nodes=len(self.graph.node_list),
                                      num_real_nodes=(len([item for item in self.graph.node_list if item.is_real()])),
                                      num_of_connections=len(self.graph.connections)))
        self.graph.node_list = real_nodes
        return self.graph

    def get_real_nodes(self):
        return [item for item in self.graph.node_list if item.is_real()]
