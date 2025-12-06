from typing import List, Tuple, Optional
import heapq
import time


class Solution:
    def findFreshFruitPart1(self, fresh_ranges: List[tuple[int, int]], check_ids: List[int]) -> int:
        check_ids.sort()
        fresh_fruit = 0
        for check_id in check_ids:
            for start, end in fresh_ranges:
                if check_id < start:
                    break
                elif start <= check_id <= end:
                    fresh_fruit += 1
                    break
         


        return fresh_fruit
    
    def findFreshFruitPart2(self, fresh_ranges: List[tuple[int, int]]) -> int:
        num_of_fresh_ids = 0

        for start, end in fresh_ranges:
            num_of_fresh_ids += (end - start) + 1

        return num_of_fresh_ids

    def fixRanges(self, id_ranges) -> List[tuple[int, int]]:
        num_id_ranges = [(int(start), int(end)) for start, end in id_ranges]
        heapq.heapify(num_id_ranges)
        fixed_id_ranges = []

        start1, end1 = heapq.heappop(num_id_ranges)
        while num_id_ranges:
            start2, end2 = heapq.heappop(num_id_ranges)
            if start2 > end1:
                fixed_id_ranges.append((start1, end1))
                start1, end1 = start2, end2
            else:
                end1 = max(end1, end2)

        fixed_id_ranges.append((start1, end1))
        return fixed_id_ranges

if __name__ == "__main__":
    start_time = time.perf_counter()
    solution = Solution()
    spoiled_database_file = open("aocdInputFiles/aocdDay5.txt", "r")
    id_ranges = []
    ids_to_check = []

    while True:

        id_range = spoiled_database_file.readline()
        if id_range == '\n':
            break
        id_ranges.append(tuple(id_range.strip('\n').split('-')))

    while True:

        id_to_check = spoiled_database_file.readline()
        if not id_to_check:
            break
        ids_to_check.append(int(id_to_check.strip('\n')))

    spoiled_database_file.close()

    #Testing part1 and part2 ----------------------------

    test_ranges = [tuple('3-5'.split('-')),
            tuple('10-14'.split('-')),
            tuple('16-20'.split('-')),
            tuple('12-18'.split('-'))
            ]
    test_id_check = [1,
                    5,
                    8,
                    11,
                    17,
                    32,
                    88]
    

    test_fixed_ranges = solution.fixRanges(test_ranges)

    test_answer_part1 = solution.findFreshFruitPart1(test_fixed_ranges, test_id_check)
    test_answer_part2 = solution.findFreshFruitPart2(test_fixed_ranges)

    print('answer to the first part for the test is:', test_answer_part1)
    print('answer to the second part for the test is:', test_answer_part2)

    #Testing part1 and part2 ----------------------------
    fixed_ranges = solution.fixRanges(id_ranges)

    answer_part1 = solution.findFreshFruitPart1(fixed_ranges, ids_to_check)
    answer_part2 = solution.findFreshFruitPart2(fixed_ranges)

    print('answer to the first part is:', answer_part1)
    print('answer to the second part is:', answer_part2)
    end_time = time.perf_counter()
    print(f"\nTotal runtime: {end_time - start_time:.6f} seconds")