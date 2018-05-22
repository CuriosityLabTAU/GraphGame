#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from KivyFiles.Questions.AnswerObject import AnswerObject
from KivyFiles.Questions.QuestionWidgets import MultipleAnswersObj, IntSpinner, BooleanQuestion
from SupplementaryFiles.Enums import QuestionTypes
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
        self.parent_screen = parent_screen
        self.the_widget = QuestionnaireWidget(parent_screen, self.parent_screen.main_app)
        self.the_end = False

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
        super(QuestionnaireWidget, self).__init__(rows=2 * len(main_app.question_list) + 1, cols=1)
        self.parent_screen = parent_screen
        self.main_app = main_app
        self.question_list = self.main_app.question_list
        self.questionsArray = []
        self.main_app.user_answers = []
        self.set_questions(self.question_list)
        store = JsonStore("Json/questions.json", encoding='utf-8')
        self.submit_button = LoggedButton(text=store['questionnaire']['next_button'][::-1],
                                          font_name="fonts/Alef-Regular.ttf", halign='right')
        print (store['questionnaire']['next_button'][::-1])
        self.submit_button.name = 'questionnaire submit'
        self.submit_button.bind(on_press=self.submit_action)
        self.add_widget(self.submit_button)

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
        for question in question_list:
            new_question_label = Label(text=question.question_string, font_name="fonts/Alef-Regular.ttf",
            halign='right')
            if question.question_type_number == QuestionTypes['NUMBER']:
                new_question = IntSpinner(question=question)

            elif question.question_type_number == QuestionTypes['MULTIPLE_CHOICE']:
                new_question = MultipleAnswersObj(question=question)

            elif question.question_type_number == QuestionTypes['BOOLEAN']:
                new_question = BooleanQuestion(question=question)

            self.questionsArray.append(new_question)
            self.add_widget(new_question_label)
            self.add_widget(new_question)