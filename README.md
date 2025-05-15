# 🎮 Đồ Án Cuối Kỳ - Trí Tuệ Nhân Tạo (Artificial Intelligence)

## 📑 Bảng nội dung

1. [Giới thiệu tổng quan về trò chơi](#-giới-thiệu-tổng-quan-về-dự-án)
2. [Mục tiêu của trò chơi](#-mục-tiêu-của-trò-chơi)
3. [Các cấp độ (levels)](#%EF%B8%8F-các-cấp-độ-levels)
4. [Cách tính điểm](#-cách-tính-điểm)
5. [Công nghệ sử dụng](#%EF%B8%8F-công-nghệ-sử-dụng)
6. [Cách chạy trò chơi](#-cách-chạy-trò-chơi)
7. [Các thành viên nhóm](#-thành-viên-nhóm)
8. [Các thuật toán được sử dụng trong trò chơi](#-các-thuật-toán-được-sử-dụng-trong-trò-chơi)
9. [So sánh hiệu suất các thuật toán](#-so-sánh-hiệu-suất-các-thuật-toán)

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
| **5** | Giống level 4 nhưng **mỗi 20 bước** sẽ có thêm **1 quái vật mới**.  |

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
cd AI_FinalProject/Pacman_Game

# Cài đặt thư viện cần thiết
pip install -r requirements.txt

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
|Hình ảnh khi chạy thuật toán|Kết quả khi áp dụng thuật toán|Đường đi của thuật toán|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/3a819ad1-4cc5-4a7a-a49b-10df2549939d)|--Level: 2 - Map: 3 - Algo: BFS--<br>Status: Win<br>Steps: 19<br>Food: 1<br>Score: -9<br>Time: 0.006945200000245677s|[Đường đi của thuật toán BFS](https://raw.githubusercontent.com/Lucamoha/AI_FinalProject/refs/heads/main/Path_AStar_BFS_BeamSearch/BFS.txt)|

### II. Informed Search - A*
|Hình ảnh khi chạy thuật toán|Kết quả khi áp dụng thuật toán|Đường đi của thuật toán|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/ccae3290-a333-4f63-bc9b-5f835140fb14)|--Level: 2 - Map: 3 - Algo: A_Star--<br>Status: Win<br>Steps: 19<br>Food: 1<br>Score: -9<br>Time: 0.003884499999912805s|[Đường đi của thuật toán A*](https://raw.githubusercontent.com/Lucamoha/AI_FinalProject/refs/heads/main/Path_AStar_BFS_BeamSearch/A_Star.txt)|

### III. Local Search - Local Beam Search
#### a. BeamWidth = 1
|Hình ảnh khi chạy thuật toán|Kết quả khi áp dụng thuật toán|Đường đi của thuật toán|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/63fa7e67-dcc6-47fa-8d4e-ff7d5ea87d14)|--Level: 2 - Map: 3 - Algo: BeamSearch--<br>Status: Win<br>Steps: 41<br>Food: 1<br>Score: -31<br>Time: 0.004805000000033033s|[Đường đi của thuật toán BeamSearch với BeamWidth = 1](https://raw.githubusercontent.com/Lucamoha/AI_FinalProject/refs/heads/main/Path_AStar_BFS_BeamSearch/BeamSearch_Width%3D1.txt)|

#### b. BeamWidth = 2
|Hình ảnh khi chạy thuật toán|Kết quả khi áp dụng thuật toán|Đường đi của thuật toán|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/fd1ce190-0d12-41e6-8f09-9aadc2f33777)|--Level: 2 - Map: 3 - Algo: BeamSearch--<br>Status: Win<br>Steps: 19<br>Food: 1<br>Score: -9<br>Time: 0.0016415999998571351s|[Đường đi của thuật toán BeamSearch với BeamWidth = 2](https://raw.githubusercontent.com/Lucamoha/AI_FinalProject/refs/heads/main/Path_AStar_BFS_BeamSearch/BeamSearch_Width%3D2.txt)|

#### b. BeamWidth = 3
|Hình ảnh khi chạy thuật toán|Kết quả khi áp dụng thuật toán|Đường đi của thuật toán|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/4b5e4bf9-965c-4659-9c9a-ba9a2157fb1a)|--Level: 2 - Map: 3 - Algo: BeamSearch--<br>Status: Win<br>Steps: 19<br>Food: 1<br>Score: -9<br>Time: 0.005931900000177848s|[Đường đi của thuật toán BeamSearch với BeamWidth = 3](https://raw.githubusercontent.com/Lucamoha/AI_FinalProject/refs/heads/main/Path_AStar_BFS_BeamSearch/BeamSearch_Width%3D3.txt)|


### IV. Searching with Nondeterminism: Searching with Partially Observation
|Hình ảnh khi chạy thuật toán|Kết quả khi áp dụng thuật toán|
| :--- | :---|
|![Image](https://github.com/user-attachments/assets/653acd08-86f3-4a4c-b518-ba1216452521)|--Level: 2 - Map: 3 - Algo: Partial_Observation--<br>Status: Win<br>Steps: 19<br>Food: 1<br>Score: -9<br>Time: 0.03737750000027518s|

### V. Constraint Satisfaction: Backtracking
|Hình ảnh khi chạy thuật toán|Kết quả khi áp dụng thuật toán|
| :--- | :---|
|![Image](https://github.com/user-attachments/assets/4e37087c-3b6e-4738-9360-9a4b580d5e95)|--Level: 2 - Map: 3 - Algo: Backtracking--<br>Status: Win<br>Steps: 29<br>Food: 1<br>Score: -19<br>Time: 0.007194500000423432s|


### VI. Reinforcement Learning: Q-Learning
|Hình ảnh khi chạy thuật toán|Kết quả khi áp dụng thuật toán|
| :--- | :---|
|![Image](https://github.com/user-attachments/assets/598838e3-51cc-48c2-8171-3a34a5e7a169)|--Level: 2 - Map: 3 - Algo: QLearning--<br>Status: Win<br>Steps: 19<br>Food: 1<br>Score: -9<br>Time: 0.27460940000037226s|

## 📈 So sánh hiệu suất các thuật toán
### So sánh hiệu suất khi áp dụng một thuật toán cho nhiều cấp độ (level)
<table>
  <thead>
    <tr>
      <th>Thuật toán</th>
      <th>Minh họa kết quả</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>BFS</b></td>
      <td><img src="https://github.com/user-attachments/assets/0b7678c2-34a8-4119-845b-2563edcf31d8" width="400"/></td>
    </tr>
    <tr>
      <td><b>A*</b></td>
      <td><img src="https://github.com/user-attachments/assets/c692b62f-e190-4717-9b46-f287f1755b09" width="400"/></td>
    </tr>
    <tr>
      <td><b>Local Beam Search</b></td>
      <td><img src="https://github.com/user-attachments/assets/62f0704f-204d-4c42-b038-e8fc8c06aaa7" width="400"/></td>
    </tr>
    <tr>
      <td><b>Partial Observation Search</b></td>
      <td><img src="https://github.com/user-attachments/assets/367d6cf3-7c0a-4602-8263-a5a2726bbcb1" width="400"/></td>
    </tr>
    <tr>
      <td><b>Backtracking</b></td>
      <td><img src="https://github.com/user-attachments/assets/790743eb-b6e9-4885-85ac-91e4b2d95e71" width="400"/></td>
    </tr>
    <tr>
      <td><b>Q-Learning</b></td>
      <td><img src="https://github.com/user-attachments/assets/7367ab27-329c-456d-bc8d-aef1cae12cf7" width="400"/></td>
    </tr>
  </tbody>
</table>

### So sánh hiệu suất khi áp dụng nhiều thuật toán cho một cấp độ (level) duy nhất
<table>
  <thead>
    <tr>
      <th>Level</th>
      <th>Minh họa kết quả</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Level 1</b></td>
      <td><img src="https://github.com/user-attachments/assets/3aee6c31-641e-4857-bec9-826a8657e05a" width="400"/></td>
    </tr>
    <tr>
      <td><b>Level 2</b></td>
      <td><img src="https://github.com/user-attachments/assets/a79eb3a2-52d9-4b43-9168-bceeead2c617" width="400"/></td>
    </tr>
    <tr>
      <td><b>Level 3</b></td>
      <td><img src="https://github.com/user-attachments/assets/34841215-3624-433c-af0c-24ebc1f24f81" width="400"/></td>
    </tr>
    <tr>
      <td><b>Level 4</b></td>
      <td><img src="https://github.com/user-attachments/assets/05c9b48c-48cf-4701-80f7-6a1ae775df5f" width="400"/></td>
    </tr>
    <tr>
      <td><b>Level 5</b></td>
      <td><img src="https://github.com/user-attachments/assets/c089c934-21d2-47da-8ec0-44d53d502ee3" width="400"/></td>
    </tr>
  </tbody>
</table>

