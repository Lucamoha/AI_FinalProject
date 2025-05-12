from Algorithms.utils import *
from constants import *
from collections import defaultdict
import random
import os
import pickle

_continue_learning = True # True nếu muốn tiếp tục học
_tolerance = 0.01 # Ngưỡng dừng
_alpha = 0.3  # Tốc độ học
_gamma = 0.9  # Hệ số chiết khấu 
_epsilon = 0.2  # Tỷ lệ khám phá
_episodes = 4000 # Số vòng lặp học
_limitStep = 1000 # Số bước tối đa trong mỗi episode

_map = 1
_level = 1
_food_positions = []
_ghost_positions = []
_wall_positions = []
Q_table = None

def _load_q_table():
    path = os.path.join("Algorithms\\qtables", f"qtable_L{_level}_M{_map}.pkl")
    if os.path.exists(path):
        with open(path, "rb") as f:
            return defaultdict(float, pickle.load(f))
    return defaultdict(float)

def _save_q_table():
    os.makedirs("Algorithms\\qtables", exist_ok=True)
    path = os.path.join("Algorithms\\qtables", f"qtable_L{_level}_M{_map}.pkl")
    with open(path, "wb") as f:
        pickle.dump(dict(Q_table), f)

def _take_action(state: tuple, action: tuple):
    """
    Thực hiện hành động trên trạng thái hiện tại và trả về trạng thái mới.
    """
    new_state = state
    x, y = state
    dx, dy = action
    new_x, new_y = x + dx, y + dy
    new_state = (new_x, new_y)
    
    if new_state in _food_positions:
        return new_state, 10 # Thưởng khi ăn thức ăn
    elif new_state in _wall_positions:
        return state, -1
    elif new_state in _ghost_positions:
        return new_state, -100
    else:
        return new_state, -1 # phạt

def _choose_action(state: tuple) -> tuple:
    if random.uniform(0, 1) < _epsilon:
        return random.choice(MOVES)

    min_food_dist = distance(state, _food_positions)
    min_ghost_dist = distance(state, _ghost_positions) if _ghost_positions else -1
    s = (state, min_food_dist, min_ghost_dist)

    best_score = float('-inf')
    best_action = None

    for action in MOVES:
        new_state, _ = _take_action(state, action)
        q_val = Q_table[(s, action)]
        h_val = heuristic(new_state, _food_positions, _ghost_positions, alpha=2)

        score = q_val - 0.1 * h_val  # trọng số 0.1 để Q vẫn chiếm ưu thế
        if score > best_score:
            best_score = score
            best_action = action

    return best_action

def _return_path(start: tuple) -> list:
    path = []
    state = start
    visited = set()

    for i in range(_limitStep):
        if state in _food_positions:
            break

        min_food_dist = distance(state, _food_positions)
        min_ghost_dist = distance(state, _ghost_positions) if _ghost_positions else -1
        s = (state, min_food_dist, min_ghost_dist)
        
        best_action = 0
        t = float('-inf')
        for action in MOVES:
            q_val = Q_table[(s, action)]
            if q_val > t:
                t = q_val
                best_action = MOVES.index(action)

        if (s, best_action) in visited:
            break
        visited.add((s, best_action))

        new_state, _ = _take_action(state, MOVES[best_action])
        path.append(new_state)
        state = new_state
    return path

def QLearning(start: tuple, food_positions: list[tuple], ghost_positions: list[tuple], wall_positions: list[tuple], map: int = 1, level: int = 1) -> list:
    global Q_table
    global _map, _level
    _map, _level = map, level
    global _food_positions, _ghost_positions, _wall_positions
    _food_positions, _ghost_positions, _wall_positions = food_positions, ghost_positions, wall_positions

    Q_table = _load_q_table()

    if not _continue_learning:
        return _return_path(start)

    for episode in range(_episodes):
        state = start
        max_delta = 0

        for _ in range(_limitStep):
            min_food_dist = distance(state, _food_positions)
            min_ghost_dist = distance(state, _ghost_positions) if _ghost_positions else -1
            s = (state, min_food_dist, min_ghost_dist)

            action = _choose_action(state)
            new_state, reward = _take_action(state, action)
            new_min_food_dist = distance(new_state, _food_positions)
            new_min_ghost_dist = distance(new_state, _ghost_positions) if _ghost_positions else -1
            ns = (new_state, new_min_food_dist, new_min_ghost_dist)

            old_value = Q_table[(s, action)]
            next_max = max([Q_table[(ns, a)] for a in MOVES])
            Q_table[(s, action)] += _alpha * (reward + _gamma * next_max - old_value)

            state = new_state
            max_delta = max(max_delta, abs(old_value - Q_table[(s, action)]))

            if state in _food_positions:
                break

        print(f"Episode {episode + 1}/{_episodes}, max delta: {max_delta:}") # debug
        if max_delta < _tolerance:
            break

    _save_q_table()
    return _return_path(start)