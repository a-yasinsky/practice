def prisonAfterNDays(cells, N):
    """
    :type cells: List[int]
    :type N: int
    :rtype: List[int]
    """
    state = []
    def nextDay(cells):
        return [int(cells[x-1] == cells[x+1]) if x > 0 and x < 7 else 0 for x,v in enumerate(cells)]

    while N > 0:
        cells = nextDay(cells)
        if cells not in state:
            state.append(cells)
            N -= 1
        else:
            delim = state.index(cells) + 1
            N = N % delim
            return state[N-1]
    return cells


print(prisonAfterNDays([0,1,0,1,1,0,0,1], 7))
