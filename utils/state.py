import random
import copy
from typing import List, Optional


def generate_random_state() -> List[List[int]]:
    numbers = list(range(9))
    while True:
        random.shuffle(numbers)
        if is_solvable(numbers):
            break
    return unflatten(numbers)


def is_solvable(flat_state: List[int]) -> bool:
    inv_count = 0
    for i in range(len(flat_state)):
        for j in range(i + 1, len(flat_state)):
            if flat_state[i] != 0 and flat_state[j] != 0 and flat_state[i] > flat_state[j]:
                inv_count += 1
    return inv_count % 2 == 0


def is_goal_state(state: List[List[int]], goal_state: Optional[List[List[int]]] = None) -> bool:
    if goal_state is None:
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return flatten(state) == flatten(goal_state)


def flatten(state: List[List[int]]) -> List[int]:
    return [cell for row in state for cell in row]


def unflatten(flat: List[int]) -> List[List[int]]:
    return [flat[i:i + 3] for i in range(0, 9, 3)]


def find_blank(state: List[List[int]]) -> tuple[int, int]:
    return next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)


def get_neighbors(state: List[List[int]]) -> List[List[List[int]]]:
    zero_row, zero_col = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dr, dc in moves:
        new_row, new_col = zero_row + dr, zero_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state]
            new_state[zero_row][zero_col], new_state[new_row][new_col] = \
                new_state[new_row][new_col], new_state[zero_row][zero_col]
            neighbors.append(new_state)
    return neighbors


def get_possible_actions(state: List[List[int]]) -> List[str]:
    i, j = find_blank(state)
    actions = []
    if i > 0:
        actions.append("up")
    if i < 2:
        actions.append("down")
    if j > 0:
        actions.append("left")
    if j < 2:
        actions.append("right")
    return actions


def apply_action(state: List[List[int]], action: str) -> Optional[List[List[int]]]:
    state = copy.deepcopy(state)
    i, j = find_blank(state)

    moves = {
        "up": (i - 1, j),
        "down": (i + 1, j),
        "left": (i, j - 1),
        "right": (i, j + 1),
    }

    if action in moves:
        ni, nj = moves[action]
        if 0 <= ni < 3 and 0 <= nj < 3:
            state[i][j], state[ni][nj] = state[ni][nj], state[i][j]
            return state
    return None


def mutate(state: List[List[int]]) -> List[List[int]]:
    flat = flatten(state)
    i, j = random.sample(range(9), 2)
    flat[i], flat[j] = flat[j], flat[i]
    return unflatten(flat)


def crossover(parent1: List[List[int]], parent2: List[List[int]]) -> List[List[int]]:
    flat1 = flatten(parent1)
    flat2 = flatten(parent2)
    cut = random.randint(1, 7)
    child = flat1[:cut] + [num for num in flat2 if num not in flat1[:cut]]
    return unflatten(child)
