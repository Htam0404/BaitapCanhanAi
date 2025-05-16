import random
from utils.state import generate_random_state, get_neighbors, flatten, unflatten, mutate, crossover


def Backtracking(start_state, goal_state, max_depth=50):

    path = [start_state]
    visited = set()

    def backtrack(state, depth):
        if depth > max_depth:
            return False
        if state == goal_state:
            return True
        visited.add(str(state))
        for neighbor in get_neighbors(state):
            if str(neighbor) not in visited:
                path.append(neighbor)
                if backtrack(neighbor, depth + 1):
                    return True
                path.pop()
        return False

    if backtrack(start_state, 0):
        return path
    else:
        print("Không tìm thấy lời giải")
        return []


def Backtracking_Forward(start_state, goal_state, max_depth=50):

    path = [start_state]
    visited = set()

    def forward_check(state):
        neighbors = get_neighbors(state)
        valid_neighbors = [
            neighbor for neighbor in neighbors if str(neighbor) not in visited]
        return valid_neighbors

    def backtrack(state, depth):
        if depth > max_depth:
            return False
        if state == goal_state:
            return True
        visited.add(str(state))

        valid_neighbors = forward_check(state)
        for neighbor in valid_neighbors:
            path.append(neighbor)
            if backtrack(neighbor, depth + 1):
                return True
            path.pop()
        return False

    if backtrack(start_state, 0):
        return path
    else:
        print("Không tìm thấy lời giải")
        return []


def Min_Conflicts(start_state, goal_state, max_steps=1000):
    current_state = start_state
    path = [current_state]

    def count_conflicts(state):
        return sum(1 for i in range(3) for j in range(3) if state[i][j] != goal_state[i][j] and state[i][j] != 0)

    def min_conflict_step(state):
        neighbors = get_neighbors(state)
        best_neighbor = min(neighbors, key=count_conflicts, default=state)
        return best_neighbor

    for _ in range(max_steps):
        if current_state == goal_state:
            return path

        next_state = min_conflict_step(current_state)

        if next_state == current_state:  # stuck
            break

        current_state = next_state
        path.append(current_state)

    print("Không tìm thấy lời giải")
    return []
