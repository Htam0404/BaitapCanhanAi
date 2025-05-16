import random
import math
from utils.state import get_neighbors, generate_random_state, flatten, unflatten, mutate, crossover
from utils.heuristic import heuristic, fitness


def hill_climbing_simple(start, goal, max_iterations=1000):
    current = start
    path = [current]
    best_h = heuristic(current, goal)

    for _ in range(max_iterations):
        neighbors = get_neighbors(current)
        if not neighbors:
            break

        next_state = min(neighbors, key=lambda s: heuristic(s, goal))
        next_h = heuristic(next_state, goal)

        if next_h >= best_h:
            break

        current = next_state
        best_h = next_h
        path.append(current)

        if current == goal:
            return path

    return path if current == goal else None


def hill_climbing_steepest_ascent(start, goal, max_iterations=1000):
    current = start
    path = [current]
    best_h = heuristic(current, goal)

    for _ in range(max_iterations):
        neighbors = get_neighbors(current)
        if not neighbors:
            break

        best_neighbor = min(
            neighbors, key=lambda state: heuristic(state, goal))
        best_neighbor_h = heuristic(best_neighbor, goal)

        if best_neighbor_h >= best_h:
            break

        current = best_neighbor
        best_h = best_neighbor_h
        path.append(current)

        if current == goal:
            return path

    return path if current == goal else None


def random_restart_hill_climbing(start, goal, max_restarts=100, max_iterations=1000):
    for _ in range(max_restarts):
        initial_state = start if _ == 0 else generate_random_state()
        result = hill_climbing_steepest_ascent(
            initial_state, goal, max_iterations)
        if result:
            return result
    return None


def simulated_annealing(start, goal, initial_temp=5000, cooling_rate=0.995, min_temp=1e-3):
    current = start
    current_h = heuristic(current, goal)
    best_state = current
    best_h = current_h
    path = [current]
    best_path = list(path)
    temp = initial_temp

    while temp > min_temp:
        neighbors = get_neighbors(current)
        if not neighbors:
            break

        next_state = random.choice(neighbors)
        next_h = heuristic(next_state, goal)
        delta_e = current_h - next_h

        if delta_e > 0 or random.random() < math.exp(delta_e / temp):
            current = next_state
            current_h = next_h
            path.append(current)

            if current_h < best_h:
                best_state = current
                best_h = current_h
                best_path = list(path)

            if current == goal:
                return path

        temp *= cooling_rate

    return best_path if best_state == goal else None


def genetic_algorithm(start, goal, population_size=200, generations=1000):
    population = [generate_random_state() for _ in range(population_size)]
    population[0] = start
    best_state = None
    best_fitness_value = float('-inf')

    for _ in range(generations):
        population.sort(key=lambda s: fitness(s, goal), reverse=True)

        if fitness(population[0], goal) > best_fitness_value:
            best_state = population[0]
            best_fitness_value = fitness(population[0], goal)

        if population[0] == goal:
            return [population[0]]

        next_gen = population[:20]

        while len(next_gen) < population_size:
            parent1, parent2 = random.sample(next_gen, 2)
            child = crossover(parent1, parent2)
            if random.random() < 0.3:
                child = mutate(child)
            next_gen.append(child)

        population = next_gen

    return [best_state] if best_state else [population[0]]


def beam_search(start, goal, beam_width=2):
    queue = [(heuristic(start, goal), start, [])]
    visited = set()
    max_iterations = 1000
    iterations = 0

    while queue and iterations < max_iterations:
        iterations += 1
        queue.sort()
        queue = queue[:beam_width]
        next_queue = []

        for _, state, path in queue:
            if state == goal:
                return path + [state]

            visited.add(tuple(map(tuple, state)))
            for new_state in get_neighbors(state):
                if tuple(map(tuple, new_state)) not in visited:
                    next_queue.append(
                        (heuristic(new_state, goal), new_state, path + [state]))

        queue = next_queue

    return None
