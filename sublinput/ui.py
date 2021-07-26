import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

pygame.init()
pygame.display.init()

HEIGHT = 24
WIDTH = 480

WHITE = (255,) * 3
BLACK = (0,) * 3
ALPHA = (0,) * 4

SCREEN_TEXT_OFFSET = 5

ICON = pygame.Surface((64, 64), pygame.SRCALPHA)
ICON.fill(ALPHA)

FONT = pygame.font.SysFont('Consolas', 16)


class InputBoxScreen:

    def __init__(self) -> None:
        self.screen = None
        self.is_running = True
        self.result_value = ''

    def __enter__(self):
        pygame.display.init()
        return self

    def __call__(self, __prompt: str) -> str:
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(__prompt)
        pygame.display.set_icon(ICON)

        while self.is_running:
            self.handle_event(pygame.event.wait())
            self.draw()

        print(f"{__prompt}{self.result_value}")
        return self.result_value

    def __exit__(self, exc_type, exc_val, exc_tb):
        pygame.display.quit()

        if exc_type:
            raise

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False
            return

        if event.type == pygame.TEXTINPUT:
            self.result_value += event.text
            return

        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_BACKSPACE:
            self.result_value = self.result_value[:-1]
            return

        if event.key == pygame.K_RETURN:
            self.is_running = False
            return

    def draw(self):
        self.screen.fill(BLACK)
        text = FONT.render(self.result_value, True, WHITE)

        text_rect = text.get_rect()

        text_rect.top = SCREEN_TEXT_OFFSET

        if text_rect.width < (WIDTH - SCREEN_TEXT_OFFSET):
            text_rect.left = SCREEN_TEXT_OFFSET
        else:
            text_rect.right = WIDTH - SCREEN_TEXT_OFFSET

        self.screen.blit(text, text_rect)
        pygame.display.update()


def main():
    with InputBoxScreen() as input_box_demo:
        input_box_demo("Demo: ")


if __name__ == '__main__':
    main()
