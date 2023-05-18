import networkx as nx
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.widgets import *
import sys
from _1_BFS import Graph_bfs
from _2_DFS import Graph_dfs
from _3_DLS import Graph_dls
from _4_IDS import Graph_ids
from _5_UCS import Graph_ucs
from _6_BDS import Graph_bds
from _7_BestFS import Graph_bestfs
from _8_AStar import Graph_astar
from _9_SimulatedAnnealing import Graph_SimulatedAnnealing
from _10_AlphaBeta import Graph_AlphaBeta

DG = nx.DiGraph()
G = nx.Graph()
Node1_arr = ['A'] * 30
Node2_arr = ['A'] * 30
Goal_list = []
limit = 0


class Ui_AISearchingTechniquesMainWindow(object):
    counter = 0
    counterG = 0
    EdgeWeight_arr = [1] * 30
    HeuristicDict = dict()
    H = {}

    def GeneratePathClicked(self):
        original_stdout = sys.stdout

        with open('test.txt', 'w') as f:
            sys.stdout = f
            searchType = str(self.SearchTypecomboBox.currentText())
            graphType = str(self.GraphTypecomboBox.currentText())
            directed = graphType != "Undirectd Graph"

            graph_classes = {
                "BFS": Graph_bfs,
                "DFS": Graph_dfs,
                "UCS": Graph_ucs,
                "DLS": Graph_dls,
                "IDS": Graph_ids,
                "BDS": Graph_bds,
                "Bfs": Graph_bestfs,
                "A*": Graph_astar,
                "SAS": Graph_SimulatedAnnealing,
                "ABS": Graph_AlphaBeta
            }

            graph_class = graph_classes.get(searchType)
            if graph_class:
                graph = graph_class(directed=directed)
                if searchType in ["UCS", "A*", "Bfs", "SAS", "ABS"]:
                    for i in range(0, self.counter):
                        graph.add_edge(Node1_arr[i], Node2_arr[i], int(
                            self.EdgeWeight_arr[i]))
                else:
                    for i in range(0, self.counter):
                        graph.add_edge(Node1_arr[i], Node2_arr[i])

                start = self.StartNode_input.text()
                goals = Goal_list
                if searchType in ["A*", "Bfs"]:
                    graph.set_heuristic(self.HeuristicDict)

                if searchType in ["UCS", "A*"]:
                    traced_path, goals, cost = graph.search(start, goals)
                    if traced_path:
                        print('Path:', end=' ')
                        graph.print_path(traced_path)
                        print('\nCost:', cost)
                        print()
                elif searchType in ["DLS", "IDS"]:
                    traced_path, goals = graph.search(
                        start, goals, limit)
                    if traced_path:
                        print('Path:', end=' ')
                        graph.print_path(traced_path)
                        print()
                else:
                    traced_path, goals = graph.search(start, goals)
                    if traced_path:
                        print('Path:', end=' ')
                        graph.print_path(traced_path)
                        print()

        sys.stdout = original_stdout  # Reset the standard output to its original value

        with open("test.txt") as f:
            contents = f.read()

        self.TheResult_Label.setText(contents)

    def GenerateGraphClicked(self):
        if self.GraphTypecomboBox.currentText() == "Undirectd Graph":
            pos = nx.spring_layout(G, dim=2)
            nx.draw(G, pos, with_labels=True, node_size=1500)
            nx.draw_networkx_edge_labels(
                G, pos, font_size=26, edge_labels=nx.get_edge_attributes(G, 'weight'))
            plt.show()
        elif self.GraphTypecomboBox.currentText() == "Directed Graph":
            pos = nx.spring_layout(DG)
            nx.draw(DG, pos, with_labels=True, node_size=1500)
            nx.draw_networkx_edge_labels(
                DG, pos, font_size=26, edge_labels=nx.get_edge_attributes(DG, 'weight'))
            plt.show()

    def AddNodeClicked(self):
        N1 = self.Node1_input.text()
        N2 = self.Node2_input.text()
        W = self.EdgeWieght_input.text()
        G.add_edge(N1, N2, weight=W)
        DG.add_edge(N1, N2, weight=W)
        Node1_arr[self.counter] = N1
        Node2_arr[self.counter] = N2
        self.EdgeWeight_arr[self.counter] = W
        self.counter = self.counter + 1
        self.Node1_input.clear()
        self.Node2_input.clear()
        self.EdgeWieght_input.clear()

    def HeuristicPushed(self):
        InputHeuristic = int(self.NodeHeuristic_input.text())
        InputNodeH = self.Node_Input.text()
        self.H[self.Node_Input.text()] = self.NodeHeuristic_input.text()
        self.HeuristicDict.update({InputNodeH: InputHeuristic})
        self.Node_Input.clear()
        self.NodeHeuristic_input.clear()

    def SubmitClicked(self):
        G = self.GoalNode_input.text()
        Goal_list.append(G)
        self.GoalNode_input.clear()

    def LimitClicked(self):
        global limit
        limit = int(self.Limit_input.text())
        self.Limit_input.clear()

    def setupUi(self, AISearchingTechniquesMainWindow):
        AISearchingTechniquesMainWindow.setObjectName(
            "AISearchingTechniquesMainWindow")
        AISearchingTechniquesMainWindow.resize(779, 790)
        self.centralwidget = QtWidgets.QWidget(AISearchingTechniquesMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SearchTypecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SearchTypecomboBox.setGeometry(QtCore.QRect(630, 50, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SearchTypecomboBox.setFont(font)
        self.SearchTypecomboBox.setObjectName("SearchTypecomboBox")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.GenerateGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateGraphButton.setGeometry(QtCore.QRect(630, 240, 131, 31))
        self.GenerateGraphButton.setObjectName("GenerateGraphButton")
        self.GenerateGraphButton.clicked.connect(self.GenerateGraphClicked)
        self.Node1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node1_input.setGeometry(QtCore.QRect(26, 48, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node1_input.setFont(font)
        self.Node1_input.setText("")
        self.Node1_input.setObjectName("Node1_input")
        self.Node2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node2_input.setGeometry(QtCore.QRect(26, 101, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node2_input.setFont(font)
        self.Node2_input.setObjectName("Node2_input")
        self.Node1Label = QtWidgets.QLabel(self.centralwidget)
        self.Node1Label.setGeometry(QtCore.QRect(26, 25, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node1Label.setFont(font)
        self.Node1Label.setObjectName("Node1Label")
        self.Node2Label = QtWidgets.QLabel(self.centralwidget)
        self.Node2Label.setGeometry(QtCore.QRect(26, 78, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node2Label.setFont(font)
        self.Node2Label.setObjectName("Node2Label")
        self.EdgeWieghtLabel = QtWidgets.QLabel(self.centralwidget)
        self.EdgeWieghtLabel.setGeometry(QtCore.QRect(26, 131, 72, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.EdgeWieghtLabel.setFont(font)
        self.EdgeWieghtLabel.setObjectName("EdgeWieghtLabel")
        self.EdgeWieght_input = QtWidgets.QLineEdit(self.centralwidget)
        self.EdgeWieght_input.setGeometry(QtCore.QRect(26, 157, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.EdgeWieght_input.setFont(font)
        self.EdgeWieght_input.setObjectName("EdgeWieght_input")
        self.AddNodesButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddNodesButton.setGeometry(QtCore.QRect(26, 189, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddNodesButton.setFont(font)
        self.AddNodesButton.setObjectName("AddNodesButton")
        self.AddNodesButton.clicked.connect(self.AddNodeClicked)
        self.TheResult_Label = QtWidgets.QLabel(self.centralwidget)
        self.TheResult_Label.setGeometry(QtCore.QRect(10, 280, 751, 481))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TheResult_Label.setFont(font)
        self.TheResult_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.TheResult_Label.setLineWidth(2)
        self.TheResult_Label.setText("")
        self.TheResult_Label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.TheResult_Label.setObjectName("TheResult_Label")
        self.GeneratePathButton = QtWidgets.QPushButton(self.centralwidget)
        self.GeneratePathButton.setGeometry(QtCore.QRect(460, 240, 131, 31))
        self.GeneratePathButton.setObjectName("GeneratePathButton")
        self.GeneratePathButton.clicked.connect(self.GeneratePathClicked)
        self.TheResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.TheResultLabel.setGeometry(QtCore.QRect(10, 230, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TheResultLabel.setFont(font)
        self.TheResultLabel.setObjectName("TheResultLabel")
        self.Node_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node_Input.setGeometry(QtCore.QRect(227, 49, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node_Input.setFont(font)
        self.Node_Input.setText("")
        self.Node_Input.setObjectName("Node_Input")
        self.NodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.NodeLabel.setGeometry(QtCore.QRect(227, 26, 33, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeLabel.setFont(font)
        self.NodeLabel.setObjectName("NodeLabel")
        self.NodeHeuristicLabel = QtWidgets.QLabel(self.centralwidget)
        self.NodeHeuristicLabel.setGeometry(QtCore.QRect(227, 78, 82, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeHeuristicLabel.setFont(font)
        self.NodeHeuristicLabel.setObjectName("NodeHeuristicLabel")
        self.NodeHeuristic_input = QtWidgets.QLineEdit(self.centralwidget)
        self.NodeHeuristic_input.setGeometry(QtCore.QRect(227, 101, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeHeuristic_input.setFont(font)
        self.NodeHeuristic_input.setObjectName("NodeHeuristic_input")
        self.AddNodeHeuristicButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddNodeHeuristicButton.setGeometry(
            QtCore.QRect(227, 130, 117, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddNodeHeuristicButton.setFont(font)
        self.AddNodeHeuristicButton.setObjectName("AddNodeHeuristicButton")
        self.AddNodeHeuristicButton.clicked.connect(self.HeuristicPushed)
        self.StartNode_input = QtWidgets.QLineEdit(self.centralwidget)
        self.StartNode_input.setGeometry(QtCore.QRect(430, 49, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.StartNode_input.setFont(font)
        self.StartNode_input.setText("")
        self.StartNode_input.setObjectName("StartNode_input")
        self.StartNodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.StartNodeLabel.setGeometry(QtCore.QRect(430, 26, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.StartNodeLabel.setFont(font)
        self.StartNodeLabel.setObjectName("StartNodeLabel")
        self.GoalNodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.GoalNodeLabel.setGeometry(QtCore.QRect(430, 77, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GoalNodeLabel.setFont(font)
        self.GoalNodeLabel.setObjectName("GoalNodeLabel")
        self.GoalNode_input = QtWidgets.QLineEdit(self.centralwidget)
        self.GoalNode_input.setGeometry(QtCore.QRect(430, 100, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GoalNode_input.setFont(font)
        self.GoalNode_input.setObjectName("GoalNode_input")
        self.Limit_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Limit_input.setGeometry(QtCore.QRect(630, 155, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Limit_input.setFont(font)
        self.Limit_input.setText("")
        self.Limit_input.setObjectName("Limit_input")
        self.LimitLabel = QtWidgets.QLabel(self.centralwidget)
        self.LimitLabel.setGeometry(QtCore.QRect(630, 135, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LimitLabel.setFont(font)
        self.LimitLabel.setObjectName("LimitLabel")
        self.LimitButton = QtWidgets.QPushButton(self.centralwidget)
        self.LimitButton.setGeometry(QtCore.QRect(630, 185, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LimitButton.setFont(font)
        self.LimitButton.setObjectName("LimitButton")
        self.LimitButton.clicked.connect(self.LimitClicked)
        self.GraphTypecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.GraphTypecomboBox.setGeometry(QtCore.QRect(630, 100, 122, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GraphTypecomboBox.setFont(font)
        self.GraphTypecomboBox.setObjectName("GraphTypecomboBox")
        self.GraphTypecomboBox.addItem("")
        self.GraphTypecomboBox.addItem("")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(430, 135, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setObjectName("SubmitButton")
        self.SubmitButton.clicked.connect(self.SubmitClicked)
        AISearchingTechniquesMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AISearchingTechniquesMainWindow)
        self.statusbar.setObjectName("statusbar")
        AISearchingTechniquesMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AISearchingTechniquesMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AISearchingTechniquesMainWindow)

    def retranslateUi(self, AISearchingTechniquesMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AISearchingTechniquesMainWindow.setWindowTitle(
            _translate("AISearchingTechniquesMainWindow", "AI Searching Techniques"))
        self.SearchTypecomboBox.setCurrentText(
            _translate("AISearchingTechniquesMainWindow", "BFS"))
        self.SearchTypecomboBox.setItemText(
            0, _translate("AISearchingTechniquesMainWindow", "BFS"))
        self.SearchTypecomboBox.setItemText(
            1, _translate("AISearchingTechniquesMainWindow", "DFS"))
        self.SearchTypecomboBox.setItemText(
            2, _translate("AISearchingTechniquesMainWindow", "UCS"))
        self.SearchTypecomboBox.setItemText(
            3, _translate("AISearchingTechniquesMainWindow", "DLS"))
        self.SearchTypecomboBox.setItemText(
            4, _translate("AISearchingTechniquesMainWindow", "IDS"))
        self.SearchTypecomboBox.setItemText(
            5, _translate("AISearchingTechniquesMainWindow", "BDS"))
        self.SearchTypecomboBox.setItemText(
            6, _translate("AISearchingTechniquesMainWindow", "A*"))
        self.SearchTypecomboBox.setItemText(
            7, _translate("AISearchingTechniquesMainWindow", "Bfs"))
        self.SearchTypecomboBox.setItemText(
            8, _translate("AISearchingTechniquesMainWindow", "SAS"))
        self.SearchTypecomboBox.setItemText(
            9, _translate("AISearchingTechniquesMainWindow", "ABS"))
        self.GenerateGraphButton.setText(_translate(
            "AISearchingTechniquesMainWindow", "Generate Graph"))
        self.Node1Label.setText(_translate(
            "AISearchingTechniquesMainWindow", "Node 1"))
        self.Node2Label.setText(_translate(
            "AISearchingTechniquesMainWindow", "Node 2"))
        self.EdgeWieghtLabel.setText(_translate(
            "AISearchingTechniquesMainWindow", "Edge Wieght"))
        self.AddNodesButton.setText(_translate(
            "AISearchingTechniquesMainWindow", "Add Nodes"))
        self.TheResult_Label.setWhatsThis(_translate("AISearchingTechniquesMainWindow",
                                                     "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.GeneratePathButton.setText(_translate(
            "AISearchingTechniquesMainWindow", "Generate Path"))
        self.TheResultLabel.setText(_translate(
            "AISearchingTechniquesMainWindow", "The Result"))
        self.NodeLabel.setText(_translate(
            "AISearchingTechniquesMainWindow", "Node "))
        self.NodeHeuristicLabel.setText(_translate(
            "AISearchingTechniquesMainWindow", "Node Heuristic"))
        self.AddNodeHeuristicButton.setText(_translate(
            "AISearchingTechniquesMainWindow", "Add Node Heuristic"))
        self.StartNodeLabel.setText(_translate(
            "AISearchingTechniquesMainWindow", "Start Node"))
        self.GoalNodeLabel.setText(_translate(
            "AISearchingTechniquesMainWindow", "Goal Nodes"))
        self.LimitLabel.setText(_translate(
            "AISearchingTechniquesMainWindow", "Limit"))
        self.LimitButton.setText(_translate(
            "AISearchingTechniquesMainWindow", "Add Limit"))
        self.GraphTypecomboBox.setCurrentText(_translate(
            "AISearchingTechniquesMainWindow", "Undirectd Graph"))
        self.GraphTypecomboBox.setItemText(0, _translate(
            "AISearchingTechniquesMainWindow", "Undirectd Graph"))
        self.GraphTypecomboBox.setItemText(1, _translate(
            "AISearchingTechniquesMainWindow", "Directed Graph"))
        self.SubmitButton.setText(_translate(
            "AISearchingTechniquesMainWindow", "Submit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AISearchingTechniquesMainWindow = QtWidgets.QMainWindow()
    ui = Ui_AISearchingTechniquesMainWindow()
    ui.setupUi(AISearchingTechniquesMainWindow)
    AISearchingTechniquesMainWindow.show()
    sys.exit(app.exec_())
