import time
from typing import List, Tuple

class Solution:
    def fixIds(self, id_ranges: List[str]) -> int:
        invalid_ids_sum = 0
        for num_range in id_ranges:
            start, _ , end = num_range.partition('-')
            for num in range(int(start), int(end)+ 1):
                if self.checkInvalidId(str(num)):
                    invalid_ids_sum += num
        return invalid_ids_sum
    
    def findInvalidIdsPart2(self, id_ranges: List[str]) -> int:
        invalid_ids_sum = 0
        for num_range in id_ranges:
            start, _ , end = num_range.partition('-')
            for num in range(int(start), int(end)+ 1):
                if self.checkInvalidIdPart2(str(num)):
                    invalid_ids_sum += num
        return invalid_ids_sum
    
    def checkInvalidId(self, id: str) -> bool:
        if len(id) % 2 != 0:
            return False
        midpoint = len(id) // 2
        return id[:midpoint] == id[midpoint:]
    
    def checkInvalidIdPart2(self, id: str) -> bool:
        midpoint = len(id) // 2
        for subarray in range(1, midpoint + 1):
            if len(id) % subarray != 0:
                continue
            check = id[:subarray]
            end = subarray
            start = 0
            while end < len(id) + 1:
                if check != id[start:end]:
                    break
                elif end == len(id):
                    return True
                start += subarray
                end += subarray
        return False


class TestSolution:
    def testFindInvalidIdsPart2(self):
        test1 = Solution()
        ranges = ["11-22"]
        answer = test1.findInvalidIdsPart2(ranges)
        assert answer == 33

        test2 = Solution()
        ranges = ['1188511880-1188511890']
        answer = test2.findInvalidIdsPart2(ranges)
        assert answer == 1188511885

        test3 = Solution()
        ranges = ["38593856-38593862"]
        answer = test3.findInvalidIdsPart2(ranges)
        assert answer == 38593859

        test4 = Solution()
        ranges = ["222220-222224"]
        answer = test4.findInvalidIdsPart2(ranges)
        assert answer == 222222

        test5 = Solution()
        ranges = ["2121212118-2121212124"]
        answer = test5.findInvalidIdsPart2(ranges)
        assert answer == 2121212121


if __name__ == "__main__":
    solution = Solution()
    id_file = open("aocdInputFiles/aocdDay2.txt", "r")
    id_ranges = id_file.readline()
    id_file.close()

    # Run tests
    test = TestSolution()
    test.testFindInvalidIdsPart2()

    ranges = id_ranges.split(',')

    start1 = time.perf_counter()
    answer1 = solution.fixIds(ranges)
    end1 = time.perf_counter()

    start2 = time.perf_counter()
    answer2 = solution.findInvalidIdsPart2(ranges)
    end2 = time.perf_counter()

    print('answer to the first part is:', answer1)
    print(f'time for part 1: {end1 - start1:.6f} seconds')
    
    # Clearly a brute force approach which takes a long time
    print('answer to the second part is:', answer2)
    print(f'time for part 2: {end2 - start2:.6f} seconds')
