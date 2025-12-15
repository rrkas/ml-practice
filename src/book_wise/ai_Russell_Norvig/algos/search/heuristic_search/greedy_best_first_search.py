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


def greedy_best_first_search(problem: Problem):
    node = Node(problem.initial_state, None, None, 0)

    if problem.goal_test(node.state):
        return solution(node)

    # Priority queue ordered by heuristic cost
    frontier = [(problem.heuristic(node.state), node)]
    heapq.heapify(frontier)

    explored = set()

    while len(frontier) > 0:
        _, node = heapq.heappop(frontier)

        if problem.goal_test(node.state):
            return solution(node)

        explored.add(node)

        for action in problem.actions(node.state):
            child = child_node(problem, node, action)
            h_cost = problem.heuristic(child.state)

            # Add child only if it's not in frontier or explored
            in_frontier = any(n.state == child.state for _, n in frontier)
            in_explored = any(n.state == child.state for n in explored)

            if not in_frontier and not in_explored:
                heapq.heappush(frontier, (h_cost, child))
            else:
                # Optional: If it's in the frontier but has a
                # better heuristic, replace it
                for idx, (old_cost, old_node) in enumerate(frontier):
                    if old_node.state == child.state and h_cost < old_cost:
                        frontier[idx] = (h_cost, child)
                        heapq.heapify(frontier)
                        break

    return FAILURE  # No solution found


# Greedy Best-First Search using general best first search
greedy_best_first_search_alt = lambda problem: best_first_search(
    problem, f=lambda n: problem.heuristic(n.state)
)
