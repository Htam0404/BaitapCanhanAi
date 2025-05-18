# BÁO CÁO ĐỒ ÁN: ỨNG DỤNG CÁC THUẬT TOÁN TÌM KIẾM TRONG BÀI TOÁN 8 Ô CHỮ

## 1. MỤC TIÊU

Mục tiêu chính của đồ án là nghiên cứu, phân tích sâu và triển khai ứng dụng các thuật toán tìm kiếm khác nhau nhằm giải quyết hiệu quả bài toán 8 ô chữ. Thông qua dự án này, chúng tôi chứng minh khả năng hiện thực hóa các thuật toán tìm kiếm có thông tin và không có thông tin, đồng thời tiến hành đánh giá định lượng hiệu suất của từng phương pháp khi áp dụng vào bối cảnh trò chơi.

## 2. NỘI DUNG NGHIÊN CỨU

### 2.1. Các Thuật Toán Tìm Kiếm Không Có Thông Tin (Uninformed Search Algorithms)

#### 2.1.1. Phân tích Bài Toán Tìm Kiếm và Định nghĩa Solution

Bài toán 8 ô chữ, một bài toán kinh điển trong lĩnh vực Trí tuệ Nhân tạo, được cấu thành bởi các yếu tố cơ bản sau:

- **Trạng thái (State)**: Biểu diễn cấu hình hiện tại của trò chơi thông qua ma trận vuông 3x3.
- **Trạng thái Ban Đầu (Initial State)**: Cấu hình ma trận 3x3 xác định vị trí xuất phát của các ô số.
- **Trạng thái Mục Tiêu (Goal State)**: Cấu hình ma trận 3x3 mong muốn đạt được.
- **Hành động (Actions)**: Các thao tác di chuyển ô trống (giá trị 0) theo bốn hướng: lên, xuống, trái, phải.
- **Hàm Chuyển Trạng Thái (Transition Function)**: Quy tắc xác định trạng thái kế tiếp sau khi thực hiện một hành động hợp lệ.
- **Kiểm tra Mục Tiêu (Goal Test)**: Hàm boolean đánh giá xem trạng thái hiện tại có trùng với trạng thái mục tiêu hay không.
- **Chi phí Đường đi (Path Cost)**: Số lượng hành động (di chuyển) đã thực hiện để đạt đến trạng thái hiện tại từ trạng thái ban đầu.

**Solution (Lời giải)** cho bài toán 8 ô chữ được định nghĩa là một chuỗi tối ưu các hành động (di chuyển) từ trạng thái ban đầu đến trạng thái mục tiêu, tối thiểu hóa chi phí đường đi.

#### 2.1.2. Trực Quan Hóa Thuật Toán

Ứng dụng đồ họa được phát triển cho phép trực quan hóa quá trình tìm kiếm của các thuật toán không có thông tin, bao gồm:

#### Tìm kiếm theo chiều sâu (Depth-First Search - DFS)
  Nguyên tắc hoạt động: DFS tìm kiếm theo cách đi sâu vào cây tìm kiếm, mở rộng từng nhánh con cho đến khi không thể tiếp tục, rồi quay lại và mở rộng các nhánh khác. Quá trình này tiếp diễn cho đến khi tìm thấy trạng thái mục tiêu hoặc không còngi nhánh để mở rộng.
  Hàm đánh giá: Không có hàm heuristic, chỉ dựa vào việc mở rộng các trạng thái theo chiều sâu.
  Ưu điểm: Tiết kiệm bộ nhớ vì chỉ cần lưu trữ các trạng thái dọc theo con đường tìm kiếm hiện tại.
  Nhược điểm: Không đảm bảo sẽ tìm thấy lời giải tối ưu và có thể bị rơi vào vòng lặp vô hạn nếu không xử lý đúng.

![DFS](https://github.com/user-attachments/assets/482d9fcd-5b8a-4891-a406-b13c61afea2d)


#### Tìm kiếm theo chiều rộng (Breadth-First Search - BFS)
  Nguyên tắc hoạt động: BFS tìm kiếm theo cách mở rộng tất cả các trạng thái ở cùng một mức độ trước khi chuyển sang mức độ sâu hơn. Quá trình này tiếp tục cho đến khi tìm thấy trạng thái mục tiêu.
  Hàm đánh giá: Không có hàm heuristic, tất cả các trạng thái được mở rộng theo thứ tự chiều rộng.
  Ưu điểm: Đảm bảo tìm thấy lời giải tối ưu nếu có.
  Nhược điểm: Tốn nhiều bộ nhớ vì phải lưu trữ tất cả các trạng thái ở cùng một mức độ.

![BFS](https://github.com/user-attachments/assets/e2500ea9-b409-45d9-a190-5a7b5444d468)


 #### Tìm kiếm chi phí đồng nhất (Uniform-Cost Search - UCS)
  Nguyên tắc hoạt động: UCS tìm kiếm theo chi phí nhỏ nhất, tức là mở rộng các trạng thái có chi phí thấp nhất từ điểm bắt đầu đến trạng thái hiện tại. Quá trình này tiếp tục cho đến khi tìm thấy trạng thái mục tiêu.
  Hàm đánh giá: f(n) = g(n), trong đó g(n) là chi phí đường đi từ trạng thái ban đầu đến trạng thái n.
  Ưu điểm: Đảm bảo tìm được lời giải tối ưu.
  Nhược điểm: Tốn nhiều bộ nhớ và thời gian, vì phải tính toán và lưu trữ các chi phí của các trạng thái.

![UCS](https://github.com/user-attachments/assets/bee84120-12a6-4022-acd9-631948c69e6a)



#### Tìm kiếm sâu dần (Iterative Deepening Depth-First Search - IDDFS)
  Nguyên tắc hoạt động: IDDFS kết hợp giữa DFS và BFS, thực hiện tìm kiếm theo chiều sâu nhưng với mức độ tìm kiếm giới hạn. Mỗi lần tìm kiếm, mức độ giới hạn được tăng lên, giúp đảm bảo sẽ mở rộng tất cả các trạng thái theo thứ tự tăng dần chiều sâu cho đến khi tìm thấy mục tiêu.
  Hàm đánh giá: Không có hàm heuristic, chỉ dựa vào chiều sâu của trạng thái trong cây tìm kiếm.
  Ưu điểm: Tiết kiệm bộ nhớ hơn BFS, và vẫn đảm bảo tìm được lời giải tối ưu.
  Nhược điểm: Có thể phải tính toán lại các trạng thái đã mở rộng nhiều lần.

![IDDFS](https://github.com/user-attachments/assets/bae46d52-425e-45a4-af6a-bbdb92f82492)


### 2.1.3. So sánh Hiệu Suất

Hiệu suất của các thuật toán được đánh giá dựa trên các tiêu chí định lượng như thời gian thực thi (execution time) và số lượng trạng thái đã khám phá (number of expanded nodes) để đạt được trạng thái mục tiêu.
![1](https://github.com/user-attachments/assets/fc55f0b0-c7f6-4fda-9613-ae1d55986b6d)

#### 2.1.4. Nhận Xét về Hiệu Suất

- **DFS**: Ưu điểm về bộ nhớ do chỉ duy trì nhánh tìm kiếm hiện tại. Tuy nhiên, có nguy cơ rơi vào vòng lặp vô hạn hoặc tìm thấy lời giải không tối ưu. Hiệu suất thực tế có thể kém trên không gian trạng thái lớn của bài toán 8 ô chữ.
- **BFS**: Đảm bảo tìm được lời giải tối ưu (số bước di chuyển ít nhất). Nhược điểm là tiêu tốn nhiều bộ nhớ để lưu trữ các nút ở cùng mức độ sâu. Hiệu suất phù hợp với bài toán 8 ô chữ có độ phức tạp vừa phải.
- **UCS**: Tương tự BFS, đảm bảo tìm được lời giải tối ưu khi chi phí các hành động khác nhau. Trong bài toán 8 ô chữ với chi phí mỗi bước đi là 1, hiệu suất tương đương BFS.
- **IDDFS**: Kết hợp ưu điểm tiết kiệm bộ nhớ của DFS và tính tối ưu của BFS. Tốn thời gian hơn do phải lặp lại việc tìm kiếm ở các độ sâu khác nhau.

### 2.2. Các Thuật Toán Tìm Kiếm Có Thông Tin (Informed Search Algorithms)

Các thuật toán này tận dụng thông tin heuristic để hướng dẫn quá trình tìm kiếm, nâng cao hiệu quả so với các thuật toán không có thông tin.

 #### Greedy Best-First Search (Tìm kiếm tham lam theo ưu tiên tốt nhất):  
![Greedy](https://github.com/user-attachments/assets/2b16b883-dfd3-47f5-9e5b-a8a4517d1515)

  
  - Hàm đánh giá (Evaluation function): f(n)=h(n), trong đó h(n) là hàm heuristic ước tính chi phí từ trạng thái n đến trạng thái mục tiêu.
  - Nguyên tắc hoạt động: Luôn chọn trạng thái có giá trị heuristic thấp nhất để mở rộng tiếp theo.
  - Ưu/nhược điểm: Nhanh chóng tìm ra lời giải nhưng không đảm bảo tính tối ưu. Dễ bị lạc vào các đường đi không hứa hẹn.

#### A* Search (Tìm kiếm A*):  

  ![Astar](https://github.com/user-attachments/assets/4386df07-5d06-4234-8e13-90dcc7245b3f)

  - Hàm đánh giá (Evaluation function): f(n)=g(n)+h(n), trong đó g(n) là chi phí đường đi từ trạng thái ban đầu đến trạng thái n, và h(n) là hàm heuristic ước tính chi phí từ trạng thái n đến trạng thái mục tiêu.
  - Nguyên tắc hoạt động: Ưu tiên mở rộng các trạng thái có tổng chi phí ước tính thấp nhất.
  - Ưu/nhược điểm: Đảm bảo tìm được lời giải tối ưu nếu hàm heuristic là chấp nhận được (admissible) và nhất quán (consistent). Có thể tốn nhiều bộ nhớ hơn các thuật toán khác.

#### IDA* Search (Tìm kiếm IDA*):  
![IDAStar](https://github.com/user-attachments/assets/e008d1c2-fdbe-4e50-b79b-ea1c64854484)

  
  - Hàm đánh giá (Evaluation function): Tương tự A*, sử dụng f(n)=g(n)+h(n).
  - Nguyên tắc hoạt động: Thực hiện tìm kiếm sâu dần (Iterative Deepening) với ngưỡng cắt dựa trên giá trị f(n). Bắt đầu với ngưỡng bằng h(initial), sau đó tăng dần ngưỡng lên giá trị f(n) nhỏ nhất vượt quá ngưỡng hiện tại của lần tìm kiếm trước.
  - Ưu/nhược điểm: Tiết kiệm bộ nhớ hơn A* vì không lưu trữ toàn bộ cây tìm kiếm. Vẫn đảm bảo tính tối ưu nếu heuristic chấp nhận được. Có thể tính toán lại các trạng thái nhiều lần.
  **Nhận xét**:
  - Greedy có thể giúp tìm ra giải pháp nhanh chóng nhưng không đảm bảo tính tối ưu
  -  A* lại cung cấp giải pháp tối ưu hơn với sự đánh giá toàn diện giữa chi phí đi qua các trạng thái và chi phí ước tính từ trạng thái hiện tại tới mục tiêu.
  - IDA* là một sự lựa chọn lý tưởng khi bộ nhớ là một yếu tố hạn chế, mặc dù nó có thể tốn thời gian tính toán hơn
 
  **So Sánh**: 
![2](https://github.com/user-attachments/assets/9c487862-a0b9-45e9-b148-df983f6fd000)

### 2.3. Các Thuật Toán Tìm Kiếm Cục Bộ (Local Search Algorithms)

Tập trung vào việc tối ưu hóa trạng thái hiện tại để tìm ra trạng thái mục tiêu, không quan tâm đến đường đi.

#### Simple Hill Climbing (Leo đồi đơn giản)

- **Hàm đánh giá**: Sử dụng hàm heuristic `h(n)` để đánh giá trạng thái.

- **Nguyên tắc hoạt động**:
  1. Bắt đầu từ một trạng thái hiện tại.
  2. Chọn ngẫu nhiên **một** trạng thái lân cận.
  3. Nếu trạng thái đó tốt hơn → di chuyển đến đó.
  4. Nếu không tốt hơn → giữ nguyên trạng thái hiện tại.
  5. Lặp lại cho đến khi không còn trạng thái nào tốt hơn.

- **Ưu điểm**:
  - Đơn giản, dễ cài đặt.
  
- **Nhược điểm**:
  - Dễ bị kẹt tại cực trị địa phương.
  - Có thể bỏ qua các trạng thái tốt hơn nếu không chọn trúng.

---

#### Steepest-Ascent Hill Climbing (Leo đồi theo hướng dốc nhất)

- **Hàm đánh giá**: Heuristic `h(n)`.

- **Nguyên tắc hoạt động**:
  1. Bắt đầu từ một trạng thái hiện tại.
  2. Tạo tất cả các trạng thái lân cận.
  3. Chọn **trạng thái tốt nhất** trong các lân cận.
  4. Nếu tốt hơn → di chuyển đến đó.
  5. Nếu không có trạng thái nào tốt hơn → dừng lại (kẹt ở local optimum).

- **Ưu điểm**:
  - Tốt hơn Simple Hill Climbing vì luôn chọn hướng tối ưu nhất tại mỗi bước.

- **Nhược điểm**:
  - Cũng dễ bị kẹt ở local optimum, plateau hoặc ridge.
  - Tốn nhiều tài nguyên hơn vì phải đánh giá tất cả các lân cận.

---

#### Random-Restart Hill Climbing (Leo đồi khởi động lại ngẫu nhiên)

- **Ý tưởng chính**:  
  Nếu một lần leo đồi bị kẹt tại cực trị địa phương, hãy **bắt đầu lại từ một trạng thái ngẫu nhiên mới** và tiếp tục leo.

- **Nguyên tắc hoạt động**:
  1. Thực hiện Simple hoặc Steepest-Ascent Hill Climbing.
  2. Nếu bị kẹt tại cực trị địa phương → khởi động lại từ trạng thái ngẫu nhiên.
  3. Lặp lại quá trình này cho đến khi tìm thấy lời giải đủ tốt hoặc đạt giới hạn số lần thử.

- **Ưu điểm**:
  - Có khả năng thoát khỏi local optima.
  - Tăng xác suất tìm được lời giải tối ưu toàn cục.

- **Nhược điểm**:
  - Cần thêm tài nguyên tính toán cho nhiều lần thử.
  - Không chắc chắn tìm ra lời giải tối ưu nếu số lần thử giới hạn.

---

#### Simulated Annealing (Mô phỏng luyện kim):  
  - Tham số: Nhiệt độ T (giảm dần theo thời gian), hàm giảm nhiệt độ.
  - Nguyên tắc hoạt động: Bắt đầu với một trạng thái hiện tại và nhiệt độ cao. Tại mỗi bước, chọn một trạng thái lân cận ngẫu nhiên. Nếu trạng thái lân cận tốt hơn, di chuyển đến đó. Nếu không tốt hơn, vẫn có một xác suất nhất định (phụ thuộc vào nhiệt độ và độ "tệ" của trạng thái lân cận) để di chuyển đến đó. Nhiệt độ giảm dần theo thời gian, làm giảm xác suất chấp nhận các di chuyển xấu hơn.

#### Genetic Algorithm (Thuật toán di truyền):  
  - Các thành phần chính:
    - Quần thể (Population): Một tập hợp các cá thể (trạng thái).
    - Hàm fitness (Fitness function): Đánh giá chất lượng của mỗi cá thể.
    - Chọn lọc (Selection): Chọn các cá thể tốt nhất để sinh sản.
    - Lai ghép (Crossover): Kết hợp thông tin từ hai cá thể cha mẹ để tạo ra cá thể con.
    - Đột biến (Mutation): Tạo ra sự thay đổi ngẫu nhiên trong cá thể con.
  #### Beam Search (Tìm kiếm theo tia)
![BeamSearch](https://github.com/user-attachments/assets/d49d64d6-7086-4bad-ab19-6053d6a7b2eb)

- **Tham số then chốt**:
  - Độ rộng tia `k`.

- **Nguyên tắc hoạt động**:
  1. Bắt đầu với `k` trạng thái đầy tiềm năng.
  2. Ở mỗi bước:
     - Từ mỗi trạng thái hiện tại, tạo ra tất cả các trạng thái lân cận.
     - Tổng hợp tất cả các trạng thái lân cận từ `k` trạng thái trước.
     - Sử dụng hàm heuristic để đánh giá và chỉ giữ lại `k` trạng thái tốt nhất.
  3. Lặp lại quá trình này cho đến khi:
     - Tìm thấy trạng thái mục tiêu, hoặc
     - Không còn trạng thái mới, hoặc
     - Đạt đến giới hạn định trước (số bước, thời gian...).

- **Đặc điểm**:
  - Kết hợp giữa BFS và chiến lược heuristic.
  - Giảm chi phí bộ nhớ so với BFS.
  - Có thể bỏ qua lời giải nếu `k` quá nhỏ.

---
  **Nhận xét**:
  - Các thuật toán Hill Climbing đơn giản nhanh nhưng dễ bị kẹt tại cực trị địa phương, không đảm bảo tìm lời giải tối ưu trong 8-puzzle.
  - Simulated Annealing cải thiện khả năng thoát khỏi cực trị địa phương, phù hợp với bài toán 8-puzzle phức tạp.
  - Beam Search giúp cân bằng giữa bộ nhớ và thời gian, hiệu quả nếu chọn beam width phù hợp.
  - Genetic Algorithm có thể tìm lời giải tốt trong không gian trạng thái lớn nhưng cần nhiều tính toán và tinh chỉnh tham số. 
  -  Tóm lại, Tìm kiếm cục bộ và tiến hóa cung cấp các phương pháp linh hoạt, có thể áp dụng trong 8-puzzle để tìm lời giải gần tối ưu nhanh hơn so với tìm kiếm toàn diện, nhưng không đảm bảo tối ưu tuyệt đối.
  
  **So sánh**:
  
  ![3](https://github.com/user-attachments/assets/2b8c057d-34a9-4087-a847-180d1fd1a5fb)

### 2.4. Các Thuật Toán Tìm Kiếm Khác

---

#### And-Or Search (Tìm kiếm AND-OR)

![And_Or](https://github.com/user-attachments/assets/75fd2bc8-27b7-437e-b5bd-d3b0c94d9889)

- **Mục tiêu**: Tìm một **cây giải pháp** (solution tree) thay vì một đường đi duy nhất.
- **Áp dụng**: Trong môi trường **không xác định** (nondeterministic), nơi mỗi hành động có thể dẫn đến nhiều kết quả khác nhau.
- **Nguyên tắc hoạt động**:
  - Tại mỗi nút OR: chọn **một hành động**.
  - Tại mỗi nút AND: tất cả các **kết quả có thể** của hành động phải dẫn đến thành công.
- **Kết quả**: Một **kế hoạch có điều kiện** (conditional plan) có thể xử lý mọi tình huống xảy ra.

---



---

#### Q-Learning (Học tăng cường Q)

- **Loại**: Thuật toán **Reinforcement Learning** (Học tăng cường) **off-policy**.
- **Mục tiêu**: Tìm **chính sách tối ưu** (optimal policy) để đưa ra hành động trong từng trạng thái.
- **Nguyên tắc hoạt động**:
  - Học bảng Q-Value `Q(s, a)` ước lượng giá trị kỳ vọng khi thực hiện hành động `a` tại trạng thái `s`.
  - **Cập nhật** Q-Value theo công thức:
    ```
    Q(s, a) ← Q(s, a) + α [r + γ * max Q(s', a') - Q(s, a)]
    ```
    - `α`: learning rate
    - `γ`: discount factor
    - `r`: phần thưởng thu được
    - `s'`: trạng thái kế tiếp
- **Ưu điểm**: Không cần mô hình môi trường (model-free).

---

#### Nondeterministic Search (Tìm kiếm không xác định)
![NondeterminnisticSearch](https://github.com/user-attachments/assets/4bc6ac74-d5ff-40f6-a847-39b9fcbfb2fb)


- **Môi trường**: Không xác định — một hành động có thể có **nhiều kết quả**.
- **Mục tiêu**: Tìm một **kế hoạch với các nhánh dự phòng**, bao gồm:
  - Các hành động chính.
  - Các **rẽ nhánh** để xử lý mọi kết quả có thể xảy ra.
- **Giải pháp**: Cây AND-OR hoặc kế hoạch có điều kiện.

---

#### Partially Observable Search (Tìm kiếm trong môi trường quan sát một phần)
![Partially Observable Search](https://github.com/user-attachments/assets/dfdbc10e-c57f-4eb7-99cb-0401732e5e84)

- **Đặc điểm**:
  - Không thể quan sát toàn bộ trạng thái thật.
  - Làm việc với **trạng thái tin tưởng** (belief states) – tập các trạng thái khả dĩ.
- **Mục tiêu**: Tìm kế hoạch hoạt động hiệu quả **dù không biết chắc mình đang ở đâu**.
- **Giải pháp điển hình**: Tìm kiếm Sensorless, lọc trạng thái, cập nhật trạng thái tin tưởng sau mỗi hành động.

---
#### Backtracking
![Backtracking](https://github.com/user-attachments/assets/6e7ceff9-3b80-490c-8088-dc4d616a2e27)

Thuật toán Backtracking duyệt qua không gian trạng thái một cách đệ quy, tìm kiếm lời giải bằng cách thử từng trạng thái và quay lại nếu không tìm được lời giải. Nếu tìm thấy trạng thái đích, thuật toán sẽ trả về đường đi.

### Cách hoạt động:
- Tạo một danh sách `path` để lưu các trạng thái đã duyệt.
- Sử dụng một tập hợp `visited` để theo dõi các trạng thái đã thăm.
- Đệ quy duyệt qua các trạng thái láng giềng của trạng thái hiện tại.
- Nếu trạng thái hiện tại là trạng thái đích, trả về đường đi.

#### Backtracking với Forward Checking
![BacktrackingForward](https://github.com/user-attachments/assets/d55e768d-77a4-4575-9e71-c08ef5041c7f)

Phiên bản này sử dụng Forward Checking để chỉ duyệt qua các láng giềng hợp lệ, giúp giảm thiểu việc duyệt qua các trạng thái đã thăm, từ đó cải thiện hiệu suất.

### Cách hoạt động:
- Kiểm tra các láng giềng hợp lệ trước khi tiếp tục.
- Tương tự như Backtracking, nếu trạng thái đích được tìm thấy, thuật toán sẽ trả về đường đi.

#### Min-Conflicts

Thuật toán Min-Conflicts là một phương pháp heuristic, nơi thuật toán tìm kiếm trạng thái có ít xung đột nhất với các láng giềng của nó và tiếp tục đi theo hướng này.

### Cách hoạt động:
- Đếm xung đột của trạng thái với các láng giềng.
- Chọn láng giềng có số lượng xung đột ít nhất.
- Dừng lại nếu không có thay đổi trạng thái hoặc đạt đến giới hạn bước đi.
#### Sensorless Search
![Sensorless](https://github.com/user-attachments/assets/8cdbebba-2a9e-4471-901c-fe4dd639bd11)

Thuật toán **Sensorless Search** (tìm kiếm không cảm biến) là một kỹ thuật tìm kiếm trong môi trường mà trạng thái ban đầu không hoàn toàn được biết và tác nhân không nhận được thông tin cảm biến từ môi trường. Tác nhân chỉ biết được tập hợp các trạng thái khả dĩ mà nó có thể đang ở và phải chọn hành động làm giảm sự bất định này.

---

#### Cách hoạt động:
1. **Khởi tạo** tập trạng thái có thể là trạng thái ban đầu (belief state).
2. **Chọn hành động** sao cho khi áp dụng vào tất cả các trạng thái trong belief state, kết quả thu được là tập mới nhỏ hơn (ít bất định hơn).
3. **Cập nhật belief state** dựa trên hành động vừa thực hiện.
4. **Lặp lại** cho đến khi tập trạng thái khả dĩ thu hẹp còn một trạng thái duy nhất (biết chắc mình đang ở đâu), hoặc đạt được trạng thái mục tiêu bất kể đang ở đâu.
5. **Dừng lại** nếu đạt mục tiêu hoặc không còn hành động nào có thể giảm bất định.

---

#### Đặc điểm:
- **Không sử dụng cảm biến**, chỉ dựa vào mô hình hành động và suy diễn logic.
- Phù hợp với môi trường **ẩn**, nơi tác nhân không thể quan sát trực tiếp.
- Tập trung vào việc **thu hẹp tập hợp trạng thái có thể** bằng các hành động có thể dự đoán được.

  ### So sánh
  ![4](https://github.com/user-attachments/assets/3c79316c-e392-41a8-aba5-9e94d1dfe103)

## 3. KẾT LUẬN

Thông qua đồ án này, chúng tôi đã thực hiện nghiên cứu, triển khai và so sánh hiệu suất của một số thuật toán tìm kiếm tiêu biểu trong bối cảnh bài toán 8 ô chữ. Kết quả nghiên cứu cho thấy:

- Các thuật toán tìm kiếm có thông tin (A*, IDA*) thường hiệu quả hơn các thuật toán không có thông tin (BFS, IDDFS, DFS) về tốc độ tìm kiếm và số lượng trạng thái duyệt qua.
- Các thuật toán tìm kiếm cục bộ có khả năng khám phá không gian trạng thái rộng lớn nhưng không đảm bảo tìm được lời giải tối ưu toàn cục.
- Thuật toán CSP phù hợp khi biểu diễn bài toán dưới dạng các ràng buộc, trong khi các thuật toán tìm kiếm trong môi trường không chắc chắn (Nondeterministic Search, Partially Observable Search) phù hợp cho các môi trường phức tạp hơn.
- Các thuật toán học tăng cường như Q-Learning có tiềm năng trong các bài toán mà tác nhân cần học hỏi thông qua tương tác với môi trường.

Việc lựa chọn thuật toán phù hợp phụ thuộc vào yêu cầu cụ thể của bài toán, bao gồm yêu cầu về tính tối ưu, giới hạn về tài nguyên tính toán và đặc điểm của không gian trạng thái.
