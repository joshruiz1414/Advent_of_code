from typing import List, Tuple, Optional
import heapq


class Solution:
    def findSpoiledFruitPart1(self, ranges: str, ids: List[str]) -> int:
        return 0

    def fixRanges(self, ranges: List[tuple[str]]) -> Optional[list[tuple[str]]]:
        pass

if __name__ == "__main__":

    solution = Solution()
    spoiled_database_file = open("aocdInputFiles/aocdDay5.txt", "r")
    id_ranges = []
    fresh_ids = []

    while True:

        id_range = spoiled_database_file.readline()
        if id_range == '\n':
            break
        id_ranges.append(tuple(id_range.strip('\n').split('-')))

    while True:

        fresh_id = spoiled_database_file.readline()
        if not fresh_id:
            break
        fresh_ids.append(fresh_id.strip('\n'))

    spoiled_database_file.close()

    #fixed_ranges = solution.fixRanges(id_ranges)

    #answer_part1 = solution.findSpoiledFruitPart1(fixed_ranges)
    #answer_part2 = solution.findSpoiledFruitPart2()

    #print('answer to the first part is:', answer_part1)
    #print('answer to the second part is:', answer_part2)