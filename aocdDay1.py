from typing import List, Tuple


class Solution:
    def FindPasswordPart1(self, rotations: List[str]) -> int:
        combination_start = 50
        zero_count = 0
        for rotation in rotations:
            rotate = rotation.strip('\n')
            direction = rotate[0]
            if direction == 'L':
                steps = int(rotate[1:])
                combination_start -= steps
            else:
                steps = int(rotate[1:])
                combination_start += steps
            combination_start = combination_start % 100
            if combination_start == 0:
                zero_count += 1

        return zero_count

    def FindPasswordPart2(self, rotations: List[str]) -> int:
        combination_start = 50
        zero_count = 0

        for rotation in rotations:
            initial_position = combination_start
            rotate = rotation.strip('\n')
            direction = rotate[0]
            amount_rotate = int(rotate[1:]) % 100
            zero_count += int(rotate[1:]) // 100

            if direction == 'L':
                if initial_position - amount_rotate <= 0 and initial_position != 0:
                    zero_count += 1
                combination_start -= amount_rotate
            else:
                if initial_position + amount_rotate >= 100:
                    zero_count += 1
                combination_start += amount_rotate

            combination_start = combination_start % 100

        return zero_count
    
class TestSolution:
    def test_FindPasswordPart1(self):
        test1 = Solution()
        rotations = ["L30\n", "R80\n", "L50\n", "R70\n"]
        answer = test1.FindPasswordPart1(rotations)
        assert answer == 1, f"Test failed for FindPasswordPart1: test1, returned {answer} when should be 1"

    def test_FindPasswordPart2(self):
        test1 = Solution()
        rotations = ["L150\n", "R250\n", "L50\n", "R170\n"]
        answer = test1.FindPasswordPart2(rotations)
        assert  answer == 6, f"Test failed for FindPasswordPart2: test1, returned {answer} when should be 6"

        test2 = Solution()
        rotations = ["L50\n", "R50\n", "L50\n", "R50\n"]
        answer = test2.FindPasswordPart2(rotations)
        assert answer == 2, f"Test failed for FindPasswordPart2: test2, returned {answer} when should be 2"

        test3 = Solution()
        rotations = ["L0\n", "R1000\n", "L50\n", "R50\n"]
        answer = test3.FindPasswordPart2(rotations)
        assert answer == 11, f"Test failed for FindPasswordPart2: test3, returned {answer} when should be 11"

        test4 = Solution()
        rotations = ["L0\n", "R1000\n", "L50\n", "R50\n", "R50\n", "R200\n"]
        answer = test4.FindPasswordPart2(rotations)
        assert answer == 14, f"Test failed for FindPasswordPart2: test4, returned {answer} when should be 14"

        test5 = Solution()
        rotations = ["L50\n", "R300", "L400" ]
        answer = test5.FindPasswordPart2(rotations)
        assert answer == 8, f"Test failed for FindPasswordPart2: test5, returned {answer} when should be 8"

        test6 = Solution()
        rotations = ["L50\n", "R300", "L400", "L50" ]
        answer = test6.FindPasswordPart2(rotations)
        assert answer == 8, f"Test failed for FindPasswordPart2: test6, returned {answer} when should be 8"

        test7 = Solution()
        rotations = ["L50\n", "R300", "L400", "R50" ]
        answer = test7.FindPasswordPart2(rotations)
        assert answer == 8, f"Test failed for FindPasswordPart2: test7, returned {answer} when should be 8"
    

if __name__ == "__main__":
    solution = Solution()
    rotation_file = open("aocdInputFiles/aocdDay1.txt", "r")
    rotations = rotation_file.readlines()
    rotation_file.close()
    # Run tests
    test = TestSolution()
    test.test_FindPasswordPart1()
    test.test_FindPasswordPart2()
    # Calculate passwords
    password1 = solution.FindPasswordPart1(rotations)
    print(f"The calculated password for part one is: {password1}")
    password2 = solution.FindPasswordPart2(rotations)
    print(f"The calculated password for part two is: {password2}")





