from constants import *
from collections import deque
from Algorithms.utils import distance_to_ghost

def BFS(start: tuple, food_positions: list, ghost_positions: list, wall_positions: list):
    """BFS giúp Pacman tìm đường đi nhưng tránh quái."""
    queue = deque([(start, [])])  # Lưu trữ (vị trí hiện tại, đường đi)
    visited = {start}

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) in food_positions:
            return path + [(r, c)]  # Tìm thấy thức ăn

        next_moves = []
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and (nr, nc) not in wall_positions and (nr, nc) not in ghost_positions:
                next_moves.append(((nr, nc), distance_to_ghost((nr, nc), ghost_positions)))

        # Sắp xếp các bước đi ưu tiên tránh xa quái
        next_moves.sort(key=lambda x: x[1], reverse=True)

        for (nr, nc), _ in next_moves:
            queue.append(((nr, nc), path + [(nr, nc)]))
            visited.add((nr, nc))

    return path  # Không tìm thấy đường đi
