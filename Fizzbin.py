#Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.
For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1



from itertools import permutations
def solution(l):
    highest_num = 0
    for i in range(1, len(l) + 1):
        for subset in permutations(l, i):
            if len(subset) >= 1:
                num = ''.join(str(x) for x in subset)
                num = int(num)
                mod_check = num % 3
                if mod_check == 0:
                    if num > highest_num:
                        highest_num = num
    return highest_num


print(solution([3, 1, 4,5, 1]))
