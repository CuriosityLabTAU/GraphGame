import time
import unittest
from os import path

from bunch import Bunch
from mock import patch, MagicMock, Mock

from GraphGeneration.CreateRandGraph import create_rand_graph
from SupplementaryFiles.GameDataHandler import GameDataHandler
from SupplementaryFiles.LineEquation import LineEquation
from SupplementaryFiles.NodeObject import NodeObject
from SupplementaryFiles.Utils import Utils
from main import CONFIG_FILE_PATH, GRAPH_CONFIG_PATH

MIN_VALUE = 0.0001
MAX_VALUE = 1


class TestGameDataHandler(unittest.TestCase):
    def setUp(self):
        self.node_1_real = NodeObject(serial=10, location={'x': 100, 'y': 100}, size=1, real=True)
        self.node_1_unreal = NodeObject(serial=11, location={'x': 100, 'y': 100}, size=1, real=False)
        self.node_2_real = NodeObject(serial=20, location={'x': 200, 'y': 200}, size=1, real=True)
        self.node_2_unreal = NodeObject(serial=21, location={'x': 200, 'y': 200}, size=1, real=False)
        self.node_2_unreal_moved = NodeObject(serial=22, location={'x': 205, 'y': 205}, size=1, real=False)
        self.node_3_real = NodeObject(serial=30, location={'x': 300, 'y': 300}, size=1, real=True)
        self.node_3_unreal = NodeObject(serial=31, location={'x': 300, 'y': 300}, size=1, real=False)
        self.node_3_unreal_moved = NodeObject(serial=32, location={'x': 305, 'y': 305}, size=1, real=False)
        self.node_4_real = NodeObject(serial=40, location={'x': 400, 'y': 400}, size=1, real=True)
        self.node_4_unreal = NodeObject(serial=41, location={'x': 400, 'y': 400}, size=1, real=False)

        self.node_list = [self.node_1_real, self.node_1_unreal, self.node_2_real, self.node_2_unreal, self.node_3_real,
                          self.node_3_unreal, self.node_4_real, self.node_4_unreal]

    def test_get_furthest_nodes(self):
        # Assemble
        node_1 = NodeObject(serial=1, location={'x': 1, 'y': 1}, size=1, real=True)
        node_2 = NodeObject(serial=2, location={'x': 2, 'y': 2}, size=1, real=True)
        node_3 = NodeObject(serial=3, location={'x': 3, 'y': 3}, size=1, real=True)
        node_4 = NodeObject(serial=4, location={'x': 4, 'y': 4}, size=1, real=True)

        # Act
        res = GameDataHandler.get_furthest_nodes(node_1, node_2, node_3, node_4)

        # Assert
        self.assertIn(node_1.serial_num, res, "node with serial number {0} was not returned by function."
                                              " Got {1}".format(node_1.serial_num, res))
        self.assertIn(node_4.serial_num, res, "node with serial number {0} was not returned by function."
                                              " Got {1}".format(node_4.serial_num, res))

    @patch('SupplementaryFiles.GameDataHandler.Utils')
    @patch('SupplementaryFiles.GameDataHandler.GraphObject.connect_nodes')
    @patch('SupplementaryFiles.GameDataHandler.GraphObject.get_node_by_serial')
    def test_connect_nodes(self, mock_get_node_by_serial, mock_connect_nodes, mock_utils):
        # Assemble
        node_1 = NodeObject(serial=1, location={'x': 1, 'y': 1}, size=1, real=True)
        node_2 = NodeObject(serial=2, location={'x': 2, 'y': 2}, size=1, real=True)

        mock_get_node_by_serial.side_effect = [node_1, node_2]
        mock_connect_nodes.return_value = None
        mock_utils.graph_config_data = None
        mock_utils.game_config_data = {'Default': {'log_level': 'ERROR'}}
        data_handler = GameDataHandler(None, None)

        # Act
        data_handler.connect_nodes(node_1, node_1)

        # Assert
        mock_connect_nodes.called_once(node_1, node_1, allow_overflow=True)

    @patch('SupplementaryFiles.GameDataHandler.Utils')
    def test_two_edges_are_one(self, mock_utils):
        # Assemble
        node_1 = NodeObject(serial=1, location={'x': 100, 'y': 100}, size=1, real=True)
        node_2 = NodeObject(serial=2, location={'x': 200, 'y': 200}, size=1, real=True)
        node_3 = NodeObject(serial=3, location={'x': 300, 'y': 300}, size=1, real=True)
        node_4 = NodeObject(serial=4, location={'x': 400, 'y': 400}, size=1, real=True)
        node_5 = NodeObject(serial=4, location={'x': 100, 'y': 400}, size=1, real=True)

        mock_utils.graph_config_data = None
        mock_utils.game_config_data = {'Default': {'log_level': 'ERROR'}}
        data_handler = GameDataHandler(None, None)

        edge_35 = (node_3, node_5, node_3.slope(node_5),
                   LineEquation(slope=node_3.slope(node_5), const=1, edge1=node_3, edge2=node_5))
        edge_24 = (node_2, node_4, node_2.slope(node_4),
                   LineEquation(slope=node_2.slope(node_4), const=1, edge1=node_2, edge2=node_4))
        edge_12 = (node_1, node_2, node_1.slope(node_2),
                   LineEquation(slope=node_1.slope(node_2), const=1, edge1=node_1, edge2=node_2))
        edge_13 = (node_1, node_3, node_1.slope(node_3),
                   LineEquation(slope=node_1.slope(node_3), const=1, edge1=node_1, edge2=node_3))
        edge_34 = (node_3, node_4, node_3.slope(node_4),
                   LineEquation(slope=node_3.slope(node_4), const=1, edge1=node_3, edge2=node_4))

        # Act

        res_miss = data_handler.two_edges_are_one(edge_35, edge_24)
        res_not_sure = data_handler.two_edges_are_one(edge_12, edge_34)
        res_hit = data_handler.two_edges_are_one(edge_13, edge_24)
        res_hit_same_point = data_handler.two_edges_are_one(edge_12, edge_13)
        res_same_edge = data_handler.two_edges_are_one(edge_12, edge_12)

        # Assert
        self.assertFalse(res_not_sure)
        self.assertFalse(res_miss)
        self.assertTrue(res_hit)
        self.assertTrue(res_hit_same_point)
        self.assertTrue(res_same_edge)

    @patch('SupplementaryFiles.GameDataHandler.Utils')
    @patch('SupplementaryFiles.GameDataHandler.GameDataHandler.connect_nodes')
    @patch('SupplementaryFiles.GameDataHandler.GameDataHandler.clean_connection')
    @patch('SupplementaryFiles.GameDataHandler.GraphObject.get_node_by_serial')
    def test_connect_edges_advanced(self, mock_get_node_by_serial, mock_clean, mock_connect, mock_utils):

        def mock_get_node(serial):
            for node in self.node_list:
                if node.serial_num == serial:
                    return node
            return None

        # Assemble
        mock_get_node_by_serial.side_effect = mock_get_node
        mock_utils.graph_config_data = None
        mock_utils.game_config_data = {'Default': {'log_level': 'ERROR'}}
        data_handler = GameDataHandler(None, None)

        edge_two_real_14 = (self.node_1_real, self.node_4_real, self.node_1_real.slope(self.node_4_real),
                            LineEquation(slope=self.node_1_real.slope(self.node_4_real),
                                         const=1, edge1=self.node_1_real,
                                         edge2=self.node_4_real))
        edge_left_real_13 = (self.node_1_real, self.node_3_unreal, self.node_1_real.slope(self.node_3_unreal),
                             LineEquation(slope=self.node_1_real.slope(self.node_3_unreal),
                                          const=1, edge1=self.node_1_real,
                                          edge2=self.node_3_unreal))
        edge_left_real_12 = (self.node_1_real, self.node_2_unreal, self.node_1_real.slope(self.node_2_unreal),
                             LineEquation(slope=self.node_1_real.slope(self.node_2_unreal),
                                          const=1, edge1=self.node_1_real,
                                          edge2=self.node_2_unreal))
        edge_right_real_24 = (self.node_2_unreal, self.node_4_real, self.node_2_unreal.slope(self.node_4_real),
                              LineEquation(slope=self.node_2_unreal.slope(self.node_4_real),
                                           const=1, edge1=self.node_2_unreal,
                                           edge2=self.node_4_real))
        edge_two_unreal_23 = (self.node_2_unreal, self.node_3_unreal, self.node_2_unreal.slope(self.node_3_unreal),
                              LineEquation(slope=self.node_2_unreal.slope(self.node_3_unreal),
                                           const=1, edge1=self.node_2_unreal,
                                           edge2=self.node_3_unreal))
        edge_two_unreal_13 = (self.node_1_unreal, self.node_3_unreal, self.node_1_unreal.slope(self.node_3_unreal),
                              LineEquation(slope=self.node_1_unreal.slope(self.node_3_unreal),
                                           const=1, edge1=self.node_1_unreal,
                                           edge2=self.node_3_unreal))

        # Act + Assert

        # Case 1 - One edge is connected to two real nodes. Other edge only connects to one real node and the other
        #  to a fake node
        edge = data_handler.connect_edges(edge_two_real_14, edge_left_real_13)
        mock_connect.assert_called_with(self.node_1_real, self.node_4_real)
        self.assertEquals(edge_two_real_14[3].edge1, edge[3].edge1)
        self.assertEquals(edge_two_real_14[3].edge2, edge[3].edge2)

        # Case 2 - Both edges each connect to one real node and one fake node. Both real nodes are different
        edge = data_handler.connect_edges(edge_left_real_13, edge_right_real_24)
        self.assertEquals(edge_two_real_14[3].edge1, edge[3].edge1)
        self.assertEquals(edge_two_real_14[3].edge2, edge[3].edge2)

        # Case 3 - Both edges connect to the same real node. Both edge's other node is  different fake one
        edge = data_handler.connect_edges(edge_left_real_13, edge_left_real_12)
        mock_connect.assert_called_with(self.node_1_real, self.node_3_unreal)
        self.assertEquals(edge_left_real_13[3].edge1, edge[3].edge1)
        self.assertEquals(edge_left_real_13[3].edge2, edge[3].edge2)

        # Case 4 - One edge is connected to a real node and to a fake node. Other edge connects to two fake nodes.
        edge = data_handler.connect_edges(edge_left_real_12, edge_two_unreal_23)
        mock_connect.assert_called_with(self.node_1_real, self.node_3_unreal)
        self.assertEquals(edge_left_real_13[3].edge1, edge[3].edge1)
        self.assertEquals(edge_left_real_13[3].edge2, edge[3].edge2)

        # Case 5 - Both edge have two fake nodes.
        edge = data_handler.connect_edges(edge_two_unreal_13, edge_two_unreal_23)
        mock_connect.assert_called_with(self.node_1_unreal, self.node_3_unreal)
        self.assertEquals(edge_two_unreal_13[3].edge1, edge[3].edge1)
        self.assertEquals(edge_two_unreal_13[3].edge2, edge[3].edge2)

    def test_data_collection(self):
        # WIP
        return
        # Assemble
        new_graph = create_rand_graph("../graph_config.txt")
        gamer = GameDataHandler("../graph_config.txt")

        nodes_list = []
        edges = []

        def add_empty_edge(self, graph, nodes_list, edges_list):
            for node in graph.node_list:
                if node not in nodes_list:
                    for friend in node.neighbors:
                        if friend in [item.serial_num for item in nodes_list]:
                            tmp_node = graph.get_node_by_serial(friend)
                            fake_node_1 = NodeObject(serial=None, location={'x': node.x, 'y': node.y},
                                                     size=node.size, real=False)
                            fake_node_2 = NodeObject(serial=None, location={'x': tmp_node.x, 'y': tmp_node.y},
                                                     size=tmp_node.size, real=False)
                            edges_list.append((fake_node_1, fake_node_2))
                            return

        for i in range(3):
            nodes_list.append(new_graph.node_list[i])
        # Add an extra node that is connected to one of the existing ones

        for node in nodes_list[0].neighbors:
            if node not in nodes_list:
                nodes_list.append(new_graph.get_node_by_serial(node))
                break
        for node in nodes_list:
            for friend in node.neighbors:
                if friend in [item.serial_num for item in nodes_list]:
                    edges.append((node, new_graph.get_node_by_serial(friend)))
                else:
                    origin_node = new_graph.get_node_by_serial(friend)
                    fake_node = NodeObject(serial=None, location={'x': origin_node.x, 'y': origin_node.y},
                                           size=origin_node.size, real=False)
                    edges.append((node, fake_node))

        # clean nodes
        for node in nodes_list:
            node.neighbors = set()
            node.possible_neighbors = set()

        # Add a few empty edges
        add_empty_edge(new_graph, nodes_list, edges)
        add_empty_edge(new_graph, nodes_list, edges)
        add_empty_edge(new_graph, nodes_list, edges)

        mock_reader.return_value = {'nodes': nodes_list, 'edges': edges}

        # act
        gamer.do_move()
        time.sleep(1)

    @patch('SupplementaryFiles.GameDataHandler.Utils')
    def test_trim_data(self, mock_utils):
        mock_utils.graph_config_data = None
        mock_utils.game_config_data = {'Default': {'log_level': 'ERROR'}}
        Utils.read_game_config_file(path.join("..", CONFIG_FILE_PATH))
        Utils.read_graph_config_file(path.join("..", GRAPH_CONFIG_PATH))
        data_handler = GameDataHandler(path.join("../", "graph_config.txt"), None)
        data_handler.graph.add_node(self.node_1_real.x, self.node_1_real.y, serial=self.node_1_real.serial_num)
        data_handler.graph.add_node(self.node_2_unreal.x, self.node_2_unreal.y, serial=self.node_2_unreal.serial_num)
        data_handler.graph.add_node(self.node_2_unreal_moved.x, self.node_2_unreal_moved.y, serial=self.node_2_unreal_moved.serial_num)
        data_handler.graph.add_node(self.node_3_unreal.x, self.node_3_unreal.y, serial=self.node_3_unreal.serial_num)
        data_handler.graph.add_node(self.node_3_unreal_moved.x, self.node_3_unreal_moved.y, serial=self.node_3_unreal_moved.serial_num)
        data_handler.graph.add_node(self.node_4_real.x, self.node_4_real.y, serial=self.node_4_real.serial_num)
        edge_1 = (self.node_1_real, self.node_2_unreal_moved, 1,
                  LineEquation(slope=1, const=0, edge1=self.node_1_real, edge2=self.node_2_unreal_moved))
        edge_2 = (self.node_2_unreal, self.node_3_unreal_moved, 1,
                  LineEquation(slope=1, const=0, edge1=self.node_2_unreal, edge2=self.node_3_unreal_moved))
        edge_3 = (self.node_3_unreal, self.node_4_real, 1,
                  LineEquation(slope=1, const=0, edge1=self.node_3_unreal, edge2=self.node_4_real))
        edge_4 = (self.node_1_real, self.node_4_real, 1,
                  LineEquation(slope=1, const=0, edge1=self.node_1_real, edge2=self.node_4_real))
        data_handler.extra_edges = [edge_1, edge_2, edge_3]

        data_handler.trim_data()
        self.assertEquals(len(data_handler.edges_to_add), 1)
        self.assertEquals(data_handler.edges_to_add[0][0].serial_num, edge_4[0].serial_num)
        self.assertEquals(data_handler.edges_to_add[0][1].serial_num, edge_4[1].serial_num)
