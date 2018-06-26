#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from KivyFiles.Questions.QuestionsDisplay import QuestionDisplay
from SupplementaryFiles.GLogger import GLogger
from SupplementaryFiles.GLogger import LogAction
from KivyCommunication import *
LANGUAGE = 'Hebrew'  # 'Hebrew'
from SupplementaryFiles.Utils import *
import logging
from kivy.core.audio import SoundLoader
from kivy.logger import Logger


class QuestionnaireScreen(Screen):
    real_user = True
    game_number = -1
    main_app = None

    questionnaire = None

    def setup(self, main_app, number=-1, real_user=True):
        """
        :param real_user: Bool. False if machine player
        :param number: The game number
        :param main_app: The main app that runs the program. We use it to pass the question list into the page and get
        the answers out of the page.
        """
        # Init
        self.size = (200, 100)
        self.game_number = number
        self.main_app = main_app
        self.real_user = real_user
        self.main_app.user_answers = []

        self.questionnaire = QuestionDisplay(self)

    def on_enter(self, *args):
        log_str = 'start,'

        GLogger.log(logging.INFO, "", action=LogAction.data, obj='game_questionnaire_' + str(self.game_number), comment=log_str)
        self.questionnaire.load()
        self.explanation()

    def explanation(self):
        if self.game_number == 0:
            SoundLoader.load('Sounds/1.wav').play()


    def end_questionnaire(self):
        GLogger.log(logging.INFO,"",action=LogAction.press, obj="Graph {} - Questions - {}"
                       .format(self.main_app.sm.current, self.main_app.user_answers), comment=self.main_app.user_id)
        self.next_game()

    def next_game(self):
        log_str = 'end game'
        GLogger.log(logging.INFO,"",action=LogAction.data, obj='game_questionnaire_' + str(self.game_number), comment=log_str)

        # log all the calculated things


        try:
            self.main_app.sm.current = 'game_results_' + str(self.game_number)

        except Exception as e:
            GLogger.log(logging.ERROR,"",action=LogAction.data, obj='game_questionnaire_', comment='the_end - {}'.format(e), sync=True)