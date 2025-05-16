import random
from utils.state import flatten, apply_action, is_goal_state, get_possible_actions


def q_learning(start_state, goal_state, num_episodes=5000, alpha=0.1, gamma=0.9, epsilon=0.2):
    q_table = {}
    actions = ["up", "down", "left", "right"]

    def get_state_key(state):
        return tuple(flatten(state))

    def get_q(state, action):
        state_key = get_state_key(state)
        if state_key not in q_table:
            q_table[state_key] = {a: 0 for a in actions}
        return q_table[state_key][action]

    def update_q(state, action, value):
        state_key = get_state_key(state)
        if state_key not in q_table:
            q_table[state_key] = {a: 0 for a in actions}
        q_table[state_key][action] = value

    def choose_action(state):
        possible_actions = get_possible_actions(state)
        if not possible_actions:
            return None

        if random.random() < epsilon:
            return random.choice(possible_actions)
        else:
            state_key = get_state_key(state)
            q_values = q_table.get(state_key, {a: 0 for a in actions})
            valid_q = {a: q_values.get(a, 0) for a in possible_actions}
            return max(valid_q, key=valid_q.get)

    for episode in range(num_episodes):
        state = start_state

        while not is_goal_state(state, goal_state):
            possible_actions = get_possible_actions(state)
            if not possible_actions:
                break

            action = choose_action(state)
            if action is None:
                break

            next_state = apply_action(state, action)

            reward = 0 if is_goal_state(next_state, goal_state) else -1

            current_q = get_q(state, action)
            next_possible_actions = get_possible_actions(next_state)
            if next_possible_actions:
                next_max_q = max([get_q(next_state, a)
                                 for a in next_possible_actions])
            else:
                next_max_q = 0

            new_q = current_q + alpha * \
                (reward + gamma * next_max_q - current_q)
            update_q(state, action, new_q)

            state = next_state

    return q_table
