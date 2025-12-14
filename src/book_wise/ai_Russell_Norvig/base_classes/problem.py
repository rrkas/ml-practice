import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))

from src.book_wise.ai_Russell_Norvig.base_classes.state import State


class Problem:
    def __init__(self, initial_state: State):
        self.initial_state = initial_state
        # 1. initial_state: The initial state that the agent starts in.

    def actions(self, state: State):
        """
        2. A description of the possible actions available to the agent.
        Given a particular state s, ACTIONS(s) returns the set of actions
        that can be executed in s.
        """
        raise NotImplementedError()

    def result(self, state: State, action):
        """
        3. A description of what each action does; the formal name for this
        is the transition model, specified by a function RESULT(s, a) that
        returns the state that results from doing action a in state s.
        """
        raise NotImplementedError()

    def goal_test(self, state: State):
        # 4. The goal test, which determines whether a given state is a goal state.
        raise NotImplementedError()

    def step_cost(self, state: State, action, new_state: State):
        """
        5. The step cost of taking action
        a in state s to reach state s' is denoted by c(s, a, s').
        """
        raise NotImplementedError()

    def heuristic(self, state: State):
        """
        Returns estimated cost from state to goal.
        """
        raise NotImplementedError()
