import unittest

from SupplementaryFiles.GraphObj import GraphObject


class TestGraph(unittest.TestCase):

    def test_create_graph(self):
        # Arrange
        max_neighbors = 5
        extra_distance = 1
        # Act
        new_graph = GraphObject(max_x=1000, max_y=1000, node_count=20, max_neighbors=max_neighbors, extra_distance=extra_distance)
        # Assert
        assert (new_graph.node_list == [])
        assert (new_graph.extra_distance == extra_distance)
        assert (new_graph.max_neighbors == max_neighbors)

    def test_add_node(self):
        # Arrange
        x_coor = 50
        y_coor = 50
        size = 4
        new_graph = GraphObject(max_x=1000, max_y=1000, node_count=20, max_neighbors=5,
                                extra_distance=10)

        # Act
        new_graph.add_node(x_coor, y_coor, node_size=size)

        # Assert
        self.assertEqual(new_graph.node_list[0].x,x_coor)
        self.assertEqual(new_graph.node_list[0].y,y_coor)
        self.assertEqual(new_graph.node_list[0].size,size)

    def test_get_possible_connections(self):
        # Arrange
        new_graph = GraphObject(max_x=1000, max_y=1000, node_count=20, max_neighbors=5,
                                extra_distance=10)

        # Act
        serial1 = new_graph.add_node(50, 50).serial_num
        serial2 = new_graph.add_node(50, 100).serial_num
        serial3 = new_graph.add_node(50, 200).serial_num
        list = new_graph.get_possible_connections(serial1)

        # Assert
        self.assertTrue(list.__contains__(serial2))
        self.assertFalse(list.__contains__(serial3))

    def test_get_best_connection(self):
        # Arrange
        new_graph = GraphObject(max_x=1000, max_y=1000, node_count=20, max_neighbors=5,
                                extra_distance=10)
        serial_1 = new_graph.add_node(50, 50).serial_num
        serial_2 = new_graph.add_node(50, 100).serial_num
        serial_3 = new_graph.add_node(50, 200).serial_num

        # Act
        connection_list = new_graph.get_possible_connections(serial_1)
        best_connection_id = new_graph.get_best_connection(new_graph.get_node_by_serial(serial_1), connection_list)

        # Assert
        self.assertEqual(best_connection_id, serial_2)

    def test_get_node_by_serial(self):
        # Arrange
        new_graph = GraphObject(max_x=1000, max_y=1000, node_count=20, max_neighbors=5,
                                extra_distance=10)
        serial_1 = new_graph.add_node(50, 50).serial_num
        serial_2 = new_graph.add_node(50, 100).serial_num
        serial_3 = new_graph.add_node(50, 200).serial_num

        # Assert
        self.assertEqual(new_graph.get_node_by_serial(serial_1).y, 50)
        self.assertEqual(new_graph.get_node_by_serial(serial_2).y, 100)
        self.assertEqual(new_graph.get_node_by_serial(serial_3).y, 200)

    def test_is_node_far_enough(self):
        # Arrange
        new_graph = GraphObject(max_x=1000, max_y=1000, node_count=20, max_neighbors=5,
                                extra_distance=10)
        new_graph.add_node(50, 50)
        new_graph.add_node(50, 100)
        new_graph.add_node(50, 200)
        serial = new_graph.node_list[0].serial_num
        serial2 = new_graph.node_list[1].serial_num
        serial3 = new_graph.node_list[2].serial_num

        # Act

        # Assert
        self.assertFalse(new_graph.is_node_far_enough(new_graph.node_list[1], new_graph.node_list[0], new_graph.node_list[2]))
        self.assertTrue(new_graph.is_node_far_enough(new_graph.node_list[0], new_graph.node_list[1], new_graph.node_list[2]))

