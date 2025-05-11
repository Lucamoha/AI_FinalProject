def manhattan(pos1: tuple, pos2: tuple):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def distance(pos: tuple, positions: list):
    """Tính khoảng cách Manhattan đến đối tượng gần nhất."""
    if not positions:
        return float('inf')
    return min(manhattan(pos, g) for g in positions)

def heuristic(pos: tuple, food_positions: list, ghost_positions: list, alpha = 2):
    """
    Hàm chi phí (cost function) cho Pacman với ưu tiên:
    - Tới gần thức ăn nhất
    - Tránh xa quái nhất
    
    alpha quyết định mức độ ưu tiên né quái so với việc ăn nhanh: 
    - alpha = 1 là cân bằng
    - alpha > 1 là ưu tiên né quái hơn
    - alpha < 1 là ưu tiên ăn thức ăn hơn

    **Chi phí càng thấp thì càng tốt**
    """
    min_food_dist = distance(pos, food_positions)
    min_ghost_dist = distance(pos, ghost_positions)
    return min_food_dist + alpha / (min_ghost_dist + 1)