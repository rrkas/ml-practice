import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(__root_path))

from src.book_wise.ai_Russell_Norvig.base_classes.node import Node
from src.book_wise.ai_Russell_Norvig.base_classes.problem import Problem


def child_node(problem: Problem, parent: Node, action):
    new_state = problem.result(parent.state, action)

    return Node(
        state=new_state,
        parent=parent,
        action=action,
        path_cost=(
            parent.path_cost
            + problem.step_cost(
                parent.state,
                action,
                new_state,
            )
        ),
    )


def solution(node: Node):
    path = []

    while node.parent is not None:
        path.insert(0, node.action)
        node = node.parent

    return path
