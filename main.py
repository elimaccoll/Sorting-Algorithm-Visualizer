from typing import List
import pygame
from random import randint
from draw_information import DrawInformation
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from draw_utils import draw
pygame.init()

def generate_arr(num_items: int, min_val: int, max_val: int) -> List[int]:
    arr = [randint(min_val, max_val) for _ in range(num_items)]
    return arr

def main():
    run = True
    clock = pygame.time.Clock()
    
    width, height = 800, 800
    num_items, min_val, max_val = 50, 0, 100
    arr = generate_arr(num_items, min_val, max_val)
    draw_info = DrawInformation(width, height, arr)

    sorting = False
    ascending = True

    # Default sorting algorithm
    algorithm = bubble_sort
    algorithm_name = "Bubble Sort"
    algorithm_generator = None

    while run:
        # Speed up by making FPS higher - Remove clock.tick for max speed
        clock.tick(60) # FPS
        
        if sorting:
            try:
                next(algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, algorithm_name, ascending)

        for event in pygame.event.get():
            # Clicking the 'X' in the top right of the window
            if event.type == pygame.QUIT:
                run = False
            
            # If no key pressed, then continue
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                sorting = False
                arr = generate_arr(num_items, min_val, max_val)
                draw_info.set_arr(arr)
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                algorithm_generator = algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = not ascending
            elif event.key == pygame.K_i and not sorting:
                algorithm = insertion_sort
                algorithm_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                algorithm = bubble_sort
                algorithm_name = "Bubble Sort"

    pygame.quit()

if __name__ == "__main__":
    main()