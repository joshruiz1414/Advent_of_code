from typing import List, Tuple, Optional
import time
import math




class Solution:
    def findMathResultPart1(self, math_grid: List[List[int]], operators: List[str]) -> int:
        total_num = 0
        curr_row = 0
        
        for col in range(len(math_grid[curr_row])):
            col_nums = []

            for row in range(len(math_grid)):
                col_nums.append(math_grid[row][col])

            total_num += math.prod(col_nums) if operators[col] == '*' else sum(col_nums)
            curr_row += 1

        return total_num
    

    def findMathResultPart2(self, math_str: List[str], operators: List[str]) -> int:
        total = 0
        col = 0
        operator_col = 0
        vertical_nums = []

        while True:
            built_num = ''

            for line in math_str:
                if col < len(line) and line[col].isdigit():
                    built_num += line[col]

            if built_num == '':
                if col > len(math_str[0]):
                    total += math.prod(vertical_nums) if operators[operator_col - 1] == '*' else sum(vertical_nums)
                    break
                total += math.prod(vertical_nums) if operators[operator_col] == '*' else sum(vertical_nums)
                vertical_nums.clear()
                operator_col += 1
                col += 1
                continue

            vertical_nums.append(int(built_num))
            col += 1
        
        return total


if __name__ == "__main__":
    start_time = time.perf_counter()
    solution = Solution()
    math_file = open("aocdInputFiles/aocdDay6.txt", "r")

    math_grid = []
    math_str = []

    while True:

        eq_numbers = math_file.readline()

        if eq_numbers[0] == '*' or eq_numbers[0] == '+':
            operators = eq_numbers.split()
            break

        math_str.append(eq_numbers.strip('\n'))
        math_grid.append([int(num) for num in eq_numbers.strip('\n').split()])

    
    math_file.close()

    answer_part1 = solution.findMathResultPart1(math_grid, operators)
    answer_part2 = solution.findMathResultPart2(math_str, operators)

    print('\nanswer to the first part is:', answer_part1)
    print('answer to the second part is:', answer_part2)

    end_time = time.perf_counter()
    print(f"\nTotal runtime: {end_time - start_time:.6f} seconds")