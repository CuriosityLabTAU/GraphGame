#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.graphics import Line
from kivy.uix.widget import Widget
from kivy.animation import Animation


class KivyEdge(Widget):
    node1 = None
    node2 = None
    line = None
    slope = None

    def __init__(self, node1, node2, width, **kwargs):
        super(KivyEdge, self).__init__(**kwargs)
        self.line_width = width
        if node1.get_x() < node2.get_x():
            self.node1 = node1
            self.node2 = node2
        else:
            self.node1 = node2
            self.node2 = node1

        with self.canvas:
            self.line = Line(points=[self.node1.get_x(), self.node1.get_y(), self.node2.get_x(), self.node2.get_y()],
                             width=self.line_width)

    def reset_edge(self, animated):
        """
        move the edge so it is drawn between its nodes
        :param animated: boolean indicating whether to show the movement of the edge
        """
        if animated:
            anim = Animation(points=[self.node1.get_x(), self.node1.get_y(), self.node2.get_x(), self.node2.get_y()])
            anim.start(self.line)
        else:
            self.line.points = [self.node1.get_x(), self.node1.get_y(), self.node2.get_x(), self.node2.get_y()]

    def set_slope(self, line_equation):
        self.slope = line_equation.slope

    def __repr__(self):
        return 'KivyEdge({}, {})'.format(self.node1, self.node2)

    def print_by_serial(self):
        return 'KivyEdge({}, {})'.format(self.node1.serial, self.node2.serial)
