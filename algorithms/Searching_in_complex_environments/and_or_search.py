import random
import heapq
from utils.state import get_neighbors, generate_random_state, flatten, unflatten, mutate, crossover
from utils.heuristic import heuristic, fitness


def and_or_search(start, goal, max_depth=70):
    def or_search(state, path, depth, visited):
        state_t = tuple(map(tuple, state))
        if state == goal:
            return path + [state]
        if depth >= max_depth or state_t in visited:
            return None

        visited.add(state_t)

        neighbors = sorted(get_neighbors(
            state), key=lambda s: heuristic(s, goal))
        for neighbor in neighbors:
            result = and_search(
                neighbor, path + [state], depth + 1, visited.copy())
            if result:
                return result

        return None

    def and_search(state, path, depth, visited):
        return or_search(state, path, depth, visited)

    visited = set()
    return or_search(start, [], 0, visited)
