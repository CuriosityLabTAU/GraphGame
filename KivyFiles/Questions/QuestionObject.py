#!/usr/bin/python
# -*- coding: utf-8 -*-
from SupplementaryFiles.Enums import Colours, QuestionTypes


class QuestionObject:
    """
    An object used for the questions displaying
    """

    def __init__(self, question_string, question_type_number, question_id, *args):
        """

        :param question_string: The string for the question
        :param question_type_number: a QuestionTypes enum
        :param question_id: The id of the question as referenced in the QuestionsAnswers class
        :param args:
        """
        self.question_string = question_string
        self.question_type_number = question_type_number
        self.get_question_values()
        self.question_id = question_id
        self.args = args

    def get_question_values(self):
        """
        Set parameters in the Question Obejcet that determin the type of answers it could receive.
        """
        # self.list_of_possible_answers Must only be created here!
        if self.question_type_number == QuestionTypes['NUMBER']:
            self.open_question = True

        elif self.question_type_number == QuestionTypes['MULTIPLE_CHOICE']:
            self.open_question = False
            self.list_of_possible_answers = []
            for colour in Colours:
                self.list_of_possible_answers.append(colour)

        elif self.question_type_number == QuestionTypes['BOOLEAN']:
            self.open_question = False
            self.list_of_possible_answers = []
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

