from sublinput.ui import InputBoxScreen
import builtins


def new_input(__prompt='') -> str:
    with InputBoxScreen() as input_box:
        return input_box(__prompt)


builtins.input = new_input
