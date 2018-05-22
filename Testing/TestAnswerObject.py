import os

from GraphGeneration.CreateRandGraph import create_rand_graph
from KivyFiles.Questions.AnswerObject import AnswerObject
from KivyFiles.Questions.QuestionObject import QuestionObject
from KivyFiles.Questions.QuestionWidgets import IntSpinner
from SupplementaryFiles.Enums import QuestionTypes, Colours


def main():
    question_data = QuestionObject("how many {} nodes there are?", QuestionTypes['NUMBER'], 1, Colours.red)
    question = IntSpinner(question=question_data)
    question.text = '6'
    graph_user = create_rand_graph("{}\..\GraphsData\config.ini".format(os.getcwd()))
    graph_real = create_rand_graph("{}\..\GraphsData\config.ini".format(os.getcwd()))
    for i in range(len(graph_user.node_list)):
        graph_user.node_list[i].colour = Colours.yellow['name']
        graph_real.node_list[i].colour = Colours.red['name']

    for i in range(len(graph_user.node_list)-5):
        graph_user.node_list[i].colour = Colours.red

    answer = AnswerObject(question_object=question, user_seen_graph=graph_user, real_graph=graph_real)

    print(answer)
