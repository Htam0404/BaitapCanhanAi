import pygame
import sys
import time
import random
from algorithms.uninformed import dfs, bfs, ucs, iddfs
from algorithms.informed import greedy, astar, idastar
from utils.state import get_neighbors, generate_random_state, flatten, unflatten, mutate, crossover
from utils.heuristic import heuristic, fitness
from algorithms.local_search import (
    hill_climbing_simple,
    hill_climbing_steepest_ascent,
    random_restart_hill_climbing,
    beam_search,
    simulated_annealing,
    genetic_algorithm,
)
from algorithms.Searching_in_complex_environments.and_or_search import and_or_search
from algorithms.CSPS import Backtracking, Backtracking_Forward, Min_Conflicts
from algorithms.Searching_in_complex_environments.SensorlessSearch import sensorless_search
from algorithms.QLearning import q_learning
from algorithms.NondeterministicSearch import nondeterministic_search
from algorithms.Searching_in_complex_environments.PartiallyObservableSearch import partially_observable_search
from utils.performance import PerformanceLogger


class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 450, 650
        self.GRID_SIZE = 3
        self.TILE_SIZE = self.WIDTH // self.GRID_SIZE
        self.FONT = pygame.font.SysFont(None, 36)

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (200, 0, 0)
        self.BLUE = (0, 0, 200)

        self.start = [
            [2, 6, 5],
            [0, 8, 7],
            [4, 3, 1]
        ]
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Nguyen Hoang Tam")

        self.selected_category = None
        self.selected_algorithm = None
        self.logger = PerformanceLogger()

        self.algorithms = {
            "Uninformed Search": ["DFS", "BFS", "UCS", "IDDFS"],
            "Informed Search": ["Greedy", "A*", "IDA*"],
            "Local Search": [
                "Hill Climbing Simple", "Hill Climbing Steepest Ascent",
                "Random Restart Hill Climbing", "Beam Search",
                "Simulated Annealing", "Genetic Algorithm"
            ],
            "And-Or Search": ["And-Or Search"],
            "CSP": ["Backtracking", "Backtracking Forward", "Min Conflicts",],
            "Sensorless Search": ["Sensorless Search"],
            "QLearning": ["QLearning"],
            "Nondeterministic Search": ["Nondeterministic Search"],
            "Partially Observable Search": ["Partially Observable Search"]
        }

        self.algorithms_map = {
            "DFS": dfs,
            "BFS": bfs,
            "UCS": ucs,
            "IDDFS": iddfs,
            "Greedy": greedy,
            "A*": astar,
            "IDA*": idastar,
            "Hill Climbing Simple": hill_climbing_simple,
            "Hill Climbing Steepest Ascent": hill_climbing_steepest_ascent,
            "Random Restart Hill Climbing": random_restart_hill_climbing,
            "Beam Search": beam_search,
            "Simulated Annealing": simulated_annealing,
            "Genetic Algorithm": genetic_algorithm,
            "And-Or Search": and_or_search,
            "Backtracking": Backtracking,
            "Backtracking Forward": Backtracking_Forward,
            "Min Conflicts": Min_Conflicts,
            "Sensorless Search": sensorless_search,
            "QLearning": q_learning,
            "Nondeterministic Search": nondeterministic_search,
            "Partially Observable Search": partially_observable_search
        }

    def draw_grid(self, state):
        self.screen.fill(self.WHITE)
        for r in range(self.GRID_SIZE):
            for c in range(self.GRID_SIZE):
                value = state[r][c]
                if value != 0:
                    pygame.draw.rect(
                        self.screen,
                        self.BLACK,
                        (c * self.TILE_SIZE, r * self.TILE_SIZE,
                         self.TILE_SIZE, self.TILE_SIZE)
                    )
                    text = self.FONT.render(str(value), True, self.WHITE)
                    self.screen.blit(
                        text,
                        (c * self.TILE_SIZE + self.TILE_SIZE // 3,
                         r * self.TILE_SIZE + self.TILE_SIZE // 4)
                    )
        pygame.display.flip()

    def draw_csp_solution(self, board):
        self.screen.fill(self.WHITE)
        size = self.WIDTH // 8
        for r in range(8):
            for c in range(8):
                color = self.BLACK if (r + c) % 2 == 0 else self.WHITE
                pygame.draw.rect(self.screen, color,
                                 (c * size, r * size, size, size))
                if board[r][c] == 1:
                    pygame.draw.circle(self.screen, self.RED,
                                       (c * size + size // 2, r * size + size // 2), size // 3)
        pygame.display.flip()

    def draw_menu(self):
        self.screen.fill(self.WHITE)
        base_spacing = 35

        for i, category in enumerate(self.algorithms.keys()):
            color = self.BLUE if self.selected_category == category else self.BLACK
            text = self.FONT.render(category, True, color)
            self.screen.blit(text, (30, 30 + i * base_spacing))

        if self.selected_category:
            algo_list = self.algorithms[self.selected_category]
            start_y = 30 + len(self.algorithms) * base_spacing
            for j, algo in enumerate(algo_list):
                color = self.BLUE if self.selected_algorithm == algo else self.BLACK
                text = self.FONT.render(algo, True, color)
                self.screen.blit(text, (100, start_y + j * base_spacing))

            start_button_y = start_y + len(algo_list) * base_spacing
            pygame.draw.rect(self.screen, self.RED,
                             (50, start_button_y, 200, 40))
            start_text = self.FONT.render("Start", True, self.WHITE)
            self.screen.blit(start_text, (110, start_button_y + 5))

        pygame.display.flip()

    def solve(self):
        if self.selected_algorithm is None:
            return

        start_time = time.time()

        if self.selected_category == "Sensorless Search":
            solution = self.algorithms_map[self.selected_algorithm](
                self.start, self.goal)

            if not solution:
                print("Không tìm thấy lời giải")
                return

            end_time = time.time()
            print(
                f"Thuật toán {self.selected_algorithm} hoàn thành trong {end_time - start_time:.4f} giây")
            print(f"Số bước thực hiện: {len(solution) - 1}")

            for i, state in enumerate(solution):
                print(f"Bước {i}:")

                if isinstance(state, list):
                    if len(state) == 9 and all(isinstance(x, int) for x in state):
                        state = [state[i:i + 3] for i in range(0, 9, 3)]
                    elif not all(isinstance(row, list) for row in state):
                        print("Trạng thái không hợp lệ, bỏ qua bước này.")
                        continue
                else:
                    print("Trạng thái không phải danh sách, bỏ qua bước này.")
                    continue

                for row in state:
                    print(row)
                self.draw_grid(state)
                pygame.time.delay(300)

        else:
            solution = self.algorithms_map[self.selected_algorithm](
                self.start, self.goal)
            self.logger.log(self.selected_algorithm, start_time)

            if not solution:
                print("Không tìm thấy lời giải")
                return

            end_time = time.time()
            print(
                f"Thuật toán {self.selected_algorithm} hoàn thành trong {end_time - start_time:.4f} giây")
            print(f"Số bước thực hiện: {len(solution) - 1}")

            for i, state in enumerate(solution):
                print(f"Bước {i}:")
                if isinstance(state, list):
                    if len(state) == 9 and all(isinstance(x, int) for x in state):
                        state = [state[i:i + 3] for i in range(0, 9, 3)]
                    elif not all(isinstance(row, list) for row in state):
                        print("Trạng thái không hợp lệ, bỏ qua bước này.")
                        continue
                else:
                    print("Trạng thái không phải danh sách, bỏ qua bước này.")
                    continue

                for row in state:
                    print(row)
                self.draw_grid(state)
                pygame.time.delay(300)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                base_spacing = 35

                for i, category in enumerate(self.algorithms.keys()):
                    if 30 <= x <= 280 and (30 + i * base_spacing) <= y <= (30 + i * base_spacing + 30):
                        self.selected_category = category
                        self.selected_algorithm = None

                if self.selected_category:
                    algo_list = self.algorithms[self.selected_category]
                    start_y = 30 + len(self.algorithms) * base_spacing
                    for j, algo in enumerate(algo_list):
                        if 100 <= x <= 250 and (start_y + j * base_spacing) <= y <= (start_y + j * base_spacing + 30):
                            self.selected_algorithm = algo

                    if 50 <= x <= 250 and start_y + len(algo_list) * base_spacing <= y <= start_y + len(algo_list) * base_spacing + 40:
                        self.solve()

    def run(self):
        while True:
            self.handle_events()
            self.draw_menu()


if __name__ == "__main__":
    game = Game()
    game.run()
