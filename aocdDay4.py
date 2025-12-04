from typing import List, Tuple


class Solution:

    def findValidPaperRollsPart1(self, paper_roll_map: List[List[str]]) -> int:

        ROW, COL = len(paper_roll_map), len(paper_roll_map[0])

        def checkValidRoll(row: int, col: int) -> bool:
            directions = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1),  (-1, 1), (1, -1)]
            adjacent_roll = 0
            for add_row, add_col in directions:
                new_row = row + add_row
                new_col = col + add_col

                if min(new_row, new_col) < 0 or new_row >= ROW or new_col >= COL or paper_roll_map[new_row][new_col] != '@':
                    continue
                adjacent_roll += 1

            return adjacent_roll < 4


        num_valid_rolls = 0
        for row in range(ROW):
            for col in range(COL):
                if paper_roll_map[row][col] == '@':
                    if checkValidRoll(row, col):
                        num_valid_rolls += 1

        return num_valid_rolls




    def findValidPaperRollsPart2(self, paper_roll_map: List[List[str]]) -> int:

        ROW, COL = len(paper_roll_map), len(paper_roll_map[0])

        def checkValidRoll(row: int, col: int) -> bool:
            directions = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1),  (-1, 1), (1, -1)]
            adjacent_roll = 0
            for add_row, add_col in directions:
                new_row = row + add_row
                new_col = col + add_col

                if min(new_row, new_col) < 0 or new_row >= ROW or new_col >= COL or paper_roll_map[new_row][new_col] == '.':
                    continue
                adjacent_roll += 1
            return adjacent_roll < 4


        num_valid_rolls = 0
        prev_removed_rolls = -1
        while True:
            prev_removed_rolls = num_valid_rolls
            for row in range(ROW):
                for col in range(COL):
                    if paper_roll_map[row][col] == '@':
                        if checkValidRoll(row, col):
                            num_valid_rolls += 1
                            paper_roll_map[row][col] = 'x'
            if prev_removed_rolls == num_valid_rolls:
                break
            for row in range(ROW):
                    for col in range(COL):
                        if paper_roll_map[row][col] == 'x':
                            paper_roll_map[row][col] = '.'


        return num_valid_rolls




if __name__ == "__main__":

    solution = Solution()
    paper_roll_file = open("aocdInputFiles/aocdDay4.txt", "r")
    paper_roll_map = []
    while True:

        paper_roll_row = paper_roll_file.readline()
        if not paper_roll_row:
            break
        paper_roll_map.append(list(paper_roll_row.strip('\n')))

    paper_roll_file.close()

    # Simple test to make sure: Answer == 13
    test = [
        list("..@@.@@@@."),
        list("@@@.@.@.@@"),
        list("@@@@@.@.@@"),
        list("@.@@@@..@."),
        list("@@.@@@@.@@"),
        list(".@@@@@@@.@" ),
        list(".@.@.@.@@@"),
        list("@.@@@.@@@@"),
        list(".@@@@@@@@."),
        list("@.@.@@@.@.")
]

    accessible_rolls1 = solution.findValidPaperRollsPart1(paper_roll_map)
    accessible_rolls2 = solution.findValidPaperRollsPart2(paper_roll_map)

    print('answer to the first part is:', accessible_rolls1)
    print('answer to the second part is:', accessible_rolls2)

# 745 not the answer for first part