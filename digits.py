for A in range(1, 10):
    for B in range(10):
        for C in range(10):
            for D in range(10):
                for E in range(1, 10):
                    left = int(''.join(str(x) for x in [A,B,C,C,D,E]))
                    right = int(''.join(str(x) for x in reversed([A, B, C, C, D, E])))
                    if left * 4 == right:
                        print(left)