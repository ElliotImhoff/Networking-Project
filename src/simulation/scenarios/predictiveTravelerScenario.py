from src.graph.graph import Graph
from src.network.network import Network
from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from src.simulation.scenarioTypes.predictiveScenario import PredictiveScenario


class PredictiveTravelerScenario:
    def __init__(self, presetNetwork, iterations: int = None) -> None:
        self.network = presetNetwork.network
        self.travelers = presetNetwork.travelers
        self.iterations = iterations
        if iterations is None:
            self.iterations = 3
        self.scenario = PredictiveScenario(
            self.network, self.travelers, self.iterations)

    def run(self):
        self.scenario.run()

    def getLogs(self):
        return self.scenario.getLogs()
