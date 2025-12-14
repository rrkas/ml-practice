import sys, pathlib

__root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(__root_path))


class State:
    def copy(self):
        raise NotImplementedError()
