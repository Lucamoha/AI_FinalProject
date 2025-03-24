

def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def distance_to_ghost(pos, ghost_positions):
    """Tính khoảng cách Manhattan đến quái gần nhất."""
    if not ghost_positions:
            return float('inf')
    return min(manhattan(pos, g) for g in ghost_positions)
