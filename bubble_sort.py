from draw_information import DrawInformation
from typing import List
from draw_utils import draw_arr

def bubble_sort(draw_info: DrawInformation, ascending: bool = True) -> List[int]:
    arr = draw_info.arr
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            num1 = arr[j]
            num2 = arr[j + 1]
            # The first condition is for ascending, second is for descending
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                draw_arr(draw_info, {j: draw_info.RED, j+1: draw_info.BLUE}, True)

                # Essentially pausing execution, yielding control back to the where
                # this was called. This allows us to still have control in the main loop.
                yield True
    return arr