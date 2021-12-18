import pygame
from typing import Tuple, List
pygame.init()

class DrawInformation:
    """ Contains information and constants for drawing the visualization window """
    # Global color constants
    BLACK: Tuple[int, int, int] = 0, 0, 0
    WHITE: Tuple[int, int, int] = 255, 255, 255
    BLUE: Tuple[int, int, int] = 0, 0, 255
    RED: Tuple[int, int, int] = 255, 0, 0
    GREEN: Tuple[int, int, int] = 0, 255, 0
    BG_COLOR: Tuple[int, int, int] = WHITE

    GRADIENTS: List[Tuple[int, int, int]] = \
        [(128, 128, 128), (160, 160, 160), (192, 192, 192)]

    FONT = pygame.font.SysFont('comicsans', size=20)
    LARGE_FONT = pygame.font.SysFont('comicsans', size=30)

    # Dimensions of window
    width: int
    height: int
    # Total padding (left + right) of array elements from edge of window
    SIDE_PADDING: int = 100
    # Padding from top of the screen
    TOP_PADDING: int = 120

    def __init__(self, width: int, height: int, arr: List[int]) -> None:
        self.width = width
        self.height = height
        
        # Create Window
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_arr(arr)

    def set_arr(self, arr: List[int]) -> None:
        self.arr = arr
        self.min_val = min(arr)
        self.max_val = max(arr)

        self.block_width = round(self.width - self.SIDE_PADDING) / len(arr)
        self.block_height = (self.height - self.TOP_PADDING) / (self.max_val - self.min_val)

        self.start_x = self.SIDE_PADDING // 2