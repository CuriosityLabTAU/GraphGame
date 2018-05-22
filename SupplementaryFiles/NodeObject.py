#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
from Point import Point
from SupplementaryFiles.Enums import Colours, Shapes


class NodeObject(Point):
    serial_num = None
    dummy_num=-1
    shape = Shapes['circle']
    size = 0
    neighbors = set()
    possible_neighbors = set()
    real = True
    colour = Colours['red']
    def __init__(self, serial, location, size, colour=Colours['red'], shape=Shapes['circle'], real=True, dummy_num=None):
        """

        :param serial:
        :param location: {'x':float, 'y':float}
        :param size:
        :param colour:
        :param shape:
        """
        super(NodeObject, self).__init__(location['x'], location['y'])
        self.serial_num = serial
        self.size = size
        self.colour = colour
        self.shape = shape
        self.neighbors = set()
        self.possible_neighbors = set()
        self.real = real
        self.dummy_num = dummy_num

    def get_num_neighbors(self):
        return len(self.neighbors)

    def distance_from_line(self, node_1, node_2):
        """
        If for some reason we davide by zero we return -1
        :param node_1: NodeObject
        :param node_2: NodeObject
        :return: distance between self and the line between the two points
        """
        # In case the two nodes are exactly horizontal or vertical to one another
        if node_2.y == node_1.y:
            if min(node_1.x, node_2.x) <= self.x <= max(node_1.x, node_2.x):
                distance = math.fabs(self.y - node_1.y)
            else:
                distance = min(self.distance(node_1), self.distance(node_2))
        elif node_2.x == node_1.x:
            if min(node_1.y, node_2.y) <= self.y <= max(node_1.y, node_2.y):
                distance = math.fabs(self.x - node_1.x)
            else:
                distance = min(self.distance(node_1), self.distance(node_2))
        # See https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
        else:
            y_part = math.fabs(node_2.y - node_1.y)
            x_part = math.fabs(node_2.x - node_1.x)

            dist_part1 = y_part * self.x
            dist_part2 = x_part * self.y
            distance = math.fabs(dist_part1
                                 - dist_part2
                                 + node_1.y * node_2.x
                                 - node_2.y * node_1.x)
            if math.sqrt(y_part ** 2 + x_part ** 2) == 0:
                raise Exception("Point-1 and Point-2 are the same!")
            distance /= math.sqrt(y_part**2 + x_part**2)
        return distance

    def is_real(self):
        return self.real
