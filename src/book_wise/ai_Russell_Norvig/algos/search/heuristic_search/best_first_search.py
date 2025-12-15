import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))

import heapq

from src.book_wise.ai_Russell_Norvig.base_classes.node import Node
from src.book_wise.ai_Russell_Norvig.base_classes.problem import Problem
from src.book_wise.ai_Russell_Norvig.constants import FAILURE
from src.book_wise.ai_Russell_Norvig.utils import child_node, solution


def best_first_search(problem: Problem, f):
    node = Node(problem.initial_state, None, None, 0)

    if problem.goal_test(node.state):
        return solution(node)

    frontier = [(f(node), node)]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        _, node = heapq.heappop(frontier)

        if problem.goal_test(node.state):
            return solution(node)

        explored.add(node)

        for action in problem.actions(node.state):
            child = child_node(problem, node, action)
            if all(n.state != child.state for n in explored) and all(
                n.state != child.state for _, n in frontier
            ):
                heapq.heappush(frontier, (f(child), child))
            else:
                # Optional: Replace in frontier if better
                for i, (old_f, old_node) in enumerate(frontier):
                    if old_node.state == child.state and f(child) < old_f:
                        frontier[i] = (f(child), child)
                        heapq.heapify(frontier)
                        break

    return FAILURE
