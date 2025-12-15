import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))


from src.book_wise.ai_Russell_Norvig.base_classes.node import Node
from src.book_wise.ai_Russell_Norvig.base_classes.problem import Problem
from src.book_wise.ai_Russell_Norvig.constants import FAILURE
from src.book_wise.ai_Russell_Norvig.utils import child_node, solution


def ida_star_search(problem: Problem):
    """
    Performs Iterative Deepening A* Search.
    Returns the solution as a list of actions, or None if no solution is found.
    """

    start_node = Node(problem.initial_state, None, None, 0)
    bound = problem.heuristic(start_node.state)

    while True:
        result = _ida_search(start_node, problem, bound)

        if isinstance(result, list):  # Found a solution
            return result

        if result == float("inf"):
            return FAILURE  # No solution

        bound = result  # Increase bound and try again


def _ida_search(node: Node, problem: Problem, bound: float):
    """
    Helper function for IDA* search.
    Returns either:
    - A solution path (list of actions), or
    - The next bound (float) to use in the next iteration
    """
    f = node.path_cost + problem.heuristic(node.state)

    if f > bound:
        return f

    if problem.goal_test(node.state):
        return solution(node)

    min_threshold = float("inf")
    for action in problem.actions(node.state):
        child = child_node(problem, node, action)
        result = _ida_search(child, problem, bound)

        if isinstance(result, list):
            return result  # Solution found

        if result < min_threshold:
            min_threshold = result

    return min_threshold
