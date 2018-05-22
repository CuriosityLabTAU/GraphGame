#!/usr/bin/python
# -*- coding: utf-8 -*-
from SupplementaryFiles.Enums import Colours, QuestionTypes
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.GraphSaveLoad import load_graph_from_json, save_graph_json
from KivyFiles.Questions.QuestionObject import QuestionObject
from SupplementaryFiles.GLogger import *
from kivy.storage.jsonstore import JsonStore

def create_draft_graph_1():
    GLogger('file', 'handmade_graph_logger.txt', 'ERROR')

    draft_graph = GraphObject(max_x=2750, max_y=2850, node_count=15, max_neighbors=5, extra_distance=1)
    draft_graph.add_node(x_loc=2169, y_loc=2163, node_colour=Colours['yellow'], serial='n1')
    draft_graph.add_node(x_loc=2450, y_loc=2792, node_colour=Colours['red'], serial='n2')
    draft_graph.add_node(x_loc=1255, y_loc=2556, node_colour=Colours['blue'], serial='n3')
    draft_graph.add_node(x_loc=1879, y_loc=1911, node_colour=Colours['blue'], serial='n4')
    draft_graph.add_node(x_loc=772, y_loc=2120, node_colour=Colours['red'], serial='n5')
    draft_graph.add_node(x_loc=343, y_loc=1456, node_colour=Colours['red'], serial='n6')
    draft_graph.add_node(x_loc=319, y_loc=2011, node_colour=Colours['yellow'], serial='n7')
    draft_graph.add_node(x_loc=902, y_loc=741, node_colour=Colours['blue'], serial='n8')
    draft_graph.add_node(x_loc=345, y_loc=833, node_colour=Colours['red'], serial='n9')
    draft_graph.add_node(x_loc=1322, y_loc=1531, node_colour=Colours['red'], serial='n10')
    draft_graph.add_node(x_loc=2006, y_loc=877, node_colour=Colours['blue'], serial='n11')
    draft_graph.add_node(x_loc=2289, y_loc=374, node_colour=Colours['red'], serial='n12')
    draft_graph.add_node(x_loc=1514, y_loc=1113, node_colour=Colours['yellow'], serial='n13')
    draft_graph.add_node(x_loc=2676, y_loc=1082, node_colour=Colours['yellow'], serial='n14')
    draft_graph.add_node(x_loc=748, y_loc=2434, node_colour=Colours['blue'], serial='n15')
    draft_graph.center_node = "n1"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n3"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n5"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n7"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n12"), draft_graph.get_node_by_serial("n11"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n6"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n14"), draft_graph.get_node_by_serial("n12"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n7"), draft_graph.get_node_by_serial("n15"))
    save_graph_json(draft_graph, "Graph_1.json")
    return draft_graph


def create_draft_graph_2():

    draft_graph = GraphObject(max_x=2450, max_y=3200, node_count=15, max_neighbors=5, extra_distance=1)
    draft_graph.add_node(x_loc=144, y_loc=2252, node_colour=Colours['blue'], serial='n1')
    draft_graph.add_node(x_loc=506, y_loc=2525, node_colour=Colours['yellow'], serial='n2')
    draft_graph.add_node(x_loc=1224, y_loc=2052, node_colour=Colours['blue'], serial='n3')
    draft_graph.add_node(x_loc=1704, y_loc=2434, node_colour=Colours['blue'], serial='n4')
    draft_graph.add_node(x_loc=1824, y_loc=1526, node_colour=Colours['red'], serial='n5')
    draft_graph.add_node(x_loc=2064, y_loc=1071, node_colour=Colours['red'], serial='n6')
    draft_graph.add_node(x_loc=1344, y_loc=890, node_colour=Colours['red'], serial='n7')
    draft_graph.add_node(x_loc=1464, y_loc=617, node_colour=Colours['blue'], serial='n8')
    draft_graph.add_node(x_loc=2376, y_loc=617, node_colour=Colours['yellow'], serial='n9')
    draft_graph.add_node(x_loc=746, y_loc=981, node_colour=Colours['blue'], serial='n10')
    draft_graph.add_node(x_loc=360, y_loc=1529, node_colour=Colours['red'], serial='n11')
    draft_graph.add_node(x_loc=72, y_loc=1635, node_colour=Colours['yellow'], serial='n12')
    draft_graph.add_node(x_loc=508, y_loc=1689, node_colour=Colours['blue'], serial='n13')
    draft_graph.add_node(x_loc=1226, y_loc=163, node_colour=Colours['red'], serial='n14')
    draft_graph.add_node(x_loc=196, y_loc=3161, node_colour=Colours['blue'], serial='n15')
    draft_graph.center_node = "n2"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n3"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n5"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n6"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n11"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n12"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n14"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n7"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n15"))

    question_one = QuestionObject("How many red nodes are there?",
                                  QuestionTypes['NUMBER'], 1, Colours['red'])
    question_two = QuestionObject("How many blue nodes do not have links to yellow nodes",
                                  QuestionTypes['NUMBER'], 5, Colours['blue'], Colours['yellow'])
    question_three = QuestionObject("Which color has the largest number of nodes?",
                                    QuestionTypes['MULTIPLE_CHOICE'], 16)
    question_four = QuestionObject("Is there a blue node that has at least 2 links to another blue node?",
                                   QuestionTypes['BOOLEAN'], 11, Colours['blue'], 2)
    question_five = QuestionObject("What is the color of the node with the largest number of links?",
                                   QuestionTypes['MULTIPLE_CHOICE'], 3)
    question_six = QuestionObject("Is every blue node linked to a red node?",
                                  QuestionTypes['BOOLEAN'], 9, Colours['blue'], Colours['red'])
    question_seven = QuestionObject("Is there an even number of yellow nodes?",
                                    QuestionTypes['BOOLEAN'], 15, Colours['yellow'], 0)
    draft_graph.question_object_list = [question_one, question_two, question_three, question_four, question_five,
                                        question_six, question_seven]

    save_graph_json(draft_graph, "Graph_2.json")


def create_draft_graph_3():
    GLogger('file', 'handmade_graph_logger.txt', 'ERROR')
    draft_graph = GraphObject(max_x=2950, max_y=2850, node_count=15, max_neighbors=5, extra_distance=1)
    draft_graph.add_node(x_loc=62, y_loc=90, node_colour=Colours['yellow'], serial='n1')
    draft_graph.add_node(x_loc=1082, y_loc=726, node_colour=Colours['blue'], serial='n2')
    draft_graph.add_node(x_loc=482, y_loc=944, node_colour=Colours['blue'], serial='n3')
    draft_graph.add_node(x_loc=1800, y_loc=581, node_colour=Colours['blue'], serial='n4')
    draft_graph.add_node(x_loc=1584, y_loc=1358, node_colour=Colours['yellow'], serial='n5')
    draft_graph.add_node(x_loc=2880, y_loc=726, node_colour=Colours['red'], serial='n6')
    draft_graph.add_node(x_loc=1896, y_loc=90, node_colour=Colours['yellow'], serial='n7')
    draft_graph.add_node(x_loc=2090, y_loc=1911, node_colour=Colours['yellow'], serial='n8')
    draft_graph.add_node(x_loc=2496, y_loc=1235, node_colour=Colours['blue'], serial='n9')
    draft_graph.add_node(x_loc=1130, y_loc=2147, node_colour=Colours['red'], serial='n10')
    draft_graph.add_node(x_loc=2904, y_loc=2328, node_colour=Colours['red'], serial='n11')
    draft_graph.add_node(x_loc=132, y_loc=1653, node_colour=Colours['blue'], serial='n12')
    draft_graph.add_node(x_loc=484, y_loc=2610, node_colour=Colours['yellow'], serial='n13')
    draft_graph.add_node(x_loc=1586, y_loc=2739, node_colour=Colours['red'], serial='n14')
    draft_graph.add_node(x_loc=2378, y_loc=2801, node_colour=Colours['blue'], serial='n15')
    draft_graph.center_node = "n2"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n3"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n4"), draft_graph.get_node_by_serial("n5"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n4"), draft_graph.get_node_by_serial("n6"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n7"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n5"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n9"), draft_graph.get_node_by_serial("n11"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n12"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n13"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n14"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n15"), draft_graph.get_node_by_serial("n14"))

    question_one = QuestionObject('Is there a red node with an odd number of links?',
                                  QuestionTypes['BOOLEAN'], 12, Colours['red'], 1)
    question_two = QuestionObject('Which color has the smallest number of nodes?',
                                  QuestionTypes['MULTIPLE_CHOICE'], 17)
    question_three = QuestionObject('How many blue nodes are there?',
                                    QuestionTypes['NUMBER'], 1, Colours['blue'])
    question_four = QuestionObject('What is the color of the node with the largest number of links?',
                                   QuestionTypes['MULTIPLE_CHOICE'], 3)
    question_five = QuestionObject('Does every red node have a link to a yellow node?',
                                   QuestionTypes['BOOLEAN'], 9, Colours['red'], Colours['yellow'])
    question_six = QuestionObject('Does all the blue nodes have an even number of links?',
                                  QuestionTypes['BOOLEAN'], 13, Colours['blue'], 0)
    question_seven = QuestionObject('Are there more red nodes than blue nodes?',
                                    QuestionTypes['BOOLEAN'], 10, Colours['red'], Colours['blue'])
    draft_graph.question_object_list = [question_one, question_two, question_three, question_four, question_five,
                                        question_six, question_seven]

    save_graph_json(draft_graph, "Graph_3.json")


def create_draft_graph_4():
    GLogger('file', 'handmade_graph_logger.txt', 'ERROR')
    draft_graph = GraphObject(max_x=4750, max_y=2400, node_count=15, max_neighbors=5, extra_distance=1)
    draft_graph.add_node(x_loc=936, y_loc=1671, node_colour=Colours['blue'], serial='n1')
    draft_graph.add_node(x_loc=480, y_loc=1998, node_colour=Colours['yellow'], serial='n2')
    draft_graph.add_node(x_loc=96, y_loc=908, node_colour=Colours['blue'], serial='n3')
    draft_graph.add_node(x_loc=1668, y_loc=2007, node_colour=Colours['red'], serial='n4')
    draft_graph.add_node(x_loc=2112, y_loc=1816, node_colour=Colours['yellow'], serial='n5')
    draft_graph.add_node(x_loc=2976, y_loc=1825, node_colour=Colours['yellow'], serial='n6')
    draft_graph.add_node(x_loc=2392, y_loc=2356, node_colour=Colours['blue'], serial='n7')
    draft_graph.add_node(x_loc=3360, y_loc=1271, node_colour=Colours['blue'], serial='n8')
    draft_graph.add_node(x_loc=1788, y_loc=1453, node_colour=Colours['red'], serial='n9')
    draft_graph.add_node(x_loc=4440, y_loc=1280, node_colour=Colours['blue'], serial='n10')
    draft_graph.add_node(x_loc=3600, y_loc=1734, node_colour=Colours['yellow'], serial='n11')
    draft_graph.add_node(x_loc=4680, y_loc=1635, node_colour=Colours['red'], serial='n12')
    draft_graph.add_node(x_loc=480, y_loc=1380, node_colour=Colours['red'], serial='n13')
    draft_graph.add_node(x_loc=2880, y_loc=566, node_colour=Colours['red'], serial='n14')
    draft_graph.add_node(x_loc=3372, y_loc=1998, node_colour=Colours['red'], serial='n15')
    draft_graph.center_node = "n1"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n3"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n4"), draft_graph.get_node_by_serial("n5"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n7"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n11"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n15"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n7"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n7"), draft_graph.get_node_by_serial("n15"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n14"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n12"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n14"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n15"))

    question_one = QuestionObject('Is there a red node that has at least two links to another red node?',
                                  QuestionTypes['BOOLEAN'], 11, Colours['red'], 2)
    question_two = QuestionObject('Is the sum of the links of all the red nodes even?',
                                  QuestionTypes['BOOLEAN'], 14, Colours['red'], 0)
    question_three = QuestionObject('Which color has the largest number of nodes?',
                                    QuestionTypes['MULTIPLE_CHOICE'], 16)
    question_four = QuestionObject('How many blue nodes have links to yellow nodes?',
                                   QuestionTypes['NUMBER'], 2, Colours['blue'], Colours['yellow'])
    question_five = QuestionObject('What is the color that contains the largest total number of links?',
                                   QuestionTypes['MULTIPLE_CHOICE'], 4)
    question_six = QuestionObject('Does every yellow node have a link to a red node?',
                                  QuestionTypes['BOOLEAN'], 9, Colours['yellow'], Colours['red'])
    question_seven = QuestionObject('Are there more blue nodes than yellow nodes?',
                                    QuestionTypes['BOOLEAN'], 10, Colours['blue'], Colours['yellow'])
    draft_graph.question_object_list = [question_one, question_two, question_three, question_four, question_five,
                                        question_six, question_seven]

    save_graph_json(draft_graph, "Graph_4.json")


def create_draft_graph_5():
    GLogger('file', 'handmade_graph_logger.txt', 'ERROR')
    draft_graph = GraphObject(max_x=2350, max_y=3050, node_count=15, max_neighbors=5, extra_distance=1)
    draft_graph.add_node(x_loc=405, y_loc=2786, node_colour=Colours['red'], serial='n1')
    draft_graph.add_node(x_loc=340, y_loc=441, node_colour=Colours['red'], serial='n2')
    draft_graph.add_node(x_loc=657, y_loc=1902, node_colour=Colours['red'], serial='n3')
    draft_graph.add_node(x_loc=187, y_loc=2512, node_colour=Colours['blue'], serial='n4')
    draft_graph.add_node(x_loc=336, y_loc=1153, node_colour=Colours['blue'], serial='n5')
    draft_graph.add_node(x_loc=1747, y_loc=2763, node_colour=Colours['yellow'], serial='n6')
    draft_graph.add_node(x_loc=1809, y_loc=514, node_colour=Colours['blue'], serial='n7')
    draft_graph.add_node(x_loc=1845, y_loc=2169, node_colour=Colours['blue'], serial='n8')
    draft_graph.add_node(x_loc=1125, y_loc=2383, node_colour=Colours['blue'], serial='n9')
    draft_graph.add_node(x_loc=1681, y_loc=1621, node_colour=Colours['yellow'], serial='n10')
    draft_graph.add_node(x_loc=1456, y_loc=152, node_colour=Colours['blue'], serial='n11')
    draft_graph.add_node(x_loc=2011, y_loc=1486, node_colour=Colours['red'], serial='n12')
    draft_graph.add_node(x_loc=2008, y_loc=345, node_colour=Colours['yellow'], serial='n13')
    draft_graph.add_node(x_loc=1449, y_loc=2993, node_colour=Colours['red'], serial='n14')
    draft_graph.add_node(x_loc=2296, y_loc=812, node_colour=Colours['red'], serial='n15')
    draft_graph.center_node = "n5"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n3"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n2"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n12"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n12"), draft_graph.get_node_by_serial("n11"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n12"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n13"), draft_graph.get_node_by_serial("n15"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n7"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n14"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n12"))

    question_one = QuestionObject('Is there a yellow node that has at least 3 links to another yellow node?',
                                  QuestionTypes['BOOLEAN'], 11, Colours['yellow'], 3)
    question_two = QuestionObject('Does all the red nodes have an odd number of links?',
                                  QuestionTypes['BOOLEAN'], 13, Colours['red'], 1)
    question_three = QuestionObject('How many yellow nodes are there?',
                                    QuestionTypes['NUMBER'], 1, Colours['yellow'])
    question_four = QuestionObject('What is the color that contains the smallest total number of links?',
                                   QuestionTypes['MULTIPLE_CHOICE'], 7)
    question_five = QuestionObject('Does every blue node have a link to a yellow node?',
                                   QuestionTypes['BOOLEAN'], 9, Colours['blue'], Colours['yellow'])
    question_six = QuestionObject('Is the number of blue nodes even?',
                                  QuestionTypes['BOOLEAN'], 15, Colours['blue'], 0)
    question_seven = QuestionObject('How many yellow nodes do not have links to red nodes?',
                                    QuestionTypes['NUMBER'], 5, Colours['yellow'], Colours['red'])
    draft_graph.question_object_list = [question_one, question_two, question_three, question_four, question_five,
                                        question_six, question_seven]

    save_graph_json(draft_graph, "Graph_5.json")


# graph1 transpose
def create_draft_graph_1_Transpose():

    GLogger('file', 'handmade_graph_logger.txt', 'ERROR')

    draft_graph = GraphObject(max_x=2850, max_y=2750, node_count=15, max_neighbors=5, extra_distance=1)
    draft_graph.add_node(x_loc=2163, y_loc=2169, node_colour=Colours['yellow'], serial='n1')
    draft_graph.add_node(x_loc=2792, y_loc=2450, node_colour=Colours['red'], serial='n2')
    draft_graph.add_node(x_loc=2556, y_loc=1255, node_colour=Colours['blue'], serial='n3')
    draft_graph.add_node(x_loc=1911, y_loc=1879, node_colour=Colours['blue'], serial='n4')
    draft_graph.add_node(x_loc=2120, y_loc=772, node_colour=Colours['red'], serial='n5')
    draft_graph.add_node(x_loc=1456, y_loc=343, node_colour=Colours['red'], serial='n6')
    draft_graph.add_node(x_loc=2011, y_loc=319, node_colour=Colours['yellow'], serial='n7')
    draft_graph.add_node(x_loc=741, y_loc=902, node_colour=Colours['blue'], serial='n8')
    draft_graph.add_node(x_loc=833, y_loc=345, node_colour=Colours['red'], serial='n9')
    draft_graph.add_node(x_loc=1531, y_loc=1322, node_colour=Colours['red'], serial='n10')
    draft_graph.add_node(x_loc=877, y_loc=2006, node_colour=Colours['blue'], serial='n11')
    draft_graph.add_node(x_loc=374, y_loc=2289, node_colour=Colours['red'], serial='n12')
    draft_graph.add_node(x_loc=1113, y_loc=1514, node_colour=Colours['yellow'], serial='n13')
    draft_graph.add_node(x_loc=1082, y_loc=2676, node_colour=Colours['yellow'], serial='n14')
    draft_graph.add_node(x_loc=2434, y_loc=748, node_colour=Colours['blue'], serial='n15')
    draft_graph.center_node = "n1"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n3"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n5"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n7"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n12"), draft_graph.get_node_by_serial("n11"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n6"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n14"), draft_graph.get_node_by_serial("n12"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n7"), draft_graph.get_node_by_serial("n15"))

    question_one = QuestionObject("How many red nodes do not have links to yellow nodes?",
                                  QuestionTypes['NUMBER'], 5, Colours['red'], Colours['yellow'])
    question_two = QuestionObject("Is the number of red nodes even?",
                                  QuestionTypes['BOOLEAN'], 15, Colours['red'], 0)
    question_three = QuestionObject("Does all the blue nodes have an odd number of links?",
                                    QuestionTypes['BOOLEAN'], 13, Colours['blue'], 1)
    question_four = QuestionObject("What is the color that contains the smallest total number of links?",
                                   QuestionTypes['MULTIPLE_CHOICE'], 7)
    question_five = QuestionObject("Does every yellow node have a link to a red node?",
                                   QuestionTypes['BOOLEAN'], 9, Colours['yellow'], Colours['red'])
    question_six = QuestionObject("Are there more blue nodes than yellow nodes?",
                                  QuestionTypes['BOOLEAN'], 10, Colours['blue'], Colours['yellow'])
    question_seven = QuestionObject("Is there a red nodes that has a link to another red node?",
                                    QuestionTypes['BOOLEAN'], 8, Colours['red'])
    draft_graph.question_object_list = [question_one, question_two, question_three, question_four, question_five,
                                        question_six, question_seven]

    save_graph_json(draft_graph, "Graph_1_transpose.json")


#graph1 90 degrees counter clockwise

def create_draft_graph_1_rotate():
    GLogger('file', 'handmade_graph_logger.txt', 'ERROR')

    draft_graph = GraphObject(max_x=2850, max_y=2750, node_count=15, max_neighbors=5, extra_distance=1)
    draft_graph.add_node(x_loc=687, y_loc=2169, node_colour=Colours['yellow'], serial='n1')
    draft_graph.add_node(x_loc=58, y_loc=2450, node_colour=Colours['red'], serial='n2')
    draft_graph.add_node(x_loc=294, y_loc=1255, node_colour=Colours['blue'], serial='n3')
    draft_graph.add_node(x_loc=939, y_loc=1879, node_colour=Colours['blue'], serial='n4')
    draft_graph.add_node(x_loc=730, y_loc=772, node_colour=Colours['red'], serial='n5')
    draft_graph.add_node(x_loc=1394, y_loc=343, node_colour=Colours['red'], serial='n6')
    draft_graph.add_node(x_loc=839, y_loc=319, node_colour=Colours['yellow'], serial='n7')
    draft_graph.add_node(x_loc=2109, y_loc=902, node_colour=Colours['blue'], serial='n8')
    draft_graph.add_node(x_loc=2017, y_loc=345, node_colour=Colours['red'], serial='n9')
    draft_graph.add_node(x_loc=1319, y_loc=1322, node_colour=Colours['red'], serial='n10')
    draft_graph.add_node(x_loc=1973, y_loc=2006, node_colour=Colours['blue'], serial='n11')
    draft_graph.add_node(x_loc=2476, y_loc=2289, node_colour=Colours['red'], serial='n12')
    draft_graph.add_node(x_loc=1737, y_loc=1514, node_colour=Colours['yellow'], serial='n13')
    draft_graph.add_node(x_loc=1768, y_loc=2676, node_colour=Colours['yellow'], serial='n14')
    draft_graph.add_node(x_loc=416, y_loc=748, node_colour=Colours['blue'], serial='n15')
    draft_graph.center_node = "n1"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n3"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n5"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n7"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n12"), draft_graph.get_node_by_serial("n11"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n6"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n14"), draft_graph.get_node_by_serial("n12"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n7"), draft_graph.get_node_by_serial("n15"))

    question_one = QuestionObject("How many red nodes do not have links to yellow nodes?",
                                  QuestionTypes['NUMBER'], 5, Colours['red'], Colours['yellow'])
    question_two = QuestionObject("Is the number of red nodes even?",
                                  QuestionTypes['BOOLEAN'], 15, Colours['red'], 0)
    question_three = QuestionObject("Does all the blue nodes have an odd number of links?",
                                    QuestionTypes['BOOLEAN'], 13, Colours['blue'], 1)
    question_four = QuestionObject("What is the color that contains the smallest total number of links?",
                                   QuestionTypes['MULTIPLE_CHOICE'], 7)
    question_five = QuestionObject("Does every yellow node have a link to a red node?",
                                   QuestionTypes['BOOLEAN'], 9, Colours['yellow'], Colours['red'])
    question_six = QuestionObject("Are there more blue nodes than yellow nodes?",
                                  QuestionTypes['BOOLEAN'], 10, Colours['blue'], Colours['yellow'])
    question_seven = QuestionObject("Is there a red nodes that has a link to another red node?",
                                    QuestionTypes['BOOLEAN'], 8, Colours['red'])
    draft_graph.question_object_list = [question_one, question_two, question_three, question_four, question_five,
                                        question_six, question_seven]

    save_graph_json(draft_graph, "Graph_1_rotate.json")



#create_draft_graph_1_Transpose()
#create_draft_graph_1_rotate()
#create_draft_graph_1()
#create_draft_graph_2()
#create_draft_graph_3()
#create_draft_graph_4()
#create_draft_graph_5()