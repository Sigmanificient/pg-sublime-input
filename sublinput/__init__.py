"""An input pygame alternative for sublime text users."""

from sublinput.ui import InputBoxScreen
import builtins


def new_input(__prompt: str ='') -> str:
    """A function that creates a new input box screen and return it's value."""
    with InputBoxScreen() as input_box:
        return input_box(__prompt)


builtins.input = new_input
