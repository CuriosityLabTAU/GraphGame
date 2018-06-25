#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    f = open('/sdcard/graphgamemain/main_6.txt', 'w')
except:
    f = open('main.txt', 'w')
f.write('1\n')
f.close()

import kivy
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
from KivyFiles.GraphDisplay import GraphDisplay
g = open('ResultsDisplay.txt', 'w')
g.write('1\n')
from kivy.graphics import Color, Rectangle
g.write('2\n')

from KivyCommunication import *
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')



def translate_answers(answers_list):
    try:

        int(str(answers_list[0]))

        return str(answers_list[0])
    except (TypeError, ValueError) as e:
        store = JsonStore("Json/questions.json", encoding='utf-8')
        translated_list = [store['questionnaire']['get_answers'][str(answer)][::-1] for answer in answers_list]
    if (len(answers_list)) == 1:

        return str(translated_list[0])
    else:

        return str(', '.join(translated_list))

class ResultDisplay:
    """
        This object lies between the screen and the widget. It is used as a buffer between the two.
    """
    parent_screen = None

    def __init__(self, parent_screen=None):
        self.parent_screen = parent_screen
        self.the_widget = ResultWidget(self, self.parent_screen.main_app)

    def load(self):
        self.the_widget.on_enter()



class ResultWidget(GridLayout):
    question_list = None
    main_app = None
    parent_app = None
    score_label_height = 50
    submit_button_height = 50
    graph_spacing = 50
    graph_title_size = 30
    res = None

    def __init__(self, parent_app, main_app):
        # The result window is split to 3 parts - information, scoreboard and button
        super(ResultWidget, self).__init__(rows=3, cols=1)

        self.parent_app = parent_app
        self.main_app = main_app

    def on_enter(self):
        col_width = kivy.core.window.Window.size[0] / 2
        height_spacing = self.score_label_height + self.submit_button_height + self.graph_spacing + \
                         (2 * self.graph_title_size)
        height = (kivy.core.window.Window.size[1] - height_spacing) / 2

        # First part of the result screen is split in two - questions and graphs
        layout = GridLayout(rows=len(self.main_app.user_answers) * 2, cols=3)
        # !/usr/bin/python
        # -*- coding: utf-8 -*-
        layout.add_widget(self.get_question_result_grid(user_answers=self.main_app.user_answers, width=col_width))
        layout.add_widget(MyLabel(size_hint_x=0.0005))
        store = JsonStore("Json/answers.json", encoding='utf-8')
        map_grid = GridLayout(rows=7, cols=1)
        map_grid.add_widget(Label(text=store['answers']['graphs_types']['discovered_graph'][::-1],font_name="fonts/Alef-Regular.ttf",
            halign='right', size_hint_y=None, height=self.graph_title_size))

        map_grid.add_widget(MyLabel(size_hint_y=0.002))


        graph_discovered = GraphDisplay(graph=self.main_app.discovered_graph,font_name="fonts/Alef-Regular.ttf",
            halign='right', dim=(col_width, height))
        map_grid.add_widget(graph_discovered)

        map_grid.add_widget(Label(text=store['answers']['graphs_types']['real_graph'][::-1],font_name="fonts/Alef-Regular.ttf",
            halign='right', size_hint_y=None, height=self.graph_title_size))

        map_grid.add_widget(MyLabel(size_hint_y=0.002))


        graph_true = GraphDisplay(graph=self.main_app.current_graph,
                                  dim=(col_width, height))
        map_grid.add_widget(graph_true)

        map_grid.add_widget(MyLabel(size_hint_y=0.002))
        layout.add_widget(map_grid)
        self.add_widget(layout)
        self.res = self.calculate_percentage(self.main_app.user_answers)
        self.add_widget(Label(text=" {}%;".format(self.res['user_score'])+store['answers']['scores']['subject_score'][::-1]+" {}%;".format(self.res['possible_score'])+ store['answers']['scores']['discovered_graph_score'][::-1]+" {}%"
                              .format(self.game_grade(self.main_app.discovered_graph,
                                                      self.main_app.current_graph))+ store['answers']['scores']['nodes_discovered'][::-1],
                              size_hint_y=None, height=self.score_label_height, font_name="fonts/Alef-Regular.ttf", halign='right'))

        self.submit_button = Button(text=store['answers']['next_button'][::-1], size_hint_y=None,font_name="fonts/Alef-Regular.ttf", halign='right', height=self.submit_button_height)
        self.submit_button.bind(on_press=self.stop_me)
        self.add_widget(self.submit_button)

        self.log_answers()

    def log_answers(self):
        graph_number = self.main_app.sm.screen_names.index(self.main_app.sm.current)
        game_number = self.main_app.sm.screens[graph_number].game_number
        for ua in self.main_app.user_answers:
            ua_str = "question_id=%d;" % ua.question_id
            ua_str += "real_answer=%s;" % str(ua.real_answer)
            ua_str += "user_answer=%s;" % str(ua.user_answer)
            ua_str += "user_graph_answer=%s;" % str(ua.user_graph_answer)
            KL.log.insert(action=LogAction.data,
                          obj="game_%d_graph_%d_user_answers" % (game_number, graph_number),
                          comment=ua_str)
        percentage_str = str(self.res)
        KL.log.insert(action=LogAction.data,
                      obj="game_%d_graph_%d_percentage" % (game_number, graph_number),
                      comment=percentage_str, sync=True)

    def stop_me(self, instance):
        self.parent_app.parent_screen.end_results()

    @staticmethod
    def get_question_result_grid(user_answers, width):
        """
        Here we create the question grid.
        Each question has the question itself and the three categories of answers:
        The answers the user gave
        The answers the user would have given if they had a perfect memory
        The true answer in the graph.
        """
        user_answers = user_answers
        question_result_grid = GridLayout(rows=len(user_answers))
        store = JsonStore("Json/answers.json", encoding='utf-8')
        for item in user_answers:
            new_question = GridLayout(rows=4, cols=1)
            new_question.add_widget(Label(text=item.question_string, text_size=(width, None), font_name="fonts/Alef-Regular.ttf", halign='right'))

            keys = GridLayout(rows=1, cols=3)
            keys.add_widget(Label(text=store['answers']['answer_graph_type']['user_answer'][::-1], font_name="fonts/Alef-Regular.ttf", halign='right'))
            keys.add_widget(Label(text=store['answers']['answer_graph_type']['discovered_graph_answer'][::-1], font_name="fonts/Alef-Regular.ttf",halign='right'))
            keys.add_widget(Label(text=store['answers']['answer_graph_type']['full_graph_answer'][::-1], font_name="fonts/Alef-Regular.ttf",halign='right'))
            new_question.add_widget(keys)

            answers = GridLayout(rows=1, cols=3)
            answers.add_widget(Label(text=translate_answers(item.user_answer),font_name="fonts/Alef-Regular.ttf", halign='right'))
            answers.add_widget(Label(text=translate_answers(item.user_graph_answer), font_name="fonts/Alef-Regular.ttf", halign='right'))
            answers.add_widget(Label(text=translate_answers(item.real_answer), font_name="fonts/Alef-Regular.ttf", halign='right'))

            new_question.add_widget(answers)
            new_question.add_widget(MyLabel(size_hint_y=0.005))

            KL.log.insert(action=LogAction.data, comment='results_question_%s_user_%s_discovered_%s_true_%s' % (
                item.question_string, str(item.user_answer), str(item.user_graph_answer), str(item.real_answer)))

            question_result_grid.add_widget(new_question)

        return question_result_grid

    @staticmethod
    def calculate_percentage(user_answers):
        """
        Calculate the score of the user and the user's graph as compared to the truth.
        :param user_answers:
        :return:
        """
        answer_list = user_answers
        user_answers_percentage = 0 #number of questions in each graph
        user_graph_answer_percentage = 0 #number of questions in each graph
        possible_answers = ['red', 'yellow', 'blue']
        for answer in answer_list:
            # print ("user_answer {0},user_graph_answer {1},real_answer {2} ".format(answer.user_answer,answer.user_graph_answer,answer.real_answer)) # DEBUG
            #Goren - the new grade calculation
            if answer.question_id == 1:
                if answer.user_graph_answer == answer.real_answer:
                    user_graph_answer_percentage = user_graph_answer_percentage + 1
                if answer.user_answer == answer.user_graph_answer:
                    user_answers_percentage = user_answers_percentage + 1
            else:
                for ans in possible_answers:
                    if ans in answer.user_graph_answer and ans in answer.real_answer:
                        user_graph_answer_percentage = user_graph_answer_percentage + 1

                    if ans not in answer.user_graph_answer and ans not in answer.real_answer:
                        user_graph_answer_percentage = user_graph_answer_percentage + 1

                for ans in possible_answers:
                    if ans in answer.user_answer and ans in answer.user_graph_answer:
                        user_answers_percentage = user_answers_percentage + 1
                    if ans not in answer.user_answer and ans not in answer.user_graph_answer:
                        user_answers_percentage = user_answers_percentage + 1

        # print(user_answers_percentage)
        # print (user_graph_answer_percentage)
        num_of_questions = len(answer_list)
        num_of_questions = num_of_questions if num_of_questions != 0 else 1
        user_possible_success = round(user_answers_percentage * 100 / (float(num_of_questions)*3), 2)
        user_true_success = round(user_graph_answer_percentage * 100 / (float(num_of_questions)*3), 2)
        return {'possible_score': user_true_success, 'user_score': user_possible_success}

    @staticmethod
    def game_grade(user_seen_graph, real_graph):
        """
        Returns the final grade for the graph. Num nodes seen vs num nodes existing.
        """
        user_graph_num_of_nodes = len([item for item in user_seen_graph.node_list if item.is_real()])
        real_graph_num_of_nodes = len([item for item in real_graph.node_list if item.is_real()])
        return round(100 * float(user_graph_num_of_nodes) / float(real_graph_num_of_nodes), 2)

    def build(self):
        return self.meta_layout




class MyLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1, 1, 1, 0.7)
            Rectangle(pos=self.pos, size=self.size)