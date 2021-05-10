Write a function solution(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before
you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations 
of positive integers no larger than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the solution would be "1". However, if M = "2" and F = "4",
it would not be possible.
Languages


def solution(x, y):
    goal = (int(x), int(y))
    start = (1, 1)
    gen = [start]
    c = 0
    while gen:
        # Generate new states
        next_gen = []
        for M,F in gen:
            if (M,F) == goal:
                return str(c)
            # Ignore states that never lead to goal
            MF = M+F
            if MF <= goal[0]:
                next_gen.append((MF, F))
            if MF <= goal[1]:
                next_gen.append((M, MF))
        
        # Go to next generation
        gen = next_gen
        c += 1
    return 'impossible'
print(solution('4', '7'))
# 4
print(solution('2', '1'))
# 1
print(solution('2', '4'))
# impossible
