import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))

from src.book_wise.ai_Russell_Norvig.constants import CUTOFF, FAILURE
from src.book_wise.ai_Russell_Norvig.base_classes.node import Node
from src.book_wise.ai_Russell_Norvig.base_classes.problem import Problem
from src.book_wise.ai_Russell_Norvig.utils import child_node, solution


def depth_limited_search(problem: Problem, limit: int):
    return recursive_dls(
        Node(problem.initial_state, None, None, 0),
        problem,
        limit,
    )


def recursive_dls(node: Node, problem: Problem, limit: int):
    if problem.goal_test(node.state):
        return solution(node)

    elif limit == 0:
        return CUTOFF

    else:
        cutoff_occurred = False
        for action in problem.actions(node.state):
            child = child_node(problem, node, action)
            result = recursive_dls(child, problem, limit - 1)
            if result == CUTOFF:
                cutoff_occurred = True
            elif result is not None:
                return result

        if cutoff_occurred:
            return CUTOFF
        else:
            return FAILURE
