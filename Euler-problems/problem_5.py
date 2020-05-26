"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""


def problem_5(n):
    run = True
    num = n
    while run:
        sum = 0
        least = 0
        for reminer in range(1, 20):
            if num % reminer != 0:
                break

            else:
                sum += reminer
                if sum == 190:
                    least = num
                    run = False
        num += 20
    return least


v = problem_5(20)
print(v)