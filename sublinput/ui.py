"""Handle the whole user interface of the sublinput package."""

from __future__ import annotations

import os
from typing import Union, Tuple, Optional, Any

# Hides the pygame support message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']: str = "hide"

import pygame

Color = Union[Tuple[int, int, int], Tuple[int, int, int, int]]

pygame.init()
pygame.display.init()

HEIGHT: int = 24
WIDTH: int = 480

WHITE: Color = (255,) * 3
BLACK: Color = (0,) * 3
ALPHA: Color = (0,) * 4

SCREEN_TEXT_OFFSET: int = 5

ICON: pygame.Surface = pygame.Surface((64, 64), pygame.SRCALPHA)
ICON.fill(ALPHA)

FONT: pygame.font.SysFont = pygame.font.SysFont('Consolas', 16)


class InputBoxScreen:

    def __init__(self) -> None:
        """Initialize the input box screen."""
        self.screen: Optional[pygame.display] = None
        self.is_running: bool = True
        self.result_value: str = ''

    def __enter__(self) -> InputBoxScreen:
        """Initialize pygame display."""
        pygame.display.init()
        return self

    def __call__(self, __prompt: str) -> str:
        """Create a screen and get a value from the user."""
        self.screen: pygame.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(__prompt)
        pygame.display.set_icon(ICON)

        while self.is_running:
            self.handle_event(pygame.event.wait())
            self.draw()

        print(f"{__prompt}{self.result_value}")
        return self.result_value

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """QUit pygame display and raise possible exception."""
        pygame.display.quit()

        if exc_type:
            raise

    def handle_event(self, event: pygame.Event) -> None:
        """Handle event from the user."""
        if event.type == pygame.QUIT:
            self.is_running: bool = False
            return

        if event.type == pygame.TEXTINPUT:
            self.result_value += event.text
            return

        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_BACKSPACE:
            self.result_value: str = self.result_value[:-1]
            return

        if event.key == pygame.K_RETURN:
            self.is_running: bool = False
            return

    def draw(self) -> None:
        """Render the user text on the screen."""
        self.screen.fill(BLACK)
        text: pygame.Surface = FONT.render(self.result_value, True, WHITE)
        text_rect: pygame.Rect = text.get_rect()

        text_rect.top = SCREEN_TEXT_OFFSET

        # Scroll when value length is higher then screen size
        if text_rect.width < (WIDTH - SCREEN_TEXT_OFFSET):
            text_rect.left = SCREEN_TEXT_OFFSET
        else:
            text_rect.right = WIDTH - SCREEN_TEXT_OFFSET

        self.screen.blit(text, text_rect)
        pygame.display.update()


def main() -> None:
    """A Demo of the InputBoxScreen class."""
    with InputBoxScreen() as input_box_demo:
        input_box_demo("Demo: ")


if __name__ == '__main__':
    main()
