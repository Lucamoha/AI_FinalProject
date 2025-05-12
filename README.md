# 🎮 Đồ Án Cuối Kỳ - Trí Tuệ Nhân Tạo (Artificial Intelligence)

## 📑 Bảng nội dung

1. [Giới thiệu tổng quan về trò chơi](#giới-thiệu-tổng-quan-về-dự-án)
2. [Mục tiêu của trò chơi](#mục-tiêu-của-trò-chơi)
3. [Các cấp độ (levels)](#các-cấp-độ-levels)
4. [Cách tính điểm](#cách-tính-điểm)
5. [Công nghệ sử dụng](#công-nghệ-sử-dụng)
6. [Cách chạy trò chơi](#cách-chạy-trò-chơi)
7. [Các thành viên nhóm](#thành-viên-nhóm)
8. [Các thuật toán được sử dụng trong trò chơi](#-các-thuật-toán-được-sử-dụng-trong-trò-chơi)

## 🧠 Giới thiệu tổng quan về dự án

Sau khi tiếp thu kiến thức về các nhóm thuật toán trong trí tuệ nhân tạo (AI), nhóm chúng tôi đã quyết định áp dụng những kiến thức đó vào việc giải quyết một bài toán thực tiễn: phát triển trò chơi Pacman. Đây là một trò chơi phổ biến, có cấu trúc phù hợp để triển khai nhiều thuật toán AI đã học như tìm đường, ra quyết định và học tăng cường. Trò chơi được xây dựng bằng thư viện **Pygame**, một thư viện mạnh mẽ hỗ trợ phát triển game bằng ngôn ngữ lập trình Python. Việc lựa chọn Pacman giúp nhóm có điều kiện thuận lợi để tích hợp và kiểm nghiệm hiệu quả của các thuật toán AI trong môi trường tương tác thực tế.

## 🎯 Mục tiêu của trò chơi

Người chơi điều khiển nhân vật **Pacman** với nhiệm vụ:

* Ăn càng nhiều **thức ăn** càng tốt.
* **Tránh va chạm** với các con **quái vật**.
* **Không được đi vào tường**.
* Game sẽ kết thúc nếu **Pacman** ăn hết thức ăn hoặc va chạm với quái

## 🗺️ Các cấp độ (Levels)

| Level | Mô tả                                                                                 |
| ----- | ------------------------------------------------------------------------------------- |
| **1** | Không có quái vật, chỉ có 1 thức ăn.                                                  |
| **2** | Có quái vật (không di chuyển), có 1 thức ăn.                                          |
| **3** | Có quái vật di chuyển **ngẫu nhiên**, có **nhiều thức ăn**.                           |
| **4** | Quái vật di chuyển theo thuật toán **A\*** để đuổi theo Pacman, có **nhiều thức ăn**. |
| **5** | Giống level 4 nhưng **mỗi 20 bước** sẽ có thêm **1 quái vật mới**, có nhiều thức ăn.  |

## 🧮 Cách tính điểm

* **Điểm khởi đầu**: `0`
* **Di chuyển 1 bước**: `-1 điểm`
* **Ăn 1 quả**: `+10 điểm`

## 🛠️ Công nghệ sử dụng

* Python 3.x
* \[Pygame]


## 🚀 Cách chạy trò chơi

```bash
# Clone repo từ github
git clone https://github.com/Lucamoha/AI_FinalProject.git

# Cài đặt thư viện Pygame
pip install pygame

# Chạy game
python main.py
```

## 🧑‍💻 Thành viên nhóm
* [Trần Triều Dương - 23110200](https://github.com/Lucamoha)
* [Văn Phú Hiền - 23110213](https://github.com/VanPhuHien)
* [Nguyễn Văn Kế - 23110234](https://github.com/nvk3005)

## 📊 Các thuật toán được sử dụng trong trò chơi
- [I. Uninformed Search - BFS](#i-uninformed-search---bfs)
- [II. Informed Search - A*](#ii-informed-search---a)
- [III. Local Search - Local Beam Search](#iii-local-search---local-beam-search)
- [IV. Searching with Nondeterminism: Searching with Partially Observation](#iv-searching-with-nondeterminism-searching-with-partially-observation)
- [V. Constraint Satisfaction: Backtracking](#v-constraint-satisfaction-backtracking)
- [VI. Reinforcement Learning: Q-Learning](#vi-reinforcement-learning-q-learning)

### I. Uninformed Search - BFS
|Hình ảnh khi chạy thuật toán|Kết quả khi áp dụng thuật toán|
| :--- | :---|

### II. Informed Search - A*
|Hình ảnh khi chạy thuật toán|Kết quả khi áp dụng thuật toán|
| :--- | :---|

### III. Local Search - Local Beam Search
|Hình ảnh khi chạy thuật toán|Kết quả khi áp dụng thuật toán|
| :--- | :---|

### IV. Searching with Nondeterminism: Searching with Partially Observation
|Hình ảnh khi chạy thuật toán|Kết quả khi áp dụng thuật toán|
| :--- | :---|

### V. Constraint Satisfaction: Backtracking
|Hình ảnh khi chạy thuật toán|Kết quả khi áp dụng thuật toán|
| :--- | :---|

### VI. Reinforcement Learning: Q-Learning
|Hình ảnh khi chạy thuật toán|Kết quả khi áp dụng thuật toán|
| :--- | :---|
