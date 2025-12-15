import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))


from src.book_wise.ai_Russell_Norvig.base_classes.state import State


vacuumActions = ["L", "R", "S"]  # L: Left, R: Right, S: Suck
vacuumSquareState = ["D", "C"]  # D: Dirty, C: Clean


class VacuumState(State):
    def __init__(self, squareA, squareB, currLoc):
        self.squares = {}
        self.squares["A"] = squareA
        self.squares["B"] = squareB
        self.currLoc = currLoc

    def __str__(self):
        return "<VacuumState " + f"squares={self.squares} " + f"currLoc={self.currLoc}>"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __o: object) -> bool:
        return str(self) == str(__o)

    def copy(self):
        return VacuumState(
            self.squares["A"],
            self.squares["B"],
            self.currLoc,
        )


init_state = VacuumState("D", "D", "A")
