from constants import *
import heapq
import random
from Algorithms.utils import manhattan

def A_star(start: tuple, pacman_position: tuple, wall_positions: list):
    """A* giúp ghost tìm đường đi ngắn nhất đến Pacman"""
    if not pacman_position:
        return []

    # Hàng đợi ưu tiên lưu trữ (f(n), g(n), vị trí hiện tại, đường đi)
    pq = []
    visited = {start}

    h = manhattan(start, pacman_position)
    heapq.heappush(pq, (h, 0, start, []))

    while pq:
        # Lấy nút có f(n) nhỏ nhất
        f, g, (r, c), path = heapq.heappop(pq)

        if (r, c) == pacman_position:
            return path + [(r, c)]  # Tìm thấy đường đi

        # Kiểm tra các bước đi lân cận (lên, xuống, trái, phải)
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and (nr, nc) not in wall_positions:
                visited.add((nr, nc))
                new_g = g + 1  # Chi phí từ start đến vị trí mới

                h = manhattan((nr, nc), pacman_position)  # Ước lượng chi phí
                f = new_g + h  # Tổng chi phí
                heapq.heappush(pq, (f, new_g, (nr, nc), path + [(nr, nc)]))

    return []  # Không tìm thấy đường đi


def random_move(start: tuple, wall_positions: list):
    """Ghost di chuyển ngẫu nhiên theo 4 hướng"""
    row, col = start 

    # Tạo các hướng di chuyển ngẫu nhiên
    possible_moves = []
    for dr, dc in MOVES:
        new_row = row + dr 
        new_col = col + dc
        new_position = (new_row, new_col)
        possible_moves.append(new_position)
    random.shuffle(possible_moves)

    # Lọc các ô đi được
    can_move = []
    for move in possible_moves:
        if move not in wall_positions:
            can_move.append(move) 

    # Nếu có đường đi thì chọn một hướng ngẫu nhiên
    if can_move:
        return random.choice(can_move)

    return []
