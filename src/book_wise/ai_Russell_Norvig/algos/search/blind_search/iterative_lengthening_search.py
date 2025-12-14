import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))

import heapq
from src.book_wise.ai_Russell_Norvig.base_classes.node import Node
from src.book_wise.ai_Russell_Norvig.base_classes.problem import Problem
from src.book_wise.ai_Russell_Norvig.constants import FAILURE
from src.book_wise.ai_Russell_Norvig.utils import child_node, solution


def iterative_lengthening_search(problem: Problem):
    cost_limit = 0

    while True:
        result, new_cost_limit = uniform_cost_search_with_cost_limit(
            problem,
            cost_limit,
        )

        if result is not FAILURE:
            return result

        if new_cost_limit == float("inf"):
            return FAILURE

        cost_limit = new_cost_limit


def uniform_cost_search_with_cost_limit(problem: Problem, cost_limit: float):
    node = Node(problem.initial_state, None, None, 0)

    if problem.goal_test(node.state):
        return solution(node), cost_limit

    frontier = [(node.path_cost, node)]
    explored = set()
    heapq.heapify(frontier)
    next_cost_limit = float("inf")

    while frontier:
        path_cost, node = heapq.heappop(frontier)

        if path_cost > cost_limit:
            next_cost_limit = min(next_cost_limit, path_cost)
            continue

        if problem.goal_test(node.state):
            return solution(node), cost_limit

        explored.add(node)

        for action in problem.actions(node.state):
            child = child_node(problem, node, action)

            if not any(child.state == n.state for n in explored) and not any(
                n.state == child.state for _, n in frontier
            ):
                heapq.heappush(frontier, (child.path_cost, child))

    return FAILURE, next_cost_limit
