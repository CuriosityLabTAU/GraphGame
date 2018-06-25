#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    f = open('/sdcard/graphgamemain/main_5.txt', 'w')
except:
    f = open('main.txt', 'w')
f.write('1\n')
f.close()

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from KivyFiles.Questions.AnswerObject import AnswerObject
from KivyFiles.Questions.QuestionWidgets import MultipleAnswersObj, IntSpinner, BooleanQuestion
from SupplementaryFiles.Enums import QuestionTypes
from kivy.logger import Logger
from kivy.storage.jsonstore import JsonStore
#import Json.questions as questionsJson

# store = dictionary with the tree-structure of the json file
# just try it

from KivyCommunication import *


class QuestionDisplay:
    """
    This object lies between the screen and the widget. It is used as a buffer between the two.
    """
    parent_screen = None

    def __init__(self, parent_screen=None):
        Logger.debug("20")
        self.parent_screen = parent_screen
        Logger.debug("21")
        self.the_widget = QuestionnaireWidget(parent_screen, self.parent_screen.main_app)
        Logger.debug("22")
        self.the_end = False
        Logger.debug("23")

    def load(self):
        self.is_playing = True


class QuestionnaireWidget(GridLayout):
    question_list = None
    main_app = None
    parent_screen = None

    def __init__(self, parent_screen, main_app):
        """
        :param main_app: The main app that runs the program. We use it to pass on the question list and the user answers
        """
        Logger.debug("30")
        super(QuestionnaireWidget, self).__init__(rows=2 * len(main_app.question_list) + 1, cols=1)
        Logger.debug("31")
        self.parent_screen = parent_screen
        Logger.debug("32")
        self.main_app = main_app
        Logger.debug("33")
        self.question_list = self.main_app.question_list
        self.questionsArray = []
        self.main_app.user_answers = []
        Logger.debug("34" + str(self.question_list))
        self.set_questions(self.question_list)
        Logger.debug("35")
        store = JsonStore("Json/questions.json", encoding='utf-8')
        Logger.debug("36")
        self.submit_button = LoggedButton(text=store['questionnaire']['next_button'][::-1],
                                          font_name="fonts/Alef-Regular.ttf", halign='right')
        Logger.debug("37")
        # print (store['questionnaire']['next_button'][::-1]) # DEBUG
        self.submit_button.name = 'questionnaire submit'
        Logger.debug("38")
        self.submit_button.bind(on_press=self.submit_action)
        Logger.debug("39")
        self.add_widget(self.submit_button)
        Logger.debug("40")

    # DO NOT REMOVE instance
    def submit_action(self, instance):
        """
        Called when the user presses the submit button. Saves the user's answers in the main app for future screens.
        :param instance: DO NOT REMOVE instance
        """
        go_to_answers = True
        bad_answers = []
        self.main_app.user_answers = []
        for question in self.questionsArray:
            if question.get_answer() is None:
                # At least one of the questions was left unanswered.
                go_to_answers = False
                bad_answers.append(question)
            else:
                self.main_app.user_answers.append(AnswerObject(question,
                                                               user_seen_graph=self.main_app.discovered_graph,
                                                               real_graph=self.main_app.current_graph))
        if go_to_answers:
            self.parent_screen.end_questionnaire()
        else:
            store = JsonStore("Json/questions.json", encoding='utf-8')
            self.main_app.user_answers = []
            popup = Popup(title=store['questionnaire']['error_message']['title'][::-1],font_name="fonts/Alef-Regular.ttf",
            halign='right',
                          content=Label(text=store['questionnaire']['error_message']['message'][::-1], font_name="fonts/Alef-Regular.ttf",
            halign='right'),
                          auto_dismiss=True,
                          size_hint=(None, None),
                          size=(800, 150))
            popup.open()

    def set_questions(self, question_list):
        """
        Goes over the question list, creates a new widget for each question and sets in in the window.
        """
        Logger.debug("50")
        for question in question_list:
            Logger.debug("51")
            new_question_label = Label(text=question.question_string, font_name="fonts/Alef-Regular.ttf", halign='right')
            Logger.debug("52")
            if question.question_type_number == QuestionTypes['NUMBER']:
                new_question = IntSpinner(question=question)
                Logger.debug("53")
            elif question.question_type_number == QuestionTypes['MULTIPLE_CHOICE']:
                new_question = MultipleAnswersObj(question=question)
                Logger.debug("54")

            elif question.question_type_number == QuestionTypes['BOOLEAN']:
                new_question = BooleanQuestion(question=question)
                Logger.debug("55")

            self.questionsArray.append(new_question)
            self.add_widget(new_question_label)
            self.add_widget(new_question)