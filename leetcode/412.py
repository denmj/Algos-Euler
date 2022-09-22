"""
izzBuzz is a childhood game that iterates over a range of numbers
and uses simple logic to decide whether to say a "Fizz,"
"Buzz," or a number. Through this problem, you will learn to convert that logic into code, and you will be introduced to
frequently used operations like modulo and string concatenation.
We encourage you to try solving 412. Fizz Buzz on your own first, then return here to watch the video solution.
"""

from typing import List


class Solution:
    @staticmethod
    def fizzBuzz(n: int) -> List[str]:
        output = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                output.append("FizzBuzz")
            elif i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(i))
        return output
