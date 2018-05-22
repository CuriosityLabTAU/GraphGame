import unittest

from SupplementaryFiles.NodeObject import NodeObject


class TestNode(unittest.TestCase):

    def test_distance_between_nodes(self):
        node1 = NodeObject(serial=1, location={'x': 1, 'y': 3}, size=1)
        node2 = NodeObject(serial=2, location={'x': 5, 'y': 6}, size=1)
        actual_distance = 5
        assert node1.distance(node2) == actual_distance

    def test_distance_from_line(self):
        # Arrange
        node1 = NodeObject(serial=1, location={'x': 1, 'y': 5}, size=1)
        node2 = NodeObject(serial=2, location={'x': 8, 'y': 7}, size=1)
        node_far = NodeObject(serial=3, location={'x': 4, 'y': 3}, size=1)
        node_close = NodeObject(serial=4, location={'x': 5, 'y': 7}, size=1)
        max_error = 0.001
        far_result = 2.7472112789737806
        close_result = 0.8241633836921342

        # Act
        far_distance = node_far.distance_from_line(node1, node2)
        close_distance = node_close.distance_from_line(node1, node2)

        # Assert
        assert far_distance < far_result + max_error or far_distance > far_result - max_error
        assert close_distance < close_result + max_error or close_distance > close_result - max_error
