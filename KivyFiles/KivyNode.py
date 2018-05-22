#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.graphics import Ellipse
from kivy.uix.widget import Widget
import math
from kivy.animation import Animation


class KivyNode(Widget):
    x_coor = 0
    y_coor = 0
    serial = -1
    colour = None
    neighbors = None

    def __init__(self, x_loc, y_loc, serial, node_size, radius, colour, **kwargs):
        super(KivyNode, self).__init__(**kwargs)
        self.node_size = node_size
        self.radius = radius/2.0
        self.bind(pos=self.redraw)
        self.bind(size=self.redraw)
        self.x_coor = x_loc
        self.y_coor = y_loc
        self.size = [self.node_size, self.node_size]
        self.pos = [self.x_coor - self.node_size / 2, self.y_coor - self.node_size / 2]
        self.serial = serial
        self.colour = colour
        self.neighbors = []
        self.original_location = (x_loc, y_loc)

    def redraw(self, *args):
        self.canvas.clear()
        with self.canvas:
            Ellipse(pos=self.pos, size=self.size)

    def __repr__(self):
        return 'KivyNode({}, {})'.format(self.x_coor, self.y_coor)

    def get_x(self):
        return self.x_coor

    def get_y(self):
        return self.y_coor

    def get_colour(self):
        return self.colour

    def get_radius(self):
        return self.radius

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def move_y(self, amount=40):
        """
        moves the node's y coordinate by 'amount'
        :param amount: optional. a distance to move the node's y_coor by
        """
        self.y_coor += amount
        self.pos = [self.x_coor - self.node_size / 2, self.y_coor - self.node_size / 2]

    def move_x(self, amount=40):
        """
        moves the node's x coordinate by 'amount'
        :param amount: optional. a distance to move the node's x_coor by
        """
        self.x_coor += amount
        self.pos = [self.x_coor - self.node_size / 2, self.y_coor - self.node_size / 2]

    def move_by_amount(self, delta_x, delta_y, animated):
        """
        :param delta_x: a distance to move the node's x_coor by
        :param delta_y: a distance to move the node's y_coor by
        :param animated: boolean, indicates whether the node's movement should be visually displayed
        """
        self.x_coor = self.x_coor + delta_x
        self.y_coor = self.y_coor + delta_y

        if animated:
            anim = Animation(x=(self.x_coor - self.node_size / 2), y=(self.y_coor - self.node_size / 2))
            anim.start(self)
        else:
            self.pos = [self.x_coor - self.node_size / 2, self.y_coor - self.node_size / 2]

    def relative_move(self, x_change, y_change):
        """
        changes the node's x_coor and y_coor coordinates so that they are now
        x_change*x_coor and y_change*y_coor respectively
        :param x_change: the relative change to the node's x_coor
        :param y_change: the relative change to the node's y_coor
        """
        self.x_coor = self.x_coor*x_change
        self.y_coor = self.y_coor*y_change
        self.pos = [self.x_coor - self.node_size / 2, self.y_coor - self.node_size / 2]

    def jump_to_location(self, new_x, new_y):
        """
        sets self's location to (new_x, new_y)
        :param new_x: new value for node's x_coor
        :param new_y: new value for node's y_coor
        """
        self.x_coor = new_x
        self.y_coor = new_y
        self.pos = [self.x_coor - self.node_size / 2, self.y_coor - self.node_size / 2]

    def get_neighbors(self):
        """
        :return: the list of neighbors associated with a given node
        """
        return self.neighbors

    def get_amount_of_neighbors(self):
        """
        :return: the number of neighbors of a given node
        """
        return len(self.neighbors)

    def get_distance_from_node(self, node):
        """
        :param node: KivyNode
        :return: the distance between self and node
        """
        if node is None:
            return -1
        x = math.fabs(node.x_coor - self.x_coor)
        y = math.fabs(node.y_coor - self.y_coor)
        dist = math.sqrt(x**2 + y**2)
        return dist

    def print_node(self):
        print "For node " + str(self.serial) + ", coordinates = ("+str(self.get_x()) + ","+str(self.get_y()) + \
              "), color = " + self.get_colour()
