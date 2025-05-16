def heuristic(state, goal=None):
    if goal is None:
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    distance = 0
    for r in range(3):
        for c in range(3):
            value = state[r][c]
            if value != 0:
                goal_r, goal_c = [(i, j) for i in range(3)
                                  for j in range(3) if goal[i][j] == value][0]
                distance += abs(r - goal_r) + abs(c - goal_c)
    return distance


def fitness(state, goal=None):
    if goal is None:
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return -heuristic(state, goal)
