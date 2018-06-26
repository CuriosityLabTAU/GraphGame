#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import path, getcwd, listdir
from random import shuffle
from kivy.app import App
from LoginScreen import LoginScreen
from QuestionnaireScreen import QuestionnaireScreen
from ResultsScreen import ResultScreen
from GraphGameScreen import GraphGameScreen
from SupplementaryFiles.GraphSaveLoad import load_graph_from_json, save_graph_json
from SupplementaryFiles.Utils import Utils
from KivyFiles.Questions.QuestionObject import QuestionObject
from SupplementaryFiles.GLogger import *
from KivyCommunication import *
from SupplementaryFiles.Enums import Colours, QuestionTypes
from kivy.logger import Logger
from kivy.uix.screenmanager import ScreenManager, Screen


CONFIG_FILE_PATH = "game_config.txt"
GRAPH_CONFIG_PATH = "graph_config.txt"
GET_RANDOM_QUESTIONS = 1

class ZeroScreen(Screen):

    def on_enter(self, *args):
        KL.restart()

    def start(self):
        self.ids['subject_id'].bind(text=self.ids['subject_id'].on_text_change)


class GraphGameMainApp(App):

    game_screen = []
    filename = 'network_new.json'

    # Variables that allow passing information between screens
    current_graph = None  # The graph the user is currently playing
    discovered_graph = None  # The graph discovered by the user in the current pipethrough
    user_answers = []
    question_list = []
    button_presses = []
    real_user = True
    user_id = None
    logger = None

    def build(self):
        self.init_communication()

        self.config = Utils.read_game_config_file(CONFIG_FILE_PATH)
        Utils.read_graph_config_file(GRAPH_CONFIG_PATH)
        self.logger = GLogger(self.config['Default']['logger_output_type'], self.config['Default']['logger_writing_location'],self.config['Default']['log_level'], self.user_data_dir)
        #self.init_communication(self.config['Cloud']['server_ip'])
        graph_config_path = self.config['Default']['graph_config_path']
        self.sm = ScreenManager()

        screen = ZeroScreen()
        screen.start()
        screen.ids['subject_id'].bind(text=screen.ids['subject_id'].on_text_change)
        self.sm.add_widget(screen)

        # # Setting up the login screen separately
        # login_screen = LoginScreen(name='LoginScreen')
        # login_screen.setup(main_app=self)
        # login_screen.add_widget(login_screen.display.layout)
        # self.sm.add_widget(login_screen)

        graph_list = self.load_graphs_from_folder()

        self.current_graph = None
        self.discovered_graph = None
        self.user_answers = []
        self.question_list = []
        self.button_presses = []
        # Enumerate over all the graphs in the folder
        for i_net, graph_data in enumerate(graph_list):
            # Step 1 - Graph Game
            self.question_list = graph_data.question_object_list
            self.game_screen.append(GraphGameScreen(name='game_graph_' + str(i_net)))
            self.game_screen[-1].setup(number=i_net,
                                       main_app=self,
                                       max_turns=int(self.config['Default']['max_turns']),
                                       real_user=True,
                                       graph=graph_data,
                                       graph_config=graph_config_path,
                                       button_presses=self.button_presses)
            self.game_screen[-1].add_widget(self.game_screen[-1].graph_game.layout)
            # Step 2 - Questionnaire
            #Goren - run nine graphs with question and then one without
            if i_net <9:
                self.game_screen.append(QuestionnaireScreen(name='game_questionnaire_' + str(i_net)))
                self.game_screen[-1].setup(number=i_net,
                                           main_app=self,
                                           real_user=self.real_user)
                self.game_screen[-1].add_widget(self.game_screen[-1].questionnaire.the_widget)
                # Step 3 - Results
                self.game_screen.append(ResultScreen(name='game_results_' + str(i_net)))
                self.game_screen[-1].setup(number=i_net,
                                           main_app=self,
                                           real_user=True)
                self.game_screen[-1].add_widget(self.game_screen[-1].result_app.the_widget)
        Logger.debug("7")

        for gs in self.game_screen:
            self.sm.add_widget(gs)

        self.sm.current = 'zero_screen'
        return self.sm

    def init_communication(self):
        KC.start(the_ip='192.168.1.254', the_parents=[self])  # 127.0.0.1
        KL.start(mode=[DataMode.file], pathname=self.user_data_dir)

    @staticmethod
    def on_connection():
        GLogger.log(logging.INFO,"", action=LogAction.data, obj='GraphGameApp', comment='start')

    def press_start(self):
        self.sm.current = 'game_graph_0'

    def load_graphs_from_folder(self):
        graph_list = []
        # Goren - notice the path to the graph defined by graphs_folder in the config file. is this where your graphs are?
        graph_folder = path.join(getcwd(), self.config['Default']['graphs_folder'])
        #for testing
        #graph_folder = path.join(getcwd(), self.config['Default']['tester_graphs_folder'])
        file_list = [item for item in listdir(graph_folder) if item.endswith(".json")]
        for graph_name in file_list:
            try:
                graph_file_path = path.join(".", graph_folder, str(graph_name))
                if GET_RANDOM_QUESTIONS:
                    self.add_random_questions(5,graph_file_path)
                current_graph = load_graph_from_json(graph_file_path)
                graph_list.append(current_graph)
            except Exception as e:
                print(e)
        #randomize
        shuffle(graph_list)
        return graph_list

    def add_random_questions (self,number_of_random_questios, graph_file_path):
        current_graph = load_graph_from_json(graph_file_path)
        store = JsonStore("Json/questions.json", encoding='utf-8')
        question_one_red = QuestionObject(store['questionnaire']['ques']['q01'][::-1].replace("X", store['questionnaire']['ques_parameters']['X_red'][::-1]),
                                      QuestionTypes['NUMBER'], 1, Colours['red'])
        question_one_blue = QuestionObject(store['questionnaire']['ques']['q01'][::-1].replace("X", store['questionnaire']['ques_parameters']['X_blue'][::-1]),
                                      QuestionTypes['NUMBER'], 1, Colours['blue'])
        question_one_yellow = QuestionObject(store['questionnaire']['ques']['q01'][::-1].replace("X", store['questionnaire']['ques_parameters']['X_yellow'][::-1]),
                                      QuestionTypes['NUMBER'], 1, Colours['yellow'])
        question_two = QuestionObject(store['questionnaire']['ques']['q03'][::-1],
                                      QuestionTypes['MULTIPLE_CHOICE'], 3)
        question_three = QuestionObject(store['questionnaire']['ques']['q06'][::-1],
                                        QuestionTypes['MULTIPLE_CHOICE'], 6)
        question_six = QuestionObject(store['questionnaire']['ques']['q16'][::-1],
                                      QuestionTypes['MULTIPLE_CHOICE'], 16)
        question_seven = QuestionObject(store['questionnaire']['ques']['q17'][::-1],
                                        QuestionTypes['MULTIPLE_CHOICE'], 17)
        q_nums = range (5)
        shuffle(q_nums)
        all_questions_graph = []
        for i in range(number_of_random_questios):
            if q_nums[i] == 0:
                q1_list = [question_one_red, question_one_blue, question_one_yellow]
                shuffle(q1_list)
                all_questions_graph.append(q1_list[0])
            elif q_nums[i] == 1:
                all_questions_graph.append(question_two)
            elif q_nums[i] == 2:
                all_questions_graph.append(question_three)
            elif q_nums[i] == 3:
                all_questions_graph.append(question_six)
            elif q_nums[i] == 4:
                all_questions_graph.append(question_seven)

        current_graph.question_object_list = all_questions_graph
        save_graph_json(current_graph, graph_file_path)

if __name__ == '__main__':
    GraphGameMainApp().run()

