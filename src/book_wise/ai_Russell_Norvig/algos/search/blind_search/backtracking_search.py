import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))

from src.book_wise.ai_Russell_Norvig.constants import FAILURE
from src.book_wise.ai_Russell_Norvig.base_classes.node import Node
from src.book_wise.ai_Russell_Norvig.base_classes.problem import Problem
from src.book_wise.ai_Russell_Norvig.utils import child_node, solution


def backtrack(problem: Problem, node: Node, explored: set):
    if problem.goal_test(node.state):
        return solution(node)

    explored.add(node)

    for action in problem.actions(node.state):
        child = child_node(problem, node, action)
        if not any([child.state == n.state for n in explored]):
            result = backtrack(child, explored)
            if result is not None:
                return result

    # Optional: allow revisiting for other paths (depends on problem)
    explored.remove(node)
    return FAILURE


def backtracking_search(problem: Problem):
    root = Node(problem.initial_state, None, None, 0)
    return backtrack(problem, root, set())
