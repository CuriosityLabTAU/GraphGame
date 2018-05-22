#!/usr/bin/python
# -*- coding: utf-8 -*-
from KivyGraph import KivyGraph
from KivyEdge import KivyEdge
from kivy.graphics import Color
from KivyNode import KivyNode
from kivy.uix.relativelayout import RelativeLayout


class GraphLayout(RelativeLayout):

    def __init__(self, original_graph, dim, zoom_rate, edge_size, **kwargs):
        """

        :param original_graph: the graph we want to display
        :param dim: screen's dimensions
        :param zoom_rate: percentage by which to enlarge/compress the graph (used for zoom)
        :param edge_size: size of the graph's edges
        """
        super(GraphLayout, self).__init__(size_hint_x=None, width=dim['max_x'], **kwargs)
        self.dim = {"min_x": 0, "min_y": 0, "max_x": dim['max_x'], "max_y": dim['max_y']}
        center_screen = self.get_center_coor()
        self.kivy_graph = KivyGraph(center_screen, zoom_rate, self.dim)
        self.get_nodes(original_graph, zoom_rate)
        self.get_edges(original_graph, zoom_rate, edge_size)
        self.kivy_graph.move_node_to_center(self.kivy_graph.get_by_serial(original_graph.center_node), False)

    def get_center_coor(self):
        """
        :return: the coordination of the center of the screen
        """
        x = self.dim['max_x'] / 2.0
        y = self.dim['max_y'] / 2.0
        return x, y

    def get_nodes(self, original_graph, zoom_rate):
        """
        for each NodeObject from the original graph (of type GraphObj) this function creates
        an equivalent KivyNode and adds it to the kivy graph (of type KivyGraph)
        """
        with self.canvas:
            for node in original_graph.node_list:
                colour = node.colour
                Color(colour['R'], colour['G'], colour['B'])
                new_node = KivyNode(node.x, node.y, node.serial_num, zoom_rate*node.size, node.size, colour['name'])
                new_node.relative_move(zoom_rate, zoom_rate)
                self.kivy_graph.add_node(new_node)

    def get_edges(self, original_graph, zoom_rate, size):
        """
        function creates a KivyEdge that represents the neighbors in the original graph (GraphObj), adds created
         edge to the kivy graph (KivyGraph), and adds the nodes (KivyNodes) connected to the edge to each other's
          list of neighbors
        """
        edges = original_graph.get_connections()
        with self.canvas:
            Color(1, 1, 1)
            for edge in edges:
                node1 = self.kivy_graph.get_by_serial(edge[0])
                node2 = self.kivy_graph.get_by_serial(edge[1])
                new_edge = KivyEdge(node1, node2, zoom_rate*size)
                self.kivy_graph.add_edge(new_edge)
                node1.add_neighbor(node2)
                node2.add_neighbor(node1)
