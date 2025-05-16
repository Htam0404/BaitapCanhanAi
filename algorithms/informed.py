import heapq
from utils.state import get_neighbors
from utils.heuristic import heuristic


def greedy(start, goal):
    queue = [(heuristic(start, goal), start, [])]
    visited = set()

    while queue:
        _, state, path = heapq.heappop(queue)
        if state == goal:
            return path + [state]

        visited.add(tuple(map(tuple, state)))
        for new_state in get_neighbors(state):
            if tuple(map(tuple, new_state)) not in visited:
                heapq.heappush(
                    queue, (heuristic(new_state, goal), new_state, path + [state]))

    return None


def astar(start, goal):
    queue = [(heuristic(start, goal), 0, start, [])]  # (f, g, state, path)
    visited = set()
    visited.add(tuple(map(tuple, start)))

    while queue:
        _, g, state, path = heapq.heappop(queue)
        if state == goal:
            return path + [state]

        for new_state in get_neighbors(state):
            if tuple(map(tuple, new_state)) not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(new_state, goal)
                heapq.heappush(
                    queue, (new_f, new_g, new_state, path + [state]))
                visited.add(tuple(map(tuple, new_state)))

    return None


def idastar(start, goal):
    def search(state, g, threshold, path, visited):
        f = g + heuristic(state, goal)
        if f > threshold:
            return f, None
        if state == goal:
            return f, path + [state]

        min_threshold = float('inf')
        visited.add(tuple(map(tuple, state)))

        for new_state in get_neighbors(state):
            if tuple(map(tuple, new_state)) not in visited:
                temp_threshold, result = search(
                    new_state, g + 1, threshold, path + [state], visited)
                if result is not None:
                    return temp_threshold, result
                min_threshold = min(min_threshold, temp_threshold)

        visited.remove(tuple(map(tuple, state)))
        return min_threshold, None

    threshold = heuristic(start, goal)
    max_iterations = 50
    iterations = 0

    while iterations < max_iterations:
        iterations += 1
        visited = set()
        temp_threshold, result = search(start, 0, threshold, [], visited)
        if result is not None:
            return result
        if temp_threshold == float('inf'):
            return None
        threshold = temp_threshold
