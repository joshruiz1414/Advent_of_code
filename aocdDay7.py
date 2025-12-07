from typing import List, Tuple, Optional
import time
import math


class Solution:
    def findNumSplitsPart1(self, beam_grid: List[List[int]]) -> int:
        ROW, COL = len(beam_grid), len(beam_grid[0])
        total_splits = 0
        beam_cols = set()
        for row in range(ROW):
            for col in range(COL):
                if beam_grid[row][col] == 'S':
                    beam_cols.add(col)
                if beam_grid[row][col] == '^' and col in beam_cols:
                    beam_cols.remove(col)
                    total_splits += 1
                    if col + 1 < COL: 
                        beam_cols.add(col + 1)
                    if col - 1 >= 0:
                        beam_cols.add(col - 1)




        return total_splits
    





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
    print(beam_grid[0])
    answer_part1 = solution.findNumSplitsPart1(beam_grid)
    #answer_part2 = solution.findNumSplitsPart2(beam_grid)

    print('\nanswer to the first part is:', answer_part1)
    #print('answer to the second part is:', answer_part2)

    end_time = time.perf_counter()
    print(f"\nTotal runtime: {end_time - start_time:.6f} seconds")