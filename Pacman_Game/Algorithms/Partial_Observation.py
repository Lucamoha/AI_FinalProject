from Algorithms.utils import manhattan
from Algorithms.BFS import BFS

def update_belief(belief_state: dict, pacman_pos: tuple, observed_ghosts: list, observed_food: list, wall_positions: list, _N: int, _M: int) -> tuple[dict, list]:
    """Cập nhật trạng thái niềm tin cho quái và thức ăn dựa trên quan sát mới."""
    OBSERVATION_RADIUS = 2
    new_belief = {'ghosts': set(), 'food': set()}

    # Tìm các ô trong phạm vi quan sát
    observable_positions = set()
    for r in range(-OBSERVATION_RADIUS, OBSERVATION_RADIUS + 1):
        for c in range(-OBSERVATION_RADIUS, OBSERVATION_RADIUS + 1):
            if abs(r) + abs(c) <= OBSERVATION_RADIUS:
                new_pos = (pacman_pos[0] + r, pacman_pos[1] + c)
                if 0 <= new_pos[0] < _N and 0 <= new_pos[1] < _M and new_pos not in wall_positions:
                    observable_positions.add(new_pos)

    # Cập nhật niềm tin về quái
    if observed_ghosts:
        new_belief['ghosts'].update([pos for pos in observed_ghosts if pos != pacman_pos])
    else:
        for pos in belief_state['ghosts']:
            if pos not in observable_positions and pos not in wall_positions and pos != pacman_pos:
                new_belief['ghosts'].add(pos)

    # Cập nhật niềm tin về thức ăn
    if observed_food:
        new_belief['food'].update(observed_food)
    else:
        for pos in belief_state['food']:
            if pos not in observable_positions and pos not in wall_positions:
                new_belief['food'].add(pos)

    updated_food_positions = [pos for pos in new_belief['food'] if pos != pacman_pos]
    new_belief['food'] = set(updated_food_positions)

    return new_belief, updated_food_positions


def Partial_Observation(pacman_start: tuple, food_positions: list, initial_ghost_positions: list, wall_positions: list, _N: int, _M: int) -> list:
    """Tìm kiếm với quan sát một phần, sử dụng BFS để Pacman ăn thức ăn và né quái."""
    # Khởi tạo trạng thái niềm tin
    belief_state = {
        'ghosts': set(pos for pos in initial_ghost_positions if pos != pacman_start) if initial_ghost_positions else set(),
        'food': set(food_positions) if food_positions else set(
            (r, c) for r in range(_N) for c in range(_M) if (r, c) not in wall_positions
        )
    }

    # Giả sử quan sát ban đầu
    observed_ghosts = [pos for pos in belief_state['ghosts'] if manhattan(pacman_start, pos) <= 2]
    observed_food = [pos for pos in belief_state['food'] if manhattan(pacman_start, pos) <= 2]
    belief_state, updated_food_positions = update_belief(belief_state, pacman_start, observed_ghosts, observed_food, wall_positions, _N, _M)

    # Chọn ô thức ăn gần nhất trong belief_state['food']
    if belief_state['food']:
        closest_food = min(belief_state['food'], key=lambda pos: manhattan(pacman_start, pos))
        path = BFS(pacman_start, [closest_food], list(belief_state['ghosts']), wall_positions)
    else:
        path = []

    # Nếu BFS không tìm được đường, thử di chuyển ngẫu nhiên
    if not path and belief_state['food']:
        ghost_obstacles = list(belief_state['ghosts'])
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            next_pos = (pacman_start[0] + dr, pacman_start[1] + dc)
            if (0 <= next_pos[0] < _N and 0 <= next_pos[1] < _M and
                next_pos not in wall_positions and next_pos not in ghost_obstacles):
                path = [next_pos]
                break

    return path