#!/usr/bin/python
# -*- coding: utf-8 -*-
import itertools
import logging

from SupplementaryFiles.Utils import Utils
from SupplementaryFiles.GameDataHandler import GameDataHandler
from SupplementaryFiles.GraphSaveLoad import load_graph_from_json
from SupplementaryFiles.GLogger import *
from KivyFiles.GraphTabletDisplay import GraphTabletDisplay
from os import path, listdir
from kivy.core.window import Window
from GraphGeneration import HandmadeGraph
from SupplementaryFiles.GLogger import *

# get the full graph that seen
# get the number of node seen
# put 0 if the #of node seen < #nodes in the graph
MAIN_CONFIG_FILE_PATH = path.join("..", "game_config.txt")
GRAPH_CONFIG_FILE = path.join("..", "graph_config.txt")
SAVED_GRAPH_PATH = "../GraphsData"

graphs_names = ["Graph_1_transpose.json"]


def main():
    print ("sdsdsds")
    GLogger('file', 'graph_validator_logger.txt', 'ERROR')
    Window.size = (1920, 1090)

    Utils.read_game_config_file(MAIN_CONFIG_FILE_PATH)
    Utils.read_graph_config_file(GRAPH_CONFIG_FILE)
    Utils.image_folder = path.join("..", Utils.image_folder)

    max_turns = int(Utils.game_config_data['Default']['max_turns'])
    it = itertools.product('1234', repeat=max_turns)
    number_of_successful_runs = 0
    # use line 30 to test all the graphs in SAVED_GRAPH_PATH; use line 31 to only test the graphs specified in 'graphs_names'
    # for current_graph in [item for item in listdir(SAVED_GRAPH_PATH) if item.endswith(".xml")]:
    for current_graph in graphs_names:
        curr_path = path.join(SAVED_GRAPH_PATH, current_graph)
        graph = load_graph_from_json(curr_path)
        with open("{}_saved_steps.txt".format(curr_path[:-5]), 'w') as f:
            num_of_graph_nodes = len(graph.node_list)
            f.write("The graph contains {} nodes\n".format(str(num_of_graph_nodes)))
            while True:
                try:
                    buttons = it.next()
                except StopIteration:
                    break
                answer, number_of_nodes_seen = run_buttons_on_graph(graph, buttons)
                number_of_successful_runs += answer
                f.write("steps: {}, seen nodes: {} \n".format(str(buttons), str(number_of_nodes_seen)))

            f.write("number of successful runs = {0}\n".format(number_of_successful_runs))


class DummyScreen:
    graph = None
    graph_config = GRAPH_CONFIG_FILE
    max_turns = 0
    button_presses = []
    button_ratio = 0.2

    def __init__(self, graph):
        self.graph = graph
        self.real_user = False
        self.max_turns = int(Utils.game_config_data['Default']['max_turns'])

    def end_graph(self):
        self.graph_game.the_end = True
        if not self.graph_game.is_playing:
            pass

    def end_game(self):
        print ("end game \n")


def run_buttons_on_graph(graph, buttons):
    #log = logging.getLogger()
    #log.setLevel(Utils.game_config_data['Default']['log_level'])
    dummy_screen = DummyScreen(graph)
    game = GraphTabletDisplay(dummy_screen)
    #game.run()
    data_handler = GameDataHandler(GRAPH_CONFIG_FILE, graph.size)
    data_handler.add_view_to_db(game.get_info_from_screen())
    for i in range(len(buttons)): #int(Utils.game_config_data['Default']['max_turns'])):
        #log.debug("doing a step {}/{}".format(i, Utils.game_config_data['Default']['max_turns']))
        game.press_button(int(buttons[i]))
        data_handler.add_view_to_db(game.get_info_from_screen())

    # print ("known nodes-"+str(data_handler.get_number_of_known_nodes())+"\n")
    answer = (data_handler.get_number_of_known_nodes() == len(graph.node_list))
    return answer, data_handler.get_number_of_known_nodes()


if __name__ == "__main__":
    print ("y")
    main()
