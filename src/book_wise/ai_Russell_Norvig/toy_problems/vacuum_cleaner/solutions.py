import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))

from src.book_wise.ai_Russell_Norvig.algos.search.blind_search.breadth_first_search import (
    breadth_first_search,
)
from src.book_wise.ai_Russell_Norvig.base_classes.node import Node
from src.book_wise.ai_Russell_Norvig.toy_problems.vacuum_cleaner.vacuum_problem import (
    VacuumProblem,
)
from src.book_wise.ai_Russell_Norvig.toy_problems.vacuum_cleaner.vacuum_state_action import (
    init_state,
)
from src.book_wise.ai_Russell_Norvig.utils import child_node


problem = VacuumProblem(init_state)
path = breadth_first_search(problem)
print(path)

node = Node(init_state, None, None, 0)
print(node)
for a in path:
    new_node = child_node(problem, node, a)
    print(a, new_node.state, new_node.path_cost, new_node)
    node = new_node
