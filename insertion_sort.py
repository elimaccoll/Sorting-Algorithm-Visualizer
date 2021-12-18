from draw_information import DrawInformation
from typing import List
from draw_utils import draw_arr

def insertion_sort(draw_info: DrawInformation, ascending: bool = True) -> List[int]:
    arr = draw_info.arr
    for i in range(1, len(arr)):
        curr = arr[i]
        while True:
            ascending_sort = i > 0 and arr[i - 1] > curr and ascending
            descending_sort = i > 0 and arr[i - 1] < curr and not ascending
            
            if not ascending_sort and not descending_sort:
                break

            arr[i] = arr[i - 1]
            i = i - 1
            arr[i] = curr
            draw_arr(draw_info, {i-1: draw_info.RED, i: draw_info.BLUE}, True)
            yield True
    return arr