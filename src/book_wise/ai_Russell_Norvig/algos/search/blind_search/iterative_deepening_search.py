import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))

from src.book_wise.ai_Russell_Norvig.algos.search.blind_search import (
    depth_limited_search,
)
from src.book_wise.ai_Russell_Norvig.base_classes.problem import Problem
from src.book_wise.ai_Russell_Norvig.constants import CUTOFF


def iterative_deepening_search(problem: Problem, limit: float = float("inf")):
    i = 0
    while i <= limit:
        result = depth_limited_search(problem, i)
        if result != CUTOFF:
            return result

        i += 1
