def partially_observable_search(start_state, goal_state):
    from collections import deque
    import time
    from utils.state import get_neighbors, flatten, unflatten

    def get_possible_states(states):
        result = set()
        for state in states:
            neighbors = get_neighbors(state)
            for neighbor in neighbors:
                result.add(tuple(flatten(neighbor)))
        return [unflatten(list(s)) for s in result]

    def is_goal_state_in(states):
        return any(s == goal_state for s in states)

    visited = set()
    belief_states = [start_state]
    path = [start_state]

    start_time = time.time()

    while not is_goal_state_in(belief_states):
        next_belief_states = get_possible_states(belief_states)
        frozen = [tuple(flatten(s)) for s in next_belief_states]

        key = tuple(sorted(frozen))
        if key in visited:
            break
        visited.add(key)

        path.append(belief_states[0])
        belief_states = next_belief_states

        if time.time() - start_time > 20:
            print("Thoát do quá thời gian")
            break

    path.append(goal_state)
    return path
