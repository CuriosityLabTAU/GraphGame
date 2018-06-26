#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

from os import path

from KivyFiles.Questions.QuestionObject import QuestionObject
from NodeObject import NodeObject
from Enums import Colours
from GraphObj import GraphObject

SAVED_GRAPH_PATH = "../GraphsData"


def save_graph_json(graph, file_name=None):
    file_data = {"center_node": graph.center_node, "size": graph.size, "extra_distance": graph.extra_distance,
                 "max_neighbors": graph.max_neighbors, "node_count": graph.node_count, "line_colour": graph.line_colour,
                 "connections": graph.connections, "question_object_list": {}, "node_list": {}}

    # Question_object_list
    for i in range(len(graph.question_object_list)):
        file_data["question_object_list"][str(i)] = {}
        file_data["question_object_list"][str(i)]["question_string"] = graph.question_object_list[i].question_string
        file_data["question_object_list"][str(i)]["question_type_number"] = graph.question_object_list[i].question_type_number
        file_data["question_object_list"][str(i)]["question_id"] = graph.question_object_list[i].question_id
        file_data["question_object_list"][str(i)]["args"] = json.dumps(graph.question_object_list[i].args)

    # Node list
    for i in range(len(graph.node_list)):
        serial = graph.node_list[i].serial_num
        file_data["node_list"][serial] = {}
        file_data["node_list"][serial]["node_x"] = graph.node_list[i].x
        file_data["node_list"][serial]["node_y"] = graph.node_list[i].y
        file_data["node_list"][serial]["node_size"] = graph.node_list[i].size
        file_data["node_list"][serial]["colour"] = str(graph.node_list[i].colour['name'])
        file_data["node_list"][serial]["shape"] = graph.node_list[i].shape
        file_data["node_list"][serial]["real"] = graph.node_list[i].real
        file_data["node_list"][serial]["dummy_num"] = graph.node_list[i].dummy_num
        file_data["node_list"][serial]["neighbors"] = json.dumps(list(graph.node_list[i].neighbors))
        file_data["node_list"][serial]["possible_neighbors"] = json.dumps(list(graph.node_list[i].possible_neighbors))

    if file_name is not None:
        file_path = path.join(SAVED_GRAPH_PATH, file_name)
        with open(file_path, 'w') as output:
            output.write(json.dumps(file_data))

    return file_data


def load_graph_from_json(file_name):

    if not path.exists(file_name):
        raise IOError("File not found", path=file_name)

    new_graph = GraphObject()
    new_graph.source_file = file_name
    with open(file_name) as f:
        data = json.loads(f.read())
        new_graph.size["max_x"] = data["size"]["max_x"]
        new_graph.size["max_y"] = data["size"]["max_y"]
        new_graph.extra_distance = data["extra_distance"]
        new_graph.center_node = data["center_node"]
        new_graph.max_neighbors = data["max_neighbors"]
        new_graph.line_colour = data["line_colour"]
        new_graph.node_count = data["node_count"]
        new_graph.connections = [(str(item[0]), str(item[1])) for item in data["connections"]]
        new_graph.question_object_list = []
        new_graph.node_list = []

        for node in data["node_list"]:
            node_shape = data["node_list"][node]["shape"]
            node_size = data["node_list"][node]["node_size"]
            node_location = {'x': data["node_list"][node]["node_x"],
                             'y': data["node_list"][node]["node_y"]}
            node_colour = Colours[data["node_list"][node]["colour"]]
            node_neighbors = set(json.loads(data["node_list"][node]["neighbors"]))
            possible_neighbors = set(json.loads(data["node_list"][node]["possible_neighbors"]))
            new_node = NodeObject(node, node_location, node_size, node_colour, node_shape)
            new_node.neighbors = node_neighbors
            new_node.possible_neighbors = possible_neighbors
            new_graph.node_list.append(new_node)

        for question in data["question_object_list"]:
            question_type_number = data["question_object_list"][question]["question_type_number"]
            question_string = data["question_object_list"][question]["question_string"]
            question_id = data["question_object_list"][question]["question_id"]
            args = json.loads(data["question_object_list"][question]["args"])

            question_object = QuestionObject(question_string, question_type_number, question_id, *args)
            new_graph.question_object_list.append(question_object)
    return new_graph


def from_name_to_color(name):
    from SupplementaryFiles import Enums

    if name == "red":
        return Enums.Colours['red']
    if name == "yellow":
        return Enums.Colours['yellow']
    if name == "blue":
        return Enums.Colours['blue']
    return -1


def from_name_to_shape(name):
    from SupplementaryFiles import Enums

    if name == "Circle":
        return Enums.Shapes['circle']
