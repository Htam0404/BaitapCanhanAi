from utils.state import get_neighbors, flatten


def sensorless_search(start, goal):
    frontier = [(start, [start])]
    explored = set()

    while frontier:
        state, path = frontier.pop(0)

        if state == goal:
            return path

        explored.add(tuple(flatten(state)))

        for neighbor in get_neighbors(state):
            if tuple(flatten(neighbor)) not in explored:
                frontier.append((neighbor, path + [neighbor]))

    return []
