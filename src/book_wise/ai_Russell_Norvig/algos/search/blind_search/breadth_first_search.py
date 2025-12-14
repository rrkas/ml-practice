import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))

from queue import Queue
from src.book_wise.ai_Russell_Norvig.constants import FAILURE
from src.book_wise.ai_Russell_Norvig.base_classes.node import Node
from src.book_wise.ai_Russell_Norvig.base_classes.problem import Problem
from src.book_wise.ai_Russell_Norvig.utils import child_node, solution


def breadth_first_search(problem: Problem):
    node = Node(problem.initial_state, None, None, 0)

    if problem.goal_test(node.state):
        return solution(node)

    frontier = Queue()
    explored = set()

    frontier.put(node)

    while True:
        if frontier.empty():
            return FAILURE

        node = frontier.get()
        explored.add(node)

        for action in problem.actions(node.state):
            child = child_node(problem, node, action)

            if not any([n.state == child.state for n in frontier.queue]) and not any(
                [n.state == child.state for n in explored]
            ):
                if problem.goal_test(child.state):
                    return solution(child)

                frontier.put(child)
