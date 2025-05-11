from constants import * 
from Algorithms.utils import distance

def Backtracking(start: tuple, food_positions: list, ghost_positions: list, wall_positions: list, max_depth=30):
    """
    Backtracking để tìm đường đi từ Pacman tới thức ăn, thoả mãn ràng buộc:
    - Không đụng ghost
    - Không đi vào tường
    - Không lặp lại
    """

    # Biến: các bước di chuyển từ 0 → max_depth
    # Miền giá trị: các hướng hợp lệ tại mỗi bước
    # Ràng buộc sẽ được kiểm tra tại mỗi bước

    visited = set()
    
    def solve(current_pos, path, depth):
        # Kiểm tra nếu đã đi quá độ sâu cho phép
        if depth > max_depth:
            return None
        
        # Trả về đường đi nếu tìm thấy thức ăn
        if current_pos in food_positions:
            return path + [current_pos] 
        
        # Đánh dấu vị trí hiện tại đã thăm
        visited.add(current_pos)
        
        # Khởi tạo danh sách các bước đi tiếp theo có thể
        next_moves = []
        r, c = current_pos
        
        # Xét tất cả các hướng di chuyển có thể
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            new_pos = (nr, nc)
            
            # Kiểm tra nếu vị trí mới hợp lệ và chưa thăm
            if new_pos not in visited and new_pos not in wall_positions and new_pos not in ghost_positions:
                # Tính khoảng cách đến quái gần nhất
                ghost_dist = distance(new_pos, ghost_positions)
                
                # Thêm cả khoảng cách đến thức ăn gần nhất
                food_dist = distance(new_pos, food_positions)
                
                # Điểm đánh giá: ưu tiên xa quái và gần thức ăn
                score = ghost_dist - 0.5 * food_dist
                
                next_moves.append((new_pos, score))
        
        # Sắp xếp các bước đi theo điểm đánh giá
        next_moves.sort(key=lambda x: x[1], reverse=True)
        
        # Thử theo độ ưu tiên
        for new_pos, _ in next_moves:
            result = solve(new_pos, path + [current_pos], depth + 1)
            if result:
                return result
        
        # Quay lui
        visited.remove(current_pos)
        return None
    
    # Bắt đầu giải quyết từ vị trí ban đầu
    result = solve(start, [], 0)
    return result[1:] if result else []