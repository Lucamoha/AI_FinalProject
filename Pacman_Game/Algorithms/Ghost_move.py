from constants import *
import heapq
from Algorithms.utils import manhattan

def A_star(start: tuple, pacman_positions: list, wall_positions: list):
    """A* giúp ghost tìm đường đi ngắn nhất đến Pacman gần nhất."""
    if not pacman_positions:
        return []

    # Hàng đợi ưu tiên lưu trữ (f(n), g(n), vị trí hiện tại, đường đi, mục tiêu Pacman)
    pq = []
    visited = {start}
    
    def find_nearest_pacman(pos):
        if not pacman_positions:
            return None
        return min(pacman_positions, key=lambda p: manhattan(pos, p))

    # Chọn Pacman gần nhất từ vị trí start
    target = find_nearest_pacman(start)
    if target is None:
        return []

    # Thêm vị trí start vào hàng đợi với mục tiêu là Pacman gần nhất
    h = manhattan(start, target)
    heapq.heappush(pq, (h, 0, start, [], target))
    
    while pq:
        # Lấy nút có f(n) nhỏ nhất
        f, g, (r, c), path, current_target = heapq.heappop(pq)
        
        if (r, c) == current_target:
            return path + [(r, c)] # Tìm thấy đường đi
        
        # Kiểm tra các bước đi lân cận (lên, xuống, trái, phải)
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and (nr, nc) not in wall_positions:
                visited.add((nr, nc))
                new_g = g + 1  # Chi phí từ start đến vị trí mới
                
                # Tìm Pacman gần nhất từ vị trí mới
                new_target = find_nearest_pacman((nr, nc))
                if new_target is None:
                    continue
                
                h = manhattan((nr, nc), new_target)  # Ước lượng chi phí 
                f = new_g + h  # Tổng chi phí 
                heapq.heappush(pq, (f, new_g, (nr, nc), path + [(nr, nc)], new_target))
    
    return []  # Không tìm thấy đường đi
