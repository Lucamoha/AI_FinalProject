from constants import *


def DFS(start: tuple, food_positions: list, ghost_positions: list, wall_positions: list):
    """DFS giúp Pacman tìm đường đi nhưng tránh quái."""
    stack = [(start, [])]  # Lưu trữ (vị trí hiện tại, đường đi)
    visited = {start}

    def distance_to_ghost(pos):
        """Tính khoảng cách Manhattan đến quái gần nhất."""
        if not ghost_positions:
            return float('inf')
        return min(abs(pos[0] - g[0]) + abs(pos[1] - g[1]) for g in ghost_positions)

    while stack:
        (r, c), path = stack.pop()

        if (r, c) in food_positions:
            return path + [(r, c)], True  # Tìm thấy thức ăn

        next_moves = []
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and (nr, nc) not in wall_positions and (nr, nc) not in ghost_positions:
                next_moves.append(((nr, nc), distance_to_ghost((nr, nc))))

        # Sắp xếp các bước đi ưu tiên tránh xa quái
        next_moves.sort(key=lambda x: x[1], reverse=True)

        for (nr, nc), _ in next_moves:
            stack.append(((nr, nc), path + [(nr, nc)]))
            visited.add((nr, nc))

    return [], False  # Không tìm thấy đường đi