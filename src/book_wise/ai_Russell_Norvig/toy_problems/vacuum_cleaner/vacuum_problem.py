import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))


from src.book_wise.ai_Russell_Norvig.base_classes.problem import Problem
from src.book_wise.ai_Russell_Norvig.toy_problems.vacuum_cleaner.vacuum_state_action import (
    VacuumState,
)


class VacuumProblem(Problem):
    def __init__(self, initial_state: VacuumState):
        self.initial_state = initial_state

    def step_cost(self, state: VacuumState, action: str, new_state: VacuumState):
        return (
            int(state.squares[state.currLoc] == "D" and action == "S")
            + int(state.currLoc == "A" and action == "R")
            + int(state.currLoc == "B" and action == "L")
        )

    def result(self, state: VacuumState, action: str):
        state = state.copy()

        state.currLoc = {
            "L": "A",
            "R": "B",
        }.get(action, state.currLoc)
        state.squares[state.currLoc] = {"S": "C"}.get(
            action,
            state.squares[state.currLoc],
        )
        return state

    def actions(self, state: VacuumState):
        actions = []

        if state.squares[state.currLoc] == "D":
            actions.append("S")

        if state.currLoc == "A":
            actions.append("R")

        if state.currLoc == "B":
            actions.append("L")

        return actions

    def goal_test(self, state: VacuumState):
        return all([v == "C" for v in state.squares.values()])
