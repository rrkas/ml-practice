import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))

import heapq
from src.book_wise.ai_Russell_Norvig.constants import FAILURE
from src.book_wise.ai_Russell_Norvig.base_classes.node import Node
from src.book_wise.ai_Russell_Norvig.base_classes.problem import Problem
from src.book_wise.ai_Russell_Norvig.utils import child_node, solution


def uniform_cost_search(problem: Problem):
    node = Node(problem.initial_state, None, None, 0)

    if problem.goal_test(node.state):
        return solution(node)

    frontier = [(node.path_cost, node)]
    explored = set()

    heapq.heapify(frontier)

    while True:
        if len(frontier) == 0:
            return FAILURE

        path_cost, node = frontier.pop(0)

        if problem.goal_test(node.state):
            return solution(node)

        explored.add(node)
        for action in problem.actions(node.state):
            child = child_node(problem, node, action)

            if not any(
                [n.state == child.state for (path_cost, n) in frontier]
            ) and not any([n.state == child.state for n in explored]):
                frontier.append((child.path_cost, child))
                heapq.heapify(frontier)
            else:
                for idx, (path_cost, n) in enumerate(frontier):
                    if n.state == child.state and path_cost > child.path_cost:
                        frontier[idx] = (child.path_cost, child)
                        heapq.heapify(frontier)
