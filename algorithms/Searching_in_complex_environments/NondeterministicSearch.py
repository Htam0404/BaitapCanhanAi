from utils.state import get_neighbors, flatten


def nondeterministic_search(start, goal):
    """
    Thuật toán tìm kiếm không xác định (nondeterministic search)
    Mỗi hành động có thể dẫn đến nhiều kết quả khác nhau.
    Duyệt theo chiều rộng để tìm đường đi đến đích.
    """

    from collections import deque

    visited = set()
    frontier = deque()
    frontier.append((start, [start]))

    while frontier:
        current_state, path = frontier.popleft()

        if current_state == goal:
            return path
        visited.add(tuple(flatten(current_state)))

        possible_outcomes = get_neighbors(current_state)

        for next_state in possible_outcomes:
            if tuple(flatten(next_state)) not in visited:
                frontier.append((next_state, path + [next_state]))

    return None
