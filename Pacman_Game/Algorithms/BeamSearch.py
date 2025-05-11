from Algorithms.utils import heuristic
from constants import MOVES

def BeamSearch(start: tuple, food_positions: list, ghost_positions: list, wall_positions: list, beam_width: int = 3):
    queue = [(heuristic(start, food_positions, ghost_positions), [start])]
    visited = set([start])

    while queue:
        candidates = []

        for _, path in queue:
            current = path[-1]
            if current in food_positions:
                return path[1:]

            r, c = current
            for dr, dc in MOVES:
                nr, nc = r + dr, c + dc
                neighbor = (nr, nc)

                if (neighbor in visited or neighbor in wall_positions or neighbor in ghost_positions):
                    continue

                visited.add(neighbor)
                new_path = path + [neighbor]
                h = heuristic(neighbor, food_positions, ghost_positions)
                candidates.append((h, new_path))

        # Giữ lại beam_width ứng viên tốt nhất
        queue = sorted(candidates)[:beam_width]

    return []