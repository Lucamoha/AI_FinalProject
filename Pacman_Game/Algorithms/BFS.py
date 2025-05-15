from constants import *
from collections import deque
from Algorithms.utils import distance

def BFS(start: tuple, food_positions: list, ghost_positions: list, wall_positions: list):
    """BFS giúp Pacman tìm đường đi nhưng tránh quái."""
    queue = deque([(start, [])])  # Lưu trữ (vị trí hiện tại, đường đi)
    visited = {start}

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) in food_positions:
            return path + [(r, c)]  # Tìm thấy thức ăn

        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and (nr, nc) not in wall_positions and (nr, nc) not in ghost_positions:
                queue.append(((nr, nc), path + [(nr, nc)]))
                visited.add((nr, nc))

    return path  # Không tìm thấy đường đi
