## The Curiosity Evaluation Tool
The Curiosity Evaluation Tool (CET) employs a three phase experiment in order to get a measurement of curiosity.
It is built by Dr. Gordon's curiosity lab and if found valid, could be used at the entrance exams for gifted classes and for job interviews.
The CET could be used by researchers, educators, human resources and more.
This application is one of the CETs used by the lab.

## Directory Structure

#### Fonts
Folder used to store fonts for lab use - mainly to allow for hebrew text

#### GraphGeneration
Contains tools to allow us to create a tests graphs manually.
* [GraphValidator](GraphGeneration/GraphValidator.py) - Allow enumerating over all steps to make sure the graph has only a single solution.
* [HandmadeGraph](GraphGeneration/HandmadeGraph.py) - Allows creating graphs manually.
* [KivyRunner](GraphGeneration/KivyRunner.py) - Allows to view a graph or play it without any other functionality.
* [CreateRandGraph](GraphGeneration/CreateRandGraph.py) - Creates random graphs.

#### GraphsData
Contains all the graphs used in the main game. All graphs are in json format.

#### Images
Contains images used in the project and game

#### KivyCommunication
Communication modules used by the lab. External code to program
* [kivy_logger](KivyCommunication/kivy_logger.py) - Main logger file. Sends data to server in lab
* [logged_widgets](KivyCommunication/logged_widgets.py) - Used for logging specific actions of widgets
* [twisted_client](KivyCommunication/twisted_client.py)  - Used by my logger for client-server interactions

#### KivyFiles
Contains almost all of the kivy files used in the project
***Questions Folder***\
Contains Kivy files used in the questionnaire and the result screen.
* [AnswerObject](KivyFiles/Questions/AnswerObject.py) - An objects that holds all data about a question, including the answer the user gave, the answer
as seen in both the graph discovered by the user and in the true graph. Used by the result screen.
* [QuestionObject](KivyFiles/Questions/QuestionObject.py) - A question object is used in the questionnaire. Holds information
about a question and the answers given to it.
* [QuestionsAnswers](KivyFiles/Questions/QuestionsAnswers.py) - Answers a question based on the type of question, the graph given and other arguments.
* [QuestionsDisplay](KivyFiles/Questions/QuestionsDisplay.py) - Holds Question display and QuestionnaireWidget. Used to display the actual questionnaire.
* [QuestionWidgets](KivyFiles/Questions/QuestionWidgets.py) - A widget used to hold the kivy information about a question for display proposes.
* [ResultDisplay](KivyFiles/Questions/ResultDisplay.py) - Holds ResultDisplay and ResultWidget. Used to display the result screen.

***Main Folder***\
* [GameLayout](KivyFiles/GameLayout.py) - Controls the displaying of the entire game. Contains the GraphLayout and the buttons.
* [GraphButton](KivyFiles/GraphButton.py) - Graph buttons a sophisticated WidgetButton that allows greater functionality in the application.
* [GraphDisplay](KivyFiles/GraphDisplay.py) - A layout that allows the entire graph to be displayed onscreen.
* [GraphLayout](KivyFiles/GraphLayout.py) - A kivy layout that contains the graph in a format that can be displayed.
* [GraphTabletDisplay](KivyFiles/GraphTabletDisplay.py) - Controls the game playing, also responsible for sending out the information seen onscreen.
* [KivyEdge](KivyFiles/KivyEdge.py) - A connection between two kivy nodes is a KivyEdge.
* [KivyGraph](KivyFiles/KivyGraph.py) - Graph object use by the graph layout to hold information about the graph.
* [KivyNode](KivyFiles/KivyNode.py) - Node objects use by the kivy graph to hold information about each node.

#### QLearning
Contains the Q learner and resulting files
* [QLearner](QLearning/QLearner.py) - Contains Qplayer and QMatrix.
QMatrix holds the matrix used to calculate each step.
QPlayer runs a series of games (episodes) that allow the QMatrix to be built up over time.

#### ScrapPad
Used for personal files

#### SupplementaryFiles
* [Enums](SupplementaryFiles/Enums.py) - Holds all enums used in the repository
* [GameDataHandler](SupplementaryFiles/GameDataHandler.py) - The main class that handle all graph data. Tracks information about the graph,
connections, false nodes, partial knowledge etc.
* [GraphObj](SupplementaryFiles/GraphObj.py) - Graph Objects hold all the data about a graph.
 All actions on the graph itself are done through this object
* [GraphSaveLoad](SupplementaryFiles/GraphSaveLoad.py) - Loads\Saves a graph from and to a json file.
* [NodeObject](SupplementaryFiles/NodeObject.py) - Node Objects as the basis of all graphs.
 Any action taken by or on a node is done through this object
* [Point](SupplementaryFiles/Point.py) - Inherited by the NodeObject. A point with functionality.
* [LineEquation](SupplementaryFiles/LineEquation.py) - Used to create a line equation for calculations.
Used to understand how nodes connect to each other in space.
* [RepeatedTimer](SupplementaryFiles/RepeatedTimer.py) - Used by GameLayout to run threads
* [Utils](SupplementaryFiles/Utils.py) - Contains general functions used all around the repository
* [GLogger](SupplementaryFiles/GLogger.py) - Personal logging library used to integrate with the lab's logging style

#### Testing
Contains testers for the project

#### Main Folder
* [Main](Main.py) - The starting point of the application.
* [GraphGameScreen](GraphGameScreen.py) - The screen object that holds the graph game part of the app. All graph interactions start here.
* [QuestionnaireScreen](QuestionnaireScreen.py) - The screen object that holds the questionnaire part of the app. All questionnaire interactions start here.
* [ResultsScreen](ResultsScreen.py) - The screen object that holds the result part of the app.
Building the widget that displayed the results to the user are constructed under this.
* [LoginScreen](LoginScreen.py) - The screen object that holds the login part of the app.
Building the widget that displayed the results to the user are constructed under this.
* [graph_config](game_config.txt) - General parameters for the application (log levels, steps per game, etc.)
* [graph_config](graph_config.txt) -
 A config files used by all the graphs when they are loaded.
 Parameters about the structure of the graphs

## Kivy flow
When setting up the game we need to load all the game screen. Each screen consists of three objects:
1) A kivy screen object. Each screen is independent from the other. The game moves between the screens as the game progresses.
2) A display object. These classes are none kivy objects that connect the screen objects to the kivy layouts
3) A kivy layout. The layout holds all the widgets that are displayed on the screen.
We load the objects in sequence: Screen -> Display -> Layout


## Back-end
### Basic infrastructure
All graphs used by the program will follow a standard build style for information graphs.
A graph is composed of a list of nodes, each node hold personal parameters, such as color, coordinates etc. and a list of connections - neighbors.
The graphs used in the program are stored under the GraphObject class and would be referenced as such from this point forward.
The graph_config file will hold any and all parameters regarding the functionality of the program: button actions, questions to use, graphs etc.

## Data Collection
#### Reading live data from graph
At every given time we track how much of the graph the user has seen so far. We do not account for memory as we try to give an optimal view of the graph
as seen by the user. The data is saved using a standard Graph Object, like the one used in the actual graph.
The only difference is the fact that our graph dynamically changes as time progresses.
After each step done by the user we pass the information seen on screen back to the db. This information is passed via a dictionary object.
The dictionary contains three fields - two list and a metadata class. One list contains all nodes in the current view and the other contains all edges
in view. An edge is represented by a tuple of two nodes. In case we do not directly see the nodes of the edge, imaginary nodes are created.
These imaginary node are represented like normal node, except for having “is_real” flag set to false and not having a representation in the node
list passed from the view. The metadata class holds information needed for post analysis of the data.

## Q Learning
We use Q-learning algorithms to allow a machine to learn the graphs and to understand the principles behind them. Running multiple episodes allow us
to see how the machine learns and improves over time. By modifying the learning factor for the machine we can simulate the effectiveness
of learning an thus create a correlation between the learning curve and the learning factor, e.g. curiosity.

