from typing import List, Tuple, Optional
import time
import math


class Solution:
    def findNumSplitsPart1(self, beam_grid: List[List[int]]) -> int:
        return 0
    





if __name__ == "__main__":
    start_time = time.perf_counter()

    solution = Solution()
    beam_file = open("aocdInputFiles/aocdDay7.txt", "r")

    beam_grid = []

    while True:

        beam_line = beam_file.readline()

        if not beam_line:
            break

        beam_grid.append(list(beam_line.strip('\n')))

    
    beam_file.close()

    answer_part1 = solution.findNumSplitsPart1(beam_grid)
    #answer_part2 = solution.findNumSplitsPart2(beam_grid)

    print('\nanswer to the first part is:', answer_part1)
    #print('answer to the second part is:', answer_part2)

    end_time = time.perf_counter()
    print(f"\nTotal runtime: {end_time - start_time:.6f} seconds")