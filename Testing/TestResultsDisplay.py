import os
import unittest
from GraphGeneration.CreateRandGraph import create_rand_graph
from KivyFiles.Questions.AnswerObject import AnswerObject
from KivyFiles.Questions.QuestionObject import QuestionObject
from KivyFiles.Questions.QuestionWidgets import IntSpinner
from KivyFiles.Questions.ResultDisplay import ResultDisplay
from SupplementaryFiles.Enums import Colours, QuestionTypes
from GraphGeneration.HandmadeGraph import create_draft_graph_1
from KivyFiles.Questions.ResultDisplay import ResultWidget

def main():

    user_graph = create_rand_graph("{}\..\GraphsData\config.ini".format(os.getcwd()))
    true_graph = create_rand_graph("{}\..\GraphsData\config.ini".format(os.getcwd()))
    for i in range(len(user_graph.node_list)):
        user_graph.node_list[i].colour = Colours.yellow['name']
        true_graph.node_list[i].colour = Colours.red['name']

    for i in range(len(user_graph.node_list)-5):
        user_graph.node_list[i].colour = Colours.red['name']

    answer_list = []

    for i in range(10):
        question_data = QuestionObject("how many {} nodes there are?", QuestionTypes['NUMBER'], 1, Colours.red)
        question = IntSpinner(question=question_data)
        question.text = '6'
        answer = AnswerObject(question_object=question, user_seen_graph=user_graph, real_graph=true_graph)
        answer_list.append(answer)

    display = ResultDisplay(answer_list, user_graph, true_graph)
    display.run()


class TestCalculatePercentage(unittest.TestCase):

    def test_upper(self):
        #prepare

        user_graph = create_draft_graph_1()
        true_graph = create_draft_graph_1()
        question_data = QuestionObject("how many {} nodes there are?", QuestionTypes['NUMBER'], 1, Colours.get("red"))
        question = IntSpinner(question=question_data)
        user_answers = [AnswerObject(question_object=question, user_seen_graph=user_graph, real_graph=true_graph),
                        AnswerObject(question_object=question, user_seen_graph=user_graph, real_graph=true_graph)]
        user_answers[0].user_answer = ["1"]
        user_answers[0].user_graph_answer = ["1"]
        user_answers[0].real_answer = ["1"]
        user_answers[1].user_answer = ["yellow", "blue"]
        user_answers[1].user_graph_answer = ["red"]
        user_answers[1].real_answer = ["blue", "red"]

        #act

        results_dict_0 = ResultWidget.calculate_percentage([user_answers[0]])
        print (results_dict_0)
        possible_score_0 = results_dict_0.get("possible_score")
        user_score_0 = results_dict_0.get("user_score")
        results_dict_1 = ResultWidget.calculate_percentage([user_answers[1]])
        possible_score_1 = results_dict_1.get("possible_score")
        user_score_1 = results_dict_1.get("user_score")
        print (results_dict_1)
        #assert
        self.assertEqual(possible_score_0,5)
        self.assertEqual(user_score_0,5)
        self.assertEqual(possible_score_1,0)
        self.assertEqual(user_score_1,0)




#if __name__ == "__main__":
    #main()


