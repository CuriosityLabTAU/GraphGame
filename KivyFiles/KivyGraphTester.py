#!/usr/bin/python
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.9.1')

from SupplementaryFiles.GraphObj import get_serial
from SupplementaryFiles.Point import Point
from SupplementaryFiles.LineEquation import LineEquation
from kivy.app import App
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.NodeObject import NodeObject
from SupplementaryFiles.Enums import Colours, QuestionTypes
from GameLayout import GameLayout
from GraphDisplay import GraphDisplay
from SupplementaryFiles.GameDataHandler import GameDataHandler
from kivy.core.window import Window


# This File contains classes used for testing throughout the development of the app

class GraphTester:
    """
    Class contains graphs and question used for testing
    """

    def __init__(self):
        pass

    @staticmethod
    def tester_graph_1():
        graph = GraphObject(None, 800, 400, 6, 4, 5)
        node1 = NodeObject(188, {'x': 369, 'y': 168}, 50, {'R': 1, 'G': 0, 'B': 0, 'name': "red"})
        node2 = NodeObject(-55, {'x': 480, 'y': 275}, 50, {'R': 0, 'G': 1, 'B': 0, 'name': "green"})
        node3 = NodeObject(640, {'x': 628, 'y': 169}, 50, {'R': 0, 'G': 0, 'B': 1, 'name': "blue"})
        node4 = NodeObject(206, {'x': 636, 'y': 306}, 50, {'R': 1, 'G': 0, 'B': 1, 'name': "magenta"})
        node5 = NodeObject(-67, {'x': 250, 'y': 289}, 50, {'R': 1, 'G': 1, 'B': 0, 'name': "yellow"})
        node6 = NodeObject(186, {'x': 184, 'y': 71}, 50, {'R': 0, 'G': 1, 'B': 1, 'name': "cyan"})
        graph.node_list.append(node1)
        graph.node_list.append(node2)
        graph.node_list.append(node3)
        graph.node_list.append(node4)
        graph.node_list.append(node5)
        graph.node_list.append(node6)
        graph.connections = [(640, 188), (-55, 206), (-55, 186), (-67, 640),
                             (-67, 206), (640, 206), (-67, 186), (640, 186)]
        graph.center_node = 188
        graph.question_object_list = GraphTester.create_questions()
        return graph

    @staticmethod
    def tester_graph_2():
        graph = GraphObject(None, 5000, 5000, 20, 3, 10)
        node1 = NodeObject("a26", {'x': 614, 'y': 600}, 50, Colours['yellow'])
        node2 = NodeObject("ce5", {'x': -2465, 'y': 2732}, 50, Colours['yellow'])
        node3 = NodeObject("4ec", {'x': -3229, 'y': 3455}, 50, Colours['red'])
        node4 = NodeObject("5e7", {'x': -1184, 'y': 3385}, 50, Colours['blue'])
        node5 = NodeObject("5ea", {'x': 303, 'y': 1050}, 50, Colours['red'])
        node6 = NodeObject("a97", {'x': -1128, 'y': 1884}, 50, Colours['blue'])
        node7 = NodeObject("5f3", {'x': -2910, 'y': 271}, 50, Colours['red'])
        node8 = NodeObject("68f", {'x': -1105, 'y': 1409}, 50, Colours['blue'])
        node9 = NodeObject("a0f", {'x': -1598, 'y': 4054}, 50, Colours['yellow'])
        node10 = NodeObject("b3b", {'x': 1047, 'y': 61}, 50, Colours['red'])
        node11 = NodeObject("379", {'x': -1034, 'y': 2046}, 50, Colours['red'])
        node12 = NodeObject("c5c", {'x': 1543, 'y': 4466}, 50, Colours['red'])
        node13 = NodeObject("97b", {'x': -2551, 'y': 1694}, 50, Colours['yellow'])
        node14 = NodeObject("ac2", {'x': 821, 'y': 4534}, 50, Colours['blue'])
        node15 = NodeObject("788", {'x': -2790, 'y': 2330}, 50, Colours['yellow'])
        node16 = NodeObject("01d", {'x': 450, 'y': 300}, 50, Colours['blue'])
        node17 = NodeObject("e29", {'x': -272, 'y': 910}, 50, Colours['yellow'])
        node18 = NodeObject("d21", {'x': -2329, 'y': 2245}, 50, Colours['blue'])
        node19 = NodeObject("7ac", {'x': 693, 'y': 3124}, 50, Colours['blue'])
        node20 = NodeObject("189", {'x': -2748, 'y': 3403}, 50, Colours['blue'])

        graph.node_list.append(node1)
        graph.node_list.append(node2)
        graph.node_list.append(node3)
        graph.node_list.append(node4)
        graph.node_list.append(node5)
        graph.node_list.append(node6)
        graph.node_list.append(node7)
        graph.node_list.append(node8)
        graph.node_list.append(node9)
        graph.node_list.append(node10)
        graph.node_list.append(node11)
        graph.node_list.append(node12)
        graph.node_list.append(node13)
        graph.node_list.append(node14)
        graph.node_list.append(node15)
        graph.node_list.append(node16)
        graph.node_list.append(node17)
        graph.node_list.append(node18)
        graph.node_list.append(node19)
        graph.node_list.append(node20)

        graph.connections = [('01d', 'e29'), ('01d', 'a97'), ('ac2', 'ce5'), ('379', 'ce5'), ('4ec', 'c5c'),
                             ('5e7', '68f'), ('5e7', '5ea'), ('5ea', '788'), ('a0f', 'a97'), ('5f3', 'b3b'),
                             ('68f', '7ac'), ('a0f', 'd21'), ('a26', 'b3b'), ('189', '379'), ('97b', 'c5c'),
                             ('97b', 'e29'), ('a26', 'ac2'), ('788', '7ac'), ('189', 'd21')]
        graph.center_node = "01d"

        return graph

    @staticmethod
    def create_questions():
        """
        Creates a list of QuestionObject
        """
        from KivyFiles.Questions.QuestionObject import QuestionObject
        question_one = QuestionObject("how many red nodes there are?", QuestionTypes['NUMBER'], 1, Colours['red'])
        question_three = QuestionObject("how many yellow nodes there are?", QuestionTypes['NUMBER'], 1, Colours['yellow'])
        question_five = QuestionObject("how many blue nodes there are?", QuestionTypes['NUMBER'], 1, Colours['blue'])

        question_list = [question_one, question_three, question_five]

        return question_list


class TestScreen:
    # A test screen to be used during testing
    graph_config = None
    max_turns = 6

    def __init__(self, graph, button_presses, button_ratio, real_user=True):
        self.graph = graph
        self.button_presses = button_presses
        self.button_ratio = button_ratio
        self.real_user = real_user

    def end_graph(self):
        App.get_running_app().stop()


class GraphGameApp(App):
    # Used in order to run the game of a single graph, without the questions or the result screen
    is_playing = True

    def __init__(self, game_screen=None, **kwargs):
        super(GraphGameApp, self).__init__(**kwargs)
        self.game_screen = game_screen
        self.original_graph = self.game_screen.graph
        self.current_data_handler = GameDataHandler(self.game_screen.graph_config, self.original_graph.size)
        self.max_turns = self.game_screen.max_turns
        self.button_presses = self.game_screen.button_presses
        self.layout = GameLayout(self)
        self.send_info_from_screen()

    def build(self):
        return self.layout

    def load(self):
        pass

    def send_info_from_screen(self):
        self.current_data_handler.add_view_to_db(self.get_info_from_screen())

    def end_game(self):
        self.is_playing = False
        self.game_screen.end_graph()

    def get_info_from_screen(self):
        """
        Function returns the nodes and edges that are at least partially displayed onscreen
        :return: returns a dictionary containing two objects:
        'nodes': A list containing the nodes that are at least partially displayed onscreen.
        'edges': A list representing the edges that are at least partially displayed onscreen. Each edge is represented
                 by a tuple containing the edge's nodes, the edge's original slope and the edge's equation. If one of
                 the nodes is not onscreen, a new NodeObject is created where the x,y coordinates represent the
                 intersection between the edge and the screen and the serial and size are set to None.
        """
        if self.layout.is_zoomed_out:
            graph_nodes = self.layout.kivy_graph_out.kivy_graph.nodes
            graph_edges = self.layout.kivy_graph_out.kivy_graph.edges
            graph_corners = self.layout.kivy_graph_out.kivy_graph.corners
        else:
            graph_nodes = self.layout.kivy_graph_in.kivy_graph.nodes
            graph_edges = self.layout.kivy_graph_in.kivy_graph.edges
            graph_corners = self.layout.kivy_graph_in.kivy_graph.corners

        nodes = self.get_onscreen_nodes(graph_nodes, graph_corners)
        edges = self.get_onscreen_edges(graph_edges, graph_corners)

        return {'nodes': nodes, 'edges': edges}

    def get_onscreen_nodes(self, graph_nodes, graph_corners):
        """
        Function goes over the list of nodes in the graph and checks which ones are displayed onscreen
        :return: A list containing the graph's nodes that are at least partially displayed onscreen.
        """
        bottom_left = graph_corners["bottom_left"]
        top_right = graph_corners["top_right"]
        displayed_nodes = []
        for node in graph_nodes:
            if node.serial != -1:
                real_node = self.original_graph.get_node_by_serial(node.serial)
                node_x = real_node.x
                node_y = real_node.y
                node_r = node.get_radius() + 0.9
                if (node_x + node_r) > bottom_left.get_x() and (node_x - node_r) < top_right.get_x() and \
                            (node_y + node_r) > bottom_left.get_y() and (node_y - node_r) < top_right.get_y():
                    displayed_nodes.append(real_node)
        return displayed_nodes

    def get_onscreen_edges(self, graph_edges, graph_corners):
        """
        Function goes over the list of edges in the graph and checks which ones are displayed onscreen
        :return: A list representing the edges that are at least partially displayed onscreen. Each edge is represented
                 by a tuple containing the edge's nodes, the edge's original slope and the edge's equation. If one of
                 the nodes is not onscreen, a new NodeObject is created where the x,y coordinates represent the
                 intersection between the edge and the screen, a new serial is created, size is set to 0 and real is
                 set to False.
        """

        # create equations representing the screen's boarders
        top_left = Point(graph_corners["top_left"].get_x(), graph_corners["top_left"].get_y())
        top_right = Point(graph_corners["top_right"].get_x() + 0.001, graph_corners["top_right"].get_y())
        bottom_left = Point(graph_corners["bottom_left"].get_x() + 0.001, graph_corners["bottom_left"].get_y())
        bottom_right = Point(graph_corners["bottom_right"].get_x(), graph_corners["bottom_right"].get_y())
        top = LineEquation.create_equation(top_left, top_right)
        bottom = LineEquation.create_equation(bottom_left, bottom_right)
        left = LineEquation.create_equation(bottom_left, top_left)
        right = LineEquation.create_equation(bottom_right, top_right)

        displayed_edges = []

        for edge in graph_edges:
            real_node1 = self.original_graph.get_node_by_serial(edge.node1.serial)
            real_node2 = self.original_graph.get_node_by_serial(edge.node2.serial)
            point1 = Point(real_node1.x, real_node1.y)
            point2 = Point(real_node2.x, real_node2.y)
            edge_equation = LineEquation.create_equation(point1, point2)
            edge.set_slope(edge_equation)

            if self.is_node_onscreen(edge.node1, graph_corners):
                if self.is_node_onscreen(edge.node2, graph_corners):
                    # both of edge's node are onscreen
                    if edge.node1.get_x() < edge.node2.get_x():
                        curr_edge = (real_node1, real_node2, edge.slope, edge_equation)
                    else:
                        curr_edge = (real_node2, real_node1, edge.slope, edge_equation)
                else:
                    # only the edge's first node in onscreen
                    curr_edge = self.get_partly_visible_edge(edge, top, bottom, left, right, edge.node1, edge_equation)
            elif self.is_node_onscreen(edge.node2, graph_corners):
                # only the edge's second node is onscreen
                curr_edge = self.get_partly_visible_edge(edge, top, bottom, left, right, edge.node2, edge_equation)
            else:
                # neither of the edge's nodes are onscreen
                curr_edge = self.get_partly_visible_edge(edge, top, bottom, left, right, None, edge_equation)

            if curr_edge is not None:
                displayed_edges.append(curr_edge)

        return displayed_edges

    def is_node_onscreen(self, node, screen_edges):
        """
        checks if a given node is onscreen
        :param node: the node to be checked
        :param screen_edges: boarders of the screen
        :return: boolean indicating if the node is/isn't onscreen
        """
        real_node = self.original_graph.get_node_by_serial(node.serial)
        node_x = real_node.x
        node_y = real_node.y
        node_r = node.get_radius() * 0.05
        return (node_x + node_r) > screen_edges["bottom_left"].get_x() and \
               (node_x - node_r) < screen_edges["top_right"].get_x() and \
               (node_y + node_r) > screen_edges["bottom_left"].get_y() and \
               (node_y - node_r) < screen_edges["top_right"].get_y()

    def get_partly_visible_edge(self, edge, top, bottom, left, right, node, edge_equation):
        """

        :param edge: an edge that can be seen onscreen but where at least one node is not visible
        :param top: equation representing the top border of the screen
        :param bottom: equation representing the bottom border of the screen
        :param left: equation representing the left border of the screen
        :param right: equation representing the right border of the screen
        :param node: the visible node connected to the edge, or None if no node is visible
        :param edge_equation: the equation of the checked edge
        :return: A tuple containing two NodeObjects, each representing a one of the edge's nodes, the edge's slope and
        the edge's equation. If one of the edge's nodes is not onscreen, the x,y coordinates represent the intersection
        between the edge and the screen, a new serial is created, size is set to 0 and real is set to False.
        """
        first_node = None
        second_node = None

        if node:
            first_node = self.original_graph.get_node_by_serial(node.serial)

        # check if edge collides with top border
        if LineEquation.check_collision_point(edge_equation, top):
            col_point = LineEquation.get_equation_collision_point(edge_equation, top)
            location = {'x': round(col_point.x, 2), 'y': round(col_point.y, 2)}
            if first_node is not None:
                second_node = NodeObject(serial=get_serial(), location=location, size=0)
                second_node.real = False
            else:
                first_node = NodeObject(serial=get_serial(), location=location, size=0)
                first_node.real = False

        # check if edge collides with bottom border
        if LineEquation.check_collision_point(edge_equation, bottom):
            col_point = LineEquation.get_equation_collision_point(edge_equation, bottom)
            location = {'x': round(col_point.x, 2), 'y': round(col_point.y, 2)}
            if first_node is not None:
                second_node = NodeObject(serial=get_serial(), location=location, size=0)
                second_node.real = False
            else:
                first_node = NodeObject(serial=get_serial(), location=location, size=0)
                first_node.real = False

        # check if edge collides with left border
        if LineEquation.check_collision_point(edge_equation, left):
            col_point = LineEquation.get_equation_collision_point(edge_equation, left)
            location = {'x': round(col_point.x, 2), 'y': round(col_point.y, 2)}
            if first_node is not None:
                second_node = NodeObject(serial=get_serial(), location=location, size=0)
                second_node.real = False

            else:
                first_node = NodeObject(serial=get_serial(), location=location, size=0)
                first_node.real = False

        # check if edge collides with right border
        if LineEquation.check_collision_point(edge_equation, right):
            col_point = LineEquation.get_equation_collision_point(edge_equation, right)
            location = {'x': round(col_point.x, 2), 'y': round(col_point.y, 2)}
            if first_node is not None:
                second_node = NodeObject(serial=get_serial(), location=location, size=0)
                second_node.real = False
            else:
                first_node = NodeObject(serial=get_serial(), location=location, size=0)
                first_node.real = False

        if second_node is None:
            if first_node is None:
                return None
            else:
                raise Exception("Only One viable node for onscreen edge: {}".format(edge.print_by_serial()))

        min_dist = edge.node1.get_radius() / 2
        if first_node.distance(second_node) < min_dist:
            return None

        if first_node.x < second_node.x:
            curr_edge = (first_node, second_node, edge.slope, edge_equation)
        else:
            curr_edge = (second_node, first_node, edge.slope, edge_equation)

        return curr_edge

    def stop_me(self):
        self.stop()


class DisplayApp(App):
    # Used in order to view an entire graph onscreen

    def __init__(self, graph, **kwargs):
        super(DisplayApp, self).__init__(**kwargs)
        dim = (kivy.core.window.Window.size[0], kivy.core.window.Window.size[1])
        self.layout = GraphDisplay(graph, dim)

    def build(self):
        return self.layout
