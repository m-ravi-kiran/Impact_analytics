def solve(N):
    if type(N) != int:
        return 'Invalid value passed. Pass an integer'
    num, den = 0, 0
    if N == 0:
        return num, den

    def back_track(arr, idx, N):
        if idx == N:
            if len(arr) != N:
                return
            # print(arr)
            nonlocal num, den
            den += 1
            if arr[-1] == 'A':
                num += 1
            return
        elif idx > N:
            return

        for i in range(idx, N):
            for j in [['P'], ['A'], ['A', 'A'], ['A', 'A', 'A']]:
                app = False
                if len(arr) == 0:
                    app = True
                    for k in j:
                        arr.append(k)
                else:
                    if arr[-1] == 'A' and j[0] == 'P':
                        app = True
                        for k in j:
                            arr.append(k)
                    elif arr[-1] == 'P':
                        app = True
                        for k in j:
                            arr.append(k)
                if app:
                    back_track(arr, i + len(j), N)
                    for k in j:
                        arr.pop()

    back_track([], 0, N)
    print(f'{num}/{den}')
    return num, den


if __name__ == '__main__':
    num, den = solve(4)
    print(f'{num}/{den}')
