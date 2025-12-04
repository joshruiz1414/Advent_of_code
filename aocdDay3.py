from typing import List, Tuple
import heapq


class Solution:
    def findHighestJoltagePart1(self, bank: str) -> int:
        highest_num = ('0', 0)
        for index, val in enumerate(bank):
            if highest_num[0] < val:
                highest_num = (val, index)
            
        check_second = bank[highest_num[1] + 1:]
        if check_second:
            second_num = max(check_second)
        else:
            second_num = max(bank[:-1])
            return (int(second_num) * 10) + int(highest_num[0])

        return (int(highest_num[0]) * 10) + int(second_num)



    def findHighestJoltagePart2(self, bank: str) -> int:
        int_ratings = list(bank)
        stack = []
        for index, rating in enumerate(int_ratings):
            while stack and rating > stack[-1] and len(stack) + (len(bank) - index) > 12:
                stack.pop()
            if len(stack) < 12:
                stack.append(rating)
            
        ans = ''
        for char in stack:
            ans += char

        return int(ans)

if __name__ == "__main__":
    
    solution = Solution()
    max_joltagePart1 = 0
    max_joltagePart2 = 0
    bank_ratings = open("aocdInputFiles/aocdDay3.txt", "r")
    while True:
        ratings = bank_ratings.readline()    
        if not ratings:
            break 
        max_joltagePart1 += solution.findHighestJoltagePart1(ratings.strip('\n'))
        max_joltagePart2 += solution.findHighestJoltagePart2(ratings.strip('\n'))
    
    bank_ratings.close()

    print('answer to the first part is:', max_joltagePart1)
    print('answer to the second part is:', max_joltagePart2)

