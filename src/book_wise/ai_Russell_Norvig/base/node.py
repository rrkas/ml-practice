from book_wise.ai_Russell_Norvig.base.state import State


class Node:
    def __init__(self, state: State, parent, action, path_cost):
        # the state in the state space to which the node corresponds
        self.state: State = state

        # the node in the search tree that generated this node
        self.parent = parent

        # the action that was applied to the parent to generate the node
        self.action = action

        """
            the cost, traditionally denoted by g(n), of the path
            from the initial state to the node, as indicated
            by the parent pointers
        """
        self.path_cost = path_cost

    def __lt__(self, __o):
        return self.path_cost < __o.path_cost

    def __str__(self):
        return (
            "<Node "
            + f"state: {self.state} "
            + f"parent: {self.parent} "
            + f"action: {self.action} "
            + f"path_cost: {self.path_cost} "
            + ">"
        )

    def __repr__(self) -> str:
        return str(self)
