import heapq
from collections import deque
from utils.state import get_neighbors


def dfs(start, goal):
    stack = [(start, [])]
    visited = set()
    max_depth = 50

    while stack:
        state, path = stack.pop()
        if state == goal:
            return path + [state]

        state_tuple = tuple(map(tuple, state))

        if state_tuple in visited or len(path) > max_depth:
            continue

        visited.add(state_tuple)
        for new_state in get_neighbors(state):
            new_state_tuple = tuple(map(tuple, new_state))
            if new_state_tuple not in visited:
                stack.append((new_state, path + [state]))

    return None


def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()
    visited.add(tuple(map(tuple, start)))

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]

        for new_state in get_neighbors(state):
            if tuple(map(tuple, new_state)) not in visited:
                queue.append((new_state, path + [state]))
                visited.add(tuple(map(tuple, new_state)))

    return None


def ucs(start, goal):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, state, path = heapq.heappop(queue)
        if state == goal:
            return path + [state]

        visited.add(tuple(map(tuple, state)))
        for new_state in get_neighbors(state):
            if tuple(map(tuple, new_state)) not in visited:
                heapq.heappush(queue, (cost + 1, new_state, path + [state]))

    return None


def iddfs(start, goal, max_depth=20000):
    def dls(state, path, depth, visited):
        if state == goal:
            return path + [state]
        if depth == 0:
            return None

        visited.add(tuple(map(tuple, state)))
        for new_state in get_neighbors(state):
            if tuple(map(tuple, new_state)) not in visited:
                result = dls(new_state, path + [state], depth - 1, visited)
                if result:
                    return result

        visited.remove(tuple(map(tuple, state)))
        return None

    for depth in range(max_depth):
        visited = set()
        result = dls(start, [], depth, visited)
        if result:
            return result

    return None
