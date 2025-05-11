from constants import *
import heapq
from Algorithms.utils import distance, heuristic

def A_Star(start: tuple, food_positions: list, ghost_positions: list, wall_positions: list):
    """A* giúp Pacman tìm đường ngắn nhất đến thức ăn gần nhất nhưng tránh quái."""
    if not food_positions:
        return []

    # Hàng đợi ưu tiên lưu trữ (f(n), g(n), vị trí hiện tại, đường đi)
    pq = []
    visited = {start}
    
    # Tính khoảng cách manhattan đến thức ăn và ưu tiên né quái
    h = heuristic(start, food_positions, ghost_positions)
    heapq.heappush(pq, (h, 0, start, []))

    while pq:
        f, g, (r, c), path = heapq.heappop(pq)

        if (r, c) in food_positions:
            return path + [(r, c)]  # Tìm thấy thức ăn

        next_moves = []
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and (nr, nc) not in wall_positions and (nr, nc) not in ghost_positions:
                next_moves.append(((nr, nc), distance((nr, nc), ghost_positions)))

        # Sắp xếp các bước đi ưu tiên tránh xa quái
        next_moves.sort(key=lambda x: x[1], reverse=True)

        for (nr, nc), _ in next_moves:
            visited.add((nr, nc))
            new_g = g + 1

            # Tính khoảng cách manhattan và chi phí đến thức ăn, ưu tiên né quái
            h = heuristic((nr, nc), food_positions, ghost_positions)
            f = new_g + h
            heapq.heappush(pq, (f, new_g, (nr, nc), path + [(nr, nc)]))

    return []  # Không tìm thấy đường đi