import logging
from random import random, randint

from os import path

from SupplementaryFiles.GameDataHandler import GameDataHandler
from SupplementaryFiles.LoadGraph import load_py_graph
from SupplementaryFiles.Utils import Utils
from KivyFiles.GraphTabletDisplay import GraphTabletDisplay

# https://gist.github.com/kastnerkyle/d127197dcfdd8fb888c2

CURIOSITY_VALUE = 1  # 1 = random. 0.1 ~ about right for learning
GAMMA = 0.8
ALPHA = 0.1

CONFIG_FILE_PATH = path.join("..", "game_config.txt")
GRAPH_CONFIG_PATH = path.join("..", "graph_config.txt")

log = logging.getLogger()

consecutive_runs = 20


class QMatrix:
    moves_matrix = []

    action_space = 4
    first_step = 0  # The first step taken by the QMatrix, press button 1
    prev_step = 0  # The previous step taken by the matrix
    prev_known_nodes = 0  # The amount of nodes we have seen until before this step
    nodes_in_graph = 10
    max_steps = 0

    def __init__(self, action_space, max_steps, nodes_in_graph):
        self.action_space = action_space
        self.max_steps = max_steps
        self.nodes_in_graph = nodes_in_graph
        self.reinit()
        self.moves_matrix = []
        for i in range(4):
            self.moves_matrix.append([])
            for _ in range(4):
                self.moves_matrix[i].append(0)

    def reinit(self, known_nodes=0):
        self.prev_step = 0
        self.prev_known_nodes = known_nodes

    def init_q_array(self):
        pass

    def init_record_array(self):
        pass

    def max_args(self):
        """
        looks at the matrix. chooses option with highest percentage
        """
        return self.moves_matrix[self.prev_step].index(max(self.moves_matrix[self.prev_step]))

    def choose_action_epsilon_greedy(self):
        if random() < CURIOSITY_VALUE:
            return randint(1, self.action_space) - 1
        else:
            return self.max_args()
        # Maybe not use greedy??

    def update_matrix(self, num_nodes, current_step):
        """

        :param num_nodes:
        :param current_step:
        :return:
        """

        improvement_score = self.get_reword_score(num_nodes, self.nodes_in_graph, calc_type=2)
        qsa = self.moves_matrix[self.prev_step][current_step]
        # = qsa + ALPHA * (rsa + GAMMA * max(self.moves_arr[current_step][:]) - qsa)
        new_q = qsa + ALPHA * (improvement_score + GAMMA * max(self.moves_matrix[current_step][:]) - qsa)
        self.moves_matrix[self.prev_step][current_step] = new_q

        self.prev_step = current_step
        return 100*float(num_nodes)/float(self.nodes_in_graph)

    def get_reword_score(self, current_known_nodes, nodes_in_full_graph, calc_type=1):
        if calc_type == 1:
            return float(current_known_nodes) / float(nodes_in_full_graph)
        elif calc_type == 2:
            diff_nodes = current_known_nodes - self.prev_known_nodes
            self.prev_known_nodes = current_known_nodes
            return diff_nodes


class QPlayer:
    auto_first_press = 0  # the first button press is predetermined

    def __init__(self):
        pass

    def run_q_player(self, graph_file_path, log_file_path):
        Utils.read_game_config_file(CONFIG_FILE_PATH)
        Utils.read_graph_config_file(GRAPH_CONFIG_PATH)
        Utils.image_folder = path.join("..", Utils.image_folder)

        log.setLevel(Utils.game_config_data['Default']['log_level'])
        session_length = 1000

        graph = load_py_graph(graph_file_path)
        q_matrix = QMatrix(action_space=4, max_steps=int(Utils.game_config_data['Default']['max_turns']), nodes_in_graph=len(graph.node_list))

        with open(log_file_path,'w') as f:
            f.write("episode, score\n")
            for i in range(session_length):
                dummy_screen = DummyScreen(graph)
                game = GraphTabletDisplay(dummy_screen)
                data_handler = GameDataHandler(GRAPH_CONFIG_PATH, graph.size)
                data_handler.add_view_to_db(game.get_info_from_screen())

                rw = 0
                game.press_button(self.auto_first_press + 1)
                data_handler.add_view_to_db(game.get_info_from_screen())
                q_matrix.reinit(known_nodes=len(data_handler.get_real_nodes()))
                for j in range(1, int(Utils.game_config_data['Default']['max_turns'])):
                    log.debug("doing a step {}/{}".format(j, Utils.game_config_data['Default']['max_turns']))
                    btn = q_matrix.choose_action_epsilon_greedy()
                    game.press_button(btn + 1)
                    data_handler.add_view_to_db(game.get_info_from_screen())
                    rw = q_matrix.update_matrix(num_nodes=len(data_handler.get_real_nodes()), current_step=btn)
                log.info("Q session {}:{} - reword:{}".format(i, session_length, rw))
                f.write("{},{}\n".format(i + 1, rw))


class DummyScreen:
    graph = None
    graph_config = GRAPH_CONFIG_PATH
    max_turns = 0
    button_presses = []
    button_ratio = 0.2

    def __init__(self, graph):
        self.graph = graph
        self.real_user = False
        self.max_turns = int(Utils.game_config_data['Default']['max_turns'])

    def end_graph(self):
        pass

    def end_game(self):
        print ("end game \n")


file_name = "Graph_1.xml"
graph_path = path.join("..", "GraphsData", file_name)
graph_path = "graph_1"
for run_index in range(19, consecutive_runs):
    run_log_file = "result_{}__{}__{}.csv".format(file_name[:-4], CURIOSITY_VALUE, run_index)
    player = QPlayer()
    player.run_q_player(graph_path, run_log_file)