import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))


import heapq
from src.book_wise.ai_Russell_Norvig.algos.search.heuristic_search.best_first_search import (
    best_first_search,
)
from src.book_wise.ai_Russell_Norvig.base_classes.node import Node
from src.book_wise.ai_Russell_Norvig.base_classes.problem import Problem
from src.book_wise.ai_Russell_Norvig.constants import FAILURE
from src.book_wise.ai_Russell_Norvig.utils import child_node, solution


def a_star_search(problem: Problem):
    start_node = Node(problem.initial_state, None, None, 0)

    if problem.goal_test(start_node.state):
        return solution(start_node)

    # Priority queue ordered by f(n) = g(n) + h(n)
    frontier = [(problem.heuristic(start_node.state), start_node)]
    heapq.heapify(frontier)

    explored = dict()  # {state: path_cost}

    while len(frontier) > 0:
        f, current = heapq.heappop(frontier)

        if problem.goal_test(current.state):
            return solution(current)

        # If this state has already been explored with a lower cost, skip
        if (
            any(n.state == current.state for n in explored)
            and explored[current] <= current.path_cost
        ):
            continue

        explored[current] = current.path_cost

        for action in problem.actions(current.state):
            child = child_node(problem, current, action)
            f_child = child.path_cost + problem.heuristic(child.state)

            # Check if child.state was already explored with a lower path_cost
            if (
                any(n.state == child.state for n in explored)
                or explored[child] > child.path_cost
            ):
                heapq.heappush(frontier, (f_child, child))

    return FAILURE  # No solution found


# A* Search using general best first search
a_star_search_alt = lambda problem: best_first_search(
    problem,
    f=lambda n: n.path_cost + problem.heuristic(n.state),
)
