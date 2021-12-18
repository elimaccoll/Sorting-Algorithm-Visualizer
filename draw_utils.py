from typing import Tuple, Dict
import pygame
from draw_information import DrawInformation
pygame.init()


def draw(draw_info: DrawInformation, algorithm_name: str, ascending: bool) -> None:
    draw_info.window.fill(draw_info.BG_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algorithm_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.BLACK)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2, 5))

    sorting_controls = draw_info.FONT.render("R - Reset | Space - Start Sorting | A - Toggle Ascending/Descending", 1, draw_info.BLACK)
    draw_info.window.blit(sorting_controls, (draw_info.width/2 - sorting_controls.get_width()/2, 40))

    algorithm_controls = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, draw_info.BLACK)
    draw_info.window.blit(algorithm_controls, (draw_info.width/2 - algorithm_controls.get_width()/2, 70))

    draw_arr(draw_info)
    
    pygame.display.update()

def draw_arr(draw_info: DrawInformation, color_positions: Dict[int, Tuple[int, int, int]] = {}, clear_bg: bool = False) -> None:
    arr = draw_info.arr

    if clear_bg:
        # Clear the section of the screen with the array
        clear_rect = (draw_info.SIDE_PADDING // 2, draw_info.TOP_PADDING, \
            draw_info.width - draw_info.SIDE_PADDING, draw_info.height - draw_info.TOP_PADDING)
        pygame.draw.rect(draw_info.window, draw_info.BG_COLOR, clear_rect)

    for i, val in enumerate(arr):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i % len(draw_info.GRADIENTS)]
        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, \
            (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()
