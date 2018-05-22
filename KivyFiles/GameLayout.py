#!/usr/bin/python
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.9.1')

from SupplementaryFiles.Utils import *
from kivy.uix.gridlayout import GridLayout
from GraphButton import MultiButton, EndButton
from GraphLayout import GraphLayout
from kivy.uix.floatlayout import FloatLayout
from SupplementaryFiles.RepeatedTimer import RepeatedTimer
from kivy.uix.image import Image
from os import path


class GameLayout(FloatLayout):
    next_func = None
    rt = None

    def __init__(self, tablet_game=None, zoom_rate=0.7, edge_size=2, **kwargs):
        super(GameLayout, self).__init__(rows=1, cols=2, **kwargs)
        self.tablet_game = tablet_game
        self.move_counter = 0
        self.dim = {"min_x": 0, "min_y": 0, "max_x": kivy.core.window.Window.size[0],
                    "max_y": kivy.core.window.Window.size[1]}
        self.button_width = self.dim["max_x"] * self.tablet_game.game_screen.button_ratio
        self.buttons = []
        self.original_graph = self.tablet_game.original_graph
        self.dim["max_x"] -= self.button_width
        self.kivy_graph_in = GraphLayout(self.original_graph, self.dim, 1, edge_size)
        self.kivy_graph_out = GraphLayout(self.original_graph, self.dim, zoom_rate, edge_size)
        self.kivy_graph_in.pos = (self.button_width, 0)
        self.kivy_graph_out.pos = (self.button_width, 0)
        self.add_widget(self.kivy_graph_in)
        self.is_zoomed_out = False
        self.set_button_functions()
        self.button_layout = self.get_buttons()
        self.add_widget(self.button_layout)
        if self.tablet_game.game_screen.real_user:
            self.rt = RepeatedTimer(1, self.call_function)
        self.button_hider = self.get_button_hider()

    def set_button_functions(self):
        """
        This function is used in order to determine the functionality of the buttons
        """
        self.button1_func = [self.zoom_out, self.zoom_in]
        self.button2_func = [self.centralize_most_connected]
        self.button3_func = [self.centralize_closest_same_color]
        self.button4_func = [self.centralize_closest_neighbor_diff_color]

    def get_buttons(self):
        """
        Creates a GridLayout that holds GraphButton needed for the game. Each button should be
        initialized using a string representing an image to be displayed on the button, a list of functions that will be
        responsible for the button's functionality, the button's number and the current gameLayout (self).
        """
        layout = GridLayout(cols=1, col_default_width=self.button_width, col_force_default=True)
        button1 = MultiButton(img=path.join(Utils.image_folder, Utils.btn_1_img), funcs=self.button1_func,
                              button_num=1, game_layout=self)
        button1.name = 'button1'
        button2 = MultiButton(img=path.join(Utils.image_folder, Utils.btn_2_img), funcs=self.button2_func,
                              button_num=2, game_layout=self)
        button2.name = 'button2'
        button3 = MultiButton(img=path.join(Utils.image_folder, Utils.btn_3_img), funcs=self.button3_func,
                              button_num=3, game_layout=self)
        button3.name = 'button3'
        button4 = MultiButton(img=path.join(Utils.image_folder, Utils.btn_4_img), funcs=self.button4_func,
                              button_num=4, game_layout=self)
        button4.name = 'button4'
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        self.buttons.append(button1)
        self.buttons.append(button2)
        self.buttons.append(button3)
        self.buttons.append(button4)
        layout.pos = (0, 0)
        return layout

    def get_button_hider(self):
        """
        Creates a GridLayout that looks similar to the button layout but is invisible. This is used in order to
        'disable' the buttons after pressing (disallowing double press)
        """
        layout = GridLayout(cols=1, col_default_width=self.button_width, col_force_default=True)
        im1 = Image(source=path.join(Utils.image_folder, Utils.btn_1_img), allow_stretch=True, keep_ratio=False,
                    color=[0.8, 0.8, 0.8, 1])
        im2 = Image(source=path.join(Utils.image_folder, Utils.btn_2_img), allow_stretch=True, keep_ratio=False,
                    color=[0.8, 0.8, 0.8, 1])
        im3 = Image(source=path.join(Utils.image_folder, Utils.btn_3_img), allow_stretch=True, keep_ratio=False,
                    color=[0.8, 0.8, 0.8, 1])
        im4 = Image(source=path.join(Utils.image_folder, Utils.btn_4_img), allow_stretch=True, keep_ratio=False,
                    color=[0.8, 0.8, 0.8, 1])
        layout.add_widget(im1)
        layout.add_widget(im2)
        layout.add_widget(im3)
        layout.add_widget(im4)
        layout.pos = (0, 0)
        return layout

    def call_function(self):
        """
        Function checks if any button put a new argument in 'next_func' variable, if so said argument is called and
         variable is reset, otherwise all buttons are enabled
        """
        if self.next_func is not None:
            func = self.next_func
            self.next_func = None
            func()
            self.tablet_game.send_info_from_screen()
            self.move_counter += 1
            if self.move_counter == self.tablet_game.max_turns:
                # once all the moves are played, removes the buttons from the screen and creates a new button in order
                # to finish the game
                self.remove_widget(self.button_layout)
                self.remove_widget(self.button_hider)
                end_layout = GridLayout(cols=1, col_default_width=self.button_width, col_force_default=True)
                end_button = EndButton(self.end_game)
                end_layout.add_widget(end_button)
                self.add_widget(end_layout)
                end_layout.pos = (0, 0)
        else:
            self.enable_buttons()

    def disable_buttons(self):
        """
        function renders the buttons unpressable
        """
        self.add_widget(self.button_hider)
        for button in self.buttons:
                button.disabled = True

    def enable_buttons(self):
        """
        function renders the buttons pressable
        """
        for button in self.buttons:
            button.disabled = False
        self.remove_widget(self.button_hider)

    def end_game(self):
        """
        function should be called after all moves are done. finished current graph diaplay inorder to move to the
        question screen
        """
        self.rt.stop()
        self.tablet_game.end_game()

    # The following functions represent button functionality. Zoom in/out switched between the GraphLayouts, other
    # functions identified the current GraphLayout and calls its corresponding function
    def zoom_out(self):
        center_node = self.kivy_graph_out.kivy_graph.get_by_serial(self.kivy_graph_in.kivy_graph.center_node.serial)
        self.kivy_graph_out.kivy_graph.move_node_to_center(center_node, False)
        self.remove_widget(self.kivy_graph_in)
        self.add_widget(self.kivy_graph_out)
        self.is_zoomed_out = True
        self.remove_widget(self.button_layout)
        self.add_widget(self.button_layout)
        self.remove_widget(self.button_hider)
        self.add_widget(self.button_hider)

    def zoom_in(self):
        center_node = self.kivy_graph_in.kivy_graph.get_by_serial(self.kivy_graph_out.kivy_graph.center_node.serial)
        self.kivy_graph_in.kivy_graph.move_node_to_center(center_node, False)
        self.remove_widget(self.kivy_graph_out)
        self.add_widget(self.kivy_graph_in)
        self.is_zoomed_out = False
        self.remove_widget(self.button_layout)
        self.add_widget(self.button_layout)
        self.remove_widget(self.button_hider)
        self.add_widget(self.button_hider)

    def centralize_most_connected(self):
        if self.is_zoomed_out:
            self.kivy_graph_out.kivy_graph.centralize_most_connected()
        else:
            self.kivy_graph_in.kivy_graph.centralize_most_connected()

    def centralize_closest_same_color(self):
        if self.is_zoomed_out:
            self.kivy_graph_out.kivy_graph.centralize_closest_same_color()
        else:
            self.kivy_graph_in.kivy_graph.centralize_closest_same_color()

    def centralize_closest_neighbor_diff_color(self):
        if self.is_zoomed_out:
            self.kivy_graph_out.kivy_graph.centralize_closest_neighbor_diff_color()
        else:
            self.kivy_graph_in.kivy_graph.centralize_closest_neighbor_diff_color()
