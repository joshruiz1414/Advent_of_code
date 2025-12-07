from typing import List, Tuple, Optional
import time




class Solution:
    def findMathResultPart1(self, math_grid: List[List[int]], operators: List[str]) -> int:
        operator_map = {}
        tota_num = 0
        return tota_num


if __name__ == "__main__":
    start_time = time.perf_counter()
    solution = Solution()
    math_file = open("aocdInputFiles/aocdDay6.txt", "r")
    math_grid = []

    while True:

        eq_numbers = math_file.readline()
        if not eq_numbers[0].isdigit():
            operators = eq_numbers.split()
            break
        math_grid.append([int(num) for num in eq_numbers.strip('\n').split()])

    
    answer_part1 = solution.findMathResultPart1(math_grid, operators)

    math_file.close()

    print('answer to the first part is:', answer_part1)
    #print('answer to the second part is:', answer_part2)

    end_time = time.perf_counter()
    print(f"\nTotal runtime: {end_time - start_time:.6f} seconds")