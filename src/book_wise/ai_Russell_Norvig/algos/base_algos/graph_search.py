import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))

from src.book_wise.ai_Russell_Norvig.constants import FAILURE
from src.book_wise.ai_Russell_Norvig.base_classes.node import Node
from src.book_wise.ai_Russell_Norvig.base_classes.problem import Problem
from src.book_wise.ai_Russell_Norvig.utils import solution


def graph_search(problem: Problem):
    frontier = [Node(problem.initial_state, None, None, 0)]
    explored = set()

    while True:
        if len(frontier) == 0:
            return FAILURE

        node: Node = frontier.pop()

        if problem.goal_test(node.state):
            return solution(node)

        explored.add(node)

        for action in problem.actions(node.state):
            new_state = problem.result(node.state, action)
            path_cost = node.path_cost + problem.step_cost(
                node.state,
                action,
                new_state,
            )
            new_node = Node(new_state, node, action, path_cost)

            if new_node not in frontier and new_node not in explored:
                frontier.append(new_node)
