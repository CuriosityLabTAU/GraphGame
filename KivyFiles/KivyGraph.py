#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.uix.widget import Widget
from random import randint
from KivyNode import KivyNode


class KivyGraph(Widget):
    center_coor = (0, 0)
    nodes = None
    edges = None
    center_node = None

    def __init__(self, center, zoom_rate, screen_size, **kwargs):
        super(KivyGraph, self).__init__(**kwargs)
        self.center_coor = center
        self.zoom_rate = zoom_rate
        self.nodes = []
        self.edges = []
        self.corners = self.set_screen_corners(screen_size)

    def set_screen_corners(self, screen_size):
        """
        function calculates the corners of the visible part of the screen which are used in order to determine
        which parts of the graph are visible
        """
        min_x = screen_size["min_x"]
        min_y = screen_size["min_y"]
        max_x = int(screen_size["max_x"]*(1/self.zoom_rate))
        max_y = int(screen_size["max_y"]*(1/self.zoom_rate))

        bottom_left = KivyNode(min_x, min_y, -1, 0, 0, 'white')
        top_left = KivyNode(min_x, max_y, -1, 0, 0, 'white')
        bottom_right = KivyNode(max_x, min_y, -1, 0, 0, 'white')
        top_right = KivyNode(max_x, max_y, -1, 0, 0, 'white')

        return {"bottom_left": bottom_left, "bottom_right": bottom_right, "top_left": top_left, "top_right": top_right}

    def add_node(self, node):
        """
        function adds a given node to the graph's nodes list
        """
        self.nodes.append(node)

    def add_edge(self, edge):
        """
        function adds a given edge to the graph's edges list
        """
        self.edges.append(edge)

    def get_by_serial(self, serial):
        """
        :param serial: a serial associated with the desired node
        :return: a node from the graph's nodes list associated with the given serial
        """
        for node in self.nodes:
            if node.serial == serial:
                return node
        raise Exception("Node '{}' was not found in node list. Node list = {}".format(serial, self.nodes))

    def move_up(self, amount=5):
        self.center_node = None
        for node in self.nodes:
            node.move_y(amount)
        for edge in self.edges:
            edge.reset_edge(False)

        self.corners["top_right"].move_y(-amount)
        self.corners["top_left"].move_y(-amount)
        self.corners["bottom_right"].move_y(-amount)
        self.corners["bottom_left"].move_y(-amount)

    def move_down(self, amount=-5):
        self.center_node = None
        for node in self.nodes:
            node.move_y(amount)
        for edge in self.edges:
            edge.reset_edge(False)

        self.corners["top_right"].move_y(-amount)
        self.corners["top_left"].move_y(-amount)
        self.corners["bottom_right"].move_y(-amount)
        self.corners["bottom_left"].move_y(-amount)

    def move_left(self, amount=-5):
        self.center_node = None
        for node in self.nodes:
            node.move_x(amount)
        for edge in self.edges:
            edge.reset_edge(False)

        self.corners["top_right"].move_x(-amount)
        self.corners["top_left"].move_x(-amount)
        self.corners["bottom_right"].move_x(-amount)
        self.corners["bottom_left"].move_x(-amount)

    def move_right(self, amount=5):
        self.center_node = None
        for node in self.nodes:
            node.move_x(amount)
        for edge in self.edges:
            edge.reset_edge(False)

        self.corners["top_right"].move_x(-amount)
        self.corners["top_left"].move_x(-amount)
        self.corners["bottom_right"].move_x(-amount)
        self.corners["bottom_left"].move_x(-amount)

    def print_graph_nodes(self):
        for node in self.nodes:
            node.print_node()

    def random_jump(self, animated=True):
        """
        function moves the coordinates of all the nodes in the graph by a random difference
        """
        x = randint(-100, 100)
        y = randint(-100, 100)
        for node in self.nodes:
            node.move_by_amount(x, y, animated)
        for edge in self.edges:
            edge.reset_edge(animated)

        self.corners["top_right"].move_by_amount(-x, -y, False)
        self.corners["top_left"].move_by_amount(-x, -y, False)
        self.corners["bottom_right"].move_by_amount(-x, -y, False)
        self.corners["bottom_left"].move_by_amount(-x, -y, False)

    def move_node_to_center(self, new_center, animated=True):
        """
        moves the graph so that a given node's coordinates are now 'center_coor' and sets given node as 'center_node'
        :param new_center: a node to be moved to the center of the screen
        :param animated: boolean. indicates whether the graph's movement should be shown visually
        """
        delta_x = self.center_coor[0] - new_center.get_x()
        delta_y = self.center_coor[1] - new_center.get_y()

        for node in self.nodes:
            node.move_by_amount(delta_x, delta_y, animated)
        for edge in self.edges:
            edge.reset_edge(animated)
        self.center_node = new_center

        corner_x = round((1/self.zoom_rate) * -delta_x, 2)
        corner_y = round((1/self.zoom_rate) * -delta_y, 2)
        self.corners["top_right"].move_by_amount(corner_x, corner_y, False)
        self.corners["top_left"].move_by_amount(corner_x, corner_y, False)
        self.corners["bottom_right"].move_by_amount(corner_x, corner_y, False)
        self.corners["bottom_left"].move_by_amount(corner_x, corner_y, False)

    def centralize_random_node(self, animated):
        """
        function chooses a random node and moves it to center of screen using the function "move_node_to_center"
        """
        i = randint(0, len(self.nodes) - 1)
        self.move_node_to_center(self.nodes[i], animated)

    def get_most_connected(self, node_list):
        """
        :param node_list: a list of nodes to be checked
        :return: the node (other than the graph's current 'center_node') out of 'node_list' that has the most neighbors
        """

        max_connections = 0
        most_connected_node = None
        for node in node_list:
            if node != self.center_node:
                curr_connections = node.get_amount_of_neighbors()
                if curr_connections > max_connections:
                    max_connections = curr_connections
                    most_connected_node = node
        return most_connected_node

    def get_closest(self, node_list, same_color):
        """
        finds the node out of node_list that is closest to the graph's current center_node
        :param node_list: a list of nodes to be checked
        :param same_color: indicates the color of desired node; -1: any color, 0: different color from center_node,
        1: same color as center_node.
        :return: The node from node_list that is closest to graph's center_node, in accordance with same_color flag
        """
        min_distance = -1
        closest_node = None
        color = self.center_node.get_colour()
        for node in node_list:
            if node != self.center_node:
                if (same_color == -1) or ((color == node.get_colour()) == same_color):
                    dist = self.center_node.get_distance_from_node(node)
                    if ((dist < min_distance) and (dist != -1)) or (min_distance == -1):
                        min_distance = dist
                        closest_node = node
        return closest_node

    def get_farthest(self, node_list, same_color):
        """
        finds the node out of node_list that is farthest from the graph's current center_node
        :param node_list: a list of nodes to be checked
        :param same_color: indicates the color of desired node; -1: any color, 0: different color from center_node,
        1: same color as center_node.
        :return: The node from node_list that is farthest from graph's center_node, in accordance with same_color flag
        """
        max_distance = 0
        farthest_node = None
        color = self.center_node.get_colour()
        for node in node_list:
            if node != self.center_node:
                if (same_color == -1) or ((color == node.get_colour()) == same_color):
                    dist = self.center_node.get_distance_from_node(node)
                    if dist > max_distance:
                        max_distance = dist
                        farthest_node = node
        return farthest_node

    def centralize_most_connected(self):
        """
        Finds, out of the nodes onscreen, the nodes with most neighbors and moves it to the center of the screen
        """
        node_list = self.get_onscreen_nodes(self.nodes)
        new_center = self.get_most_connected(node_list)
        if new_center is not None:
            self.move_node_to_center(new_center)

    def centralize_most_connected_neighbor(self):
        """
        Finds, out of the center_node's onscreen neighbors, the nodes with most neighbors and moves it to the center
        of the screen
        """
        node_list = self.get_onscreen_nodes(self.center_node.get_neighbors())
        new_center = self.get_most_connected(node_list)
        if new_center is not None:
            self.move_node_to_center(new_center)

    def centralize_closest_neighbor_same_color(self):
        """
        Finds, out of the center_node's onscreen neighbors, the node that is the closest to the center_node and has the
        same color as the center_node, and moves it to the center of the screen
        """
        node_list = self.get_onscreen_nodes(self.center_node.get_neighbors())
        new_center = self.get_closest(node_list, 1)
        if new_center is not None:
            self.move_node_to_center(new_center)

    def centralize_closest_same_color(self):
        """
        Finds, out of the nodes onscreen, the node that is the closest to the center_node and has the same
        color as the center_node, and moves it to the center of the screen
        """
        node_list = self.get_onscreen_nodes(self.nodes)
        new_center = self.get_closest(node_list, 1)
        if new_center is not None:
            self.move_node_to_center(new_center)

    def centralize_closest_neighbor_diff_color(self):
        """
        Finds, out of the center_node's onscreen neighbors, the node that is closest to the center_node and has a
        different color than the center_node, and moves it to the center of the screen
        """
        node_list = self.get_onscreen_nodes(self.center_node.get_neighbors())
        new_center = self.get_closest(node_list, 0)
        if new_center is not None:
            self.move_node_to_center(new_center)

    def centralize_farthest_neighbor(self):
        """
        Finds, out of the center_node's onscreen neighbors, the node that is the farthest from the center_node and moves
        it to the center of the screen
        """
        node_list = self.get_onscreen_nodes(self.center_node.get_neighbors())
        new_center = self.get_farthest(node_list, -1)
        if new_center is not None:
            self.move_node_to_center(new_center)

    def get_onscreen_nodes(self, node_list):
        """
        Function goes over node_list and checks which ones are displayed onscreen
        :param node_list: a list containing the nodes to be checked
        :return: A list containing the nodes from node_list that are at least partially displayed onscreen.
        """
        bl = self.corners['bottom_left']
        tr = self.corners['top_right']
        displayed_nodes = []
        for node in node_list:
            node_x = node.original_location[0]
            node_y = node.original_location[1]
            node_r = node.get_radius()/2.0

            if (node_x + node_r) > bl.get_x() and (node_x - node_r) < tr.get_x() and \
                    (node_y + node_r) > bl.get_y() and (node_y - node_r) < tr.get_y():
                displayed_nodes.append(node)
        return displayed_nodes
