#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import path


class Utils:
    game_config_data = None
    graph_config_data = None
    image_folder = path.join("..", "Images")
    btn_1_img = 'button1.jpg'
    btn_2_img = 'button2.jpg'
    btn_3_img = 'button3.jpg'
    btn_4_img = 'button4.jpg'

    btn_1_img = 'button1.jpg'
    btn_2_img = 'button2.jpg'
    btn_3_img = 'button3.jpg'
    btn_4_img = 'button4.jpg'

    @staticmethod
    def read_game_config_file(config_path):
        my_config = Utils.read_file(config_path)
        Utils.game_config_data = my_config
        Utils.image_folder = Utils.game_config_data['Default']['image_folder']
        return my_config

    @staticmethod
    def read_graph_config_file(config_path):
        my_config = Utils.read_file(config_path)
        Utils.graph_config_data = my_config
        return my_config

    @staticmethod
    def read_file(config_path):
        config_dict = {}
        with open(config_path, 'r') as f:
            for line in f:
                new_line = Utils.parse_line(line)
                key = new_line.keys()
                if not key[0] in config_dict:
                    config_dict[key[0]] = {}
                inner_key = new_line[key[0]].keys()
                config_dict[key[0]][inner_key[0]] = new_line[key[0]][inner_key[0]].rstrip()
        return config_dict

    @staticmethod
    def parse_line(line):
        point_index = line.find(".")
        equal_index = line.find("=")
        new_dict = {}
        new_dict[line[:point_index]] = {}
        new_dict[line[:point_index]][line[point_index+1:equal_index]] = line[equal_index+1:]
        return new_dict

    @staticmethod
    def max_nodes_per_size(size):
        max_nodes = 0
        return max_nodes

    @staticmethod
    def get_enum_items(enum_object):
        list = enum_object.__dict__.keys()
        list.remove("__doc__")
        list.remove("__module__")
        return list

    @staticmethod
    def format_log_msg(msg, **kwargs):
        new_message = msg
        for key, value in kwargs.iteritems():
            new_message = "{0}, {1}={2}".format(new_message, key, value)
        return new_message
