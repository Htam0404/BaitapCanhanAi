BÁO CÁO ĐỒ ÁN 

ỨNG DỤNG CÁC THUẬT TOÁN TÌM KIẾM TRONG BÀI TOÁN 8 Ô CHỮ 

1. MỤC TIÊU 

Mục tiêu chính của đồ án là nghiên cứu, phân tích sâu và triển khai ứng dụng các thuật toán tìm kiếm khác nhau nhằm giải quyết hiệu quả bài toán 8 ô chữ. Thông qua dự án này, chúng tôi chứng minh khả năng hiện thực hóa các thuật toán tìm kiếm có thông tin và không có thông tin, đồng thời tiến hành đánh giá định lượng hiệu suất của từng phương pháp khi áp dụng vào bối cảnh trò chơi. 

2. NỘI DUNG NGHIÊN CỨU 

2.1. Các Thuật Toán Tìm Kiếm Không Có Thông Tin (Uninformed Search Algorithms) 

2.1.1. Phân tích Bài Toán Tìm Kiếm và Định nghĩa Solution 

Bài toán 8 ô chữ, một bài toán kinh điển trong lĩnh vực Trí tuệ Nhân tạo, được cấu thành bởi các yếu tố cơ bản sau: 

Trạng thái (State): Biểu diễn cấu hình hiện tại của trò chơi thông qua ma trận vuông 3x3. 

Trạng thái Ban Đầu (Initial State): Cấu hình ma trận 3x3 xác định vị trí xuất phát của các ô số. 

Trạng thái Mục Tiêu (Goal State): Cấu hình ma trận 3x3 mong muốn đạt được. 

Hành động (Actions): Các thao tác di chuyển ô trống (giá trị 0) theo bốn hướng: lên, xuống, trái, phải. 

Hàm Chuyển Trạng Thái (Transition Function): Quy tắc xác định trạng thái kế tiếp sau khi thực hiện một hành động hợp lệ. 

Kiểm tra Mục Tiêu (Goal Test): Hàm boolean đánh giá xem trạng thái hiện tại có trùng với trạng thái mục tiêu hay không. 

Chi phí Đường đi (Path Cost): Số lượng hành động (di chuyển) đã thực hiện để đạt đến trạng thái hiện tại từ trạng thái ban đầu. 

Solution (Lời giải) cho bài toán 8 ô chữ được định nghĩa là một chuỗi tối ưu các hành động (di chuyển) từ trạng thái ban đầu đến trạng thái mục tiêu, tối thiểu hóa chi phí đường đi. 

2.1.2. Trực Quan Hóa Thuật Toán 

Ứng dụng đồ họa được phát triển cho phép trực quan hóa quá trình tìm kiếm của các thuật toán không có thông tin, bao gồm: 

Tìm kiếm theo chiều sâu (Depth-First Search - DFS) 

 ![alt text](UFS.gif)

Tìm kiếm theo chiều rộng (Breadth-First Search - BFS) 
![alt text](BFS.gif)
Tìm kiếm chi phí đồng nhất (Uniform-Cost Search - UCS) 
![alt text](UCS.gif)
Tìm kiếm sâu dần (Iterative Deepening Depth-First Search - IDDFS) 
![alt text](IDDFS.gif)
2.1.3. So sánh Hiệu Suất 

[Tham khảo hình ảnh so sánh hiệu suất được đính kèm] 

Hiệu suất của các thuật toán được đánh giá dựa trên các tiêu chí định lượng như thời gian thực thi (execution time) và số lượng trạng thái đã khám phá (number of expanded nodes) để đạt được trạng thái mục tiêu. 

2.1.4. Nhận Xét về Hiệu Suất 

DFS: Ưu điểm về bộ nhớ do chỉ duy trì nhánh tìm kiếm hiện tại. Tuy nhiên, có nguy cơ rơi vào vòng lặp vô hạn hoặc tìm thấy lời giải không tối ưu. Hiệu suất thực tế có thể kém trên không gian trạng thái lớn của bài toán 8 ô chữ. 

BFS: Đảm bảo tìm được lời giải tối ưu (số bước di chuyển ít nhất). Nhược điểm là tiêu tốn nhiều bộ nhớ để lưu trữ các nút ở cùng mức độ sâu. Hiệu suất phù hợp với bài toán 8 ô chữ có độ phức tạp vừa phải. 

UCS: Tương tự BFS, đảm bảo tìm được lời giải tối ưu khi chi phí các hành động khác nhau. Trong bài toán 8 ô chữ với chi phí mỗi bước đi là 1, hiệu suất tương đương BFS. 

IDDFS: Kết hợp ưu điểm tiết kiệm bộ nhớ của DFS và tính tối ưu của BFS. Tốn thời gian hơn do phải lặp lại việc tìm kiếm ở các độ sâu khác nhau. 

2.2. Các Thuật Toán Tìm Kiếm Có Thông Tin (Informed Search Algorithms) 

Các thuật toán này tận dụng thông tin heuristic để hướng dẫn quá trình tìm kiếm, nâng cao hiệu quả so với các thuật toán không có thông tin. 

Greedy Best-First Search (Tìm kiếm tham lam theo ưu tiên tốt nhất): 

Hàm đánh giá (Evaluation function): f(n)=h(n), trong đó h(n) là hàm heuristic ước tính chi phí từ trạng thái n đến trạng thái mục tiêu. 

Hàm Heuristic (Heuristic function): Sử dụng hàm Manhattan distance (tổng khoảng cách Manhattan từ vị trí hiện tại đến vị trí đích của mỗi ô). 

Nguyên tắc hoạt động: Luôn chọn trạng thái có giá trị heuristic thấp nhất để mở rộng tiếp theo. 

Ưu/nhược điểm: Nhanh chóng tìm ra lời giải nhưng không đảm bảo tính tối ưu. Dễ bị lạc vào các đường đi không hứa hẹn. 

A* Search (Tìm kiếm A*): 

Hàm đánh giá (Evaluation function): f(n)=g(n)+h(n), trong đó g(n) là chi phí đường đi từ trạng thái ban đầu đến trạng thái n, và h(n) là hàm heuristic ước tính chi phí từ trạng thái n đến trạng thái mục tiêu. 

Hàm Heuristic (Heuristic function): Sử dụng hàm Manhattan distance (tổng khoảng cách Manhattan từ vị trí hiện tại đến vị trí đích của mỗi ô). 

Nguyên tắc hoạt động: Ưu tiên mở rộng các trạng thái có tổng chi phí ước tính thấp nhất. 

Ưu/nhược điểm: Đảm bảo tìm được lời giải tối ưu nếu hàm heuristic là chấp nhận được (admissible) và nhất quán (consistent). Có thể tốn nhiều bộ nhớ hơn các thuật toán khác. 

IDA* Search (Tìm kiếm IDA*): 

Hàm đánh giá (Evaluation function): Tương tự A*, sử dụng f(n)=g(n)+h(n). 

Hàm Heuristic (Heuristic function): Sử dụng hàm Manhattan distance (tổng khoảng cách Manhattan từ vị trí hiện tại đến vị trí đích của mỗi ô). 

Nguyên tắc hoạt động: Thực hiện tìm kiếm sâu dần (Iterative Deepening) với ngưỡng cắt dựa trên giá trị f(n). Bắt đầu với ngưỡng bằng h(initial), sau đó tăng dần ngưỡng lên giá trị f(n) nhỏ nhất vượt quá ngưỡng hiện tại của lần tìm kiếm trước. 

Ưu/nhược điểm: Tiết kiệm bộ nhớ hơn A* vì không lưu trữ toàn bộ cây tìm kiếm. Vẫn đảm bảo tính tối ưu nếu heuristic chấp nhận được. Có thể tính toán lại các trạng thái nhiều lần. 

2.3. Các Thuật Toán Tìm Kiếm Cục Bộ (Local Search Algorithms) 

Tập trung vào việc tối ưu hóa trạng thái hiện tại để tìm ra trạng thái mục tiêu, không quan tâm đến đường đi. 

Hill Climbing (Leo đồi): 

Hàm đánh giá (Evaluation function): Thường là hàm heuristic h(n) (trong trường hợp tìm cực tiểu) hoặc hàm mục tiêu (trong trường hợp tìm cực đại). 

Nguyên tắc hoạt động: Bắt đầu từ một trạng thái hiện tại và di chuyển đến trạng thái lân cận có giá trị hàm đánh giá tốt hơn. Lặp lại cho đến khi không tìm thấy trạng thái lân cận nào tốt hơn. 

Các biến thể:  

Simple Hill Climbing (Leo đồi đơn giản): Chọn trạng thái lân cận tốt hơn đầu tiên tìm thấy. 

Steepest Ascent Hill Climbing (Leo đồi dốc nhất): Xem xét tất cả các trạng thái lân cận và chọn trạng thái tốt nhất. 

Ưu/nhược điểm: Đơn giản và dễ cài đặt. Dễ bị mắc kẹt ở cực đại cục bộ (local maxima) hoặc cực tiểu cục bộ (local minima), vùng bằng phẳng (plateaus), hoặc gờ (ridges). 

Random Restart Hill Climbing (Leo đồi khởi động lại ngẫu nhiên): 

Nguyên tắc hoạt động: Thực hiện thuật toán Hill Climbing nhiều lần từ các trạng thái khởi tạo ngẫu nhiên khác nhau. Lưu giữ trạng thái tốt nhất tìm được sau tất cả các lần thử. 

Ưu/nhược điểm: Tăng khả năng thoát khỏi cực đại/cực tiểu cục bộ so với Hill Climbing đơn thuần. Tuy nhiên, vẫn không đảm bảo tìm được nghiệm tối ưu toàn cục. 

Beam Search (Tìm kiếm theo chùm tia): 

Tham số: k (kích thước chùm tia). 

Nguyên tắc hoạt động: Duy trì một tập hợp k trạng thái tốt nhất (chùm tia) tại mỗi bước. Mở rộng tất cả các trạng thái trong chùm tia và chọn k trạng thái tốt nhất để tiếp tục ở bước tiếp theo. 

Ưu/nhược điểm: Cân bằng giữa tìm kiếm theo chiều rộng (như BFS) và tìm kiếm tham lam. Có thể tìm thấy lời giải tốt hơn Hill Climbing nhưng không đảm bảo tính tối ưu. 

Simulated Annealing (Mô phỏng luyện kim): 

Tham số: Nhiệt độ T (giảm dần theo thời gian), hàm giảm nhiệt độ. 

Nguyên tắc hoạt động: Bắt đầu với một trạng thái hiện tại và nhiệt độ cao. Tại mỗi bước, chọn một trạng thái lân cận ngẫu nhiên. Nếu trạng thái lân cận tốt hơn, di chuyển đến đó. Nếu không tốt hơn, vẫn có một xác suất nhất định (phụ thuộc vào nhiệt độ và độ "tệ" của trạng thái lân cận) để di chuyển đến đó. Nhiệt độ giảm dần theo thời gian, làm giảm xác suất chấp nhận các di chuyển xấu hơn. 

Ưu/nhược điểm: Có khả năng thoát khỏi cực đại/cực tiểu cục bộ tốt hơn Hill Climbing. Có thể hội tụ đến lời giải tốt nhưng có thể tốn nhiều thời gian. 

Genetic Algorithm (Thuật toán di truyền): 

Các thành phần chính:  

Quần thể (Population): Một tập hợp các cá thể (trạng thái). 

Hàm fitness (Fitness function): Đánh giá chất lượng của mỗi cá thể. 

Chọn lọc (Selection): Chọn các cá thể tốt nhất để sinh sản. 

Lai ghép (Crossover): Kết hợp thông tin từ hai cá thể cha mẹ để tạo ra cá thể con. 

Đột biến (Mutation): Tạo ra sự thay đổi ngẫu nhiên trong cá thể con. 

Nguyên tắc hoạt động: Bắt đầu với một quần thể ngẫu nhiên. Lặp lại các bước chọn lọc, lai ghép và đột biến để tạo ra các thế hệ mới với hy vọng tìm được các cá thể có fitness cao hơn. 

Ưu/nhược điểm: Hiệu quả với các bài toán có không gian tìm kiếm lớn và phức tạp. Không đảm bảo tìm được nghiệm tối ưu toàn cục và có thể tốn nhiều thời gian tính toán. 

2.4. Các Thuật Toán Tìm Kiếm Khác 

And-Or Search (Tìm kiếm AND-OR): 

Không gian trạng thái: Bao gồm các trạng thái và các nút AND (yêu cầu tất cả các nhánh con thành công) và nút OR (yêu cầu ít nhất một nhánh con thành công). 

Mục tiêu: Tìm một cây giải pháp (solution tree) thay vì một đường đi đơn lẻ. 

Ứng dụng: Phù hợp cho các bài toán có tính không xác định cao hoặc các bài toán lập kế hoạch. 

Nguyên tắc hoạt động: Xây dựng cây tìm kiếm AND-OR để tìm chiến lược giải quyết. 

CSP (Constraint Satisfaction Problems - Bài toán thỏa mãn ràng buộc): 

Các thành phần chính:  

Biến (Variables): Tập hợp các biến cần gán giá trị. 

Miền giá trị (Domains): Tập hợp các giá trị có thể gán cho mỗi biến. 

Ràng buộc (Constraints): Các quy tắc giới hạn giá trị mà các biến có thể nhận đồng thời. 

Mục tiêu: Tìm một phép gán giá trị cho tất cả các biến sao cho tất cả các ràng buộc đều được thỏa mãn. 

Các thuật toán tiêu biểu:  

Backtracking (Tìm kiếm lùi): Tìm kiếm theo chiều sâu, gán giá trị cho các biến lần lượt. Nếu gặp phải mâu thuẫn (ràng buộc bị vi phạm), quay lui và thử giá trị khác. 

Backtracking Forward Checking (Tìm kiếm lùi với kiểm tra phía trước): Cải tiến của Backtracking bằng cách kiểm tra trước các giá trị còn lại trong miền của các biến chưa được gán sau mỗi lần gán. Loại bỏ các giá trị không nhất quán với các ràng buộc. 

Min Conflicts (Thuật toán xung đột tối thiểu): Bắt đầu với một phép gán không hoàn chỉnh (hoặc hoàn chỉnh nhưng vi phạm một số ràng buộc). Lặp lại việc chọn một biến vi phạm ràng buộc và gán cho nó một giá trị mới sao cho số lượng ràng buộc bị vi phạm là tối thiểu. 

Sensorless Search (Tìm kiếm không cảm biến) / Conformant Search: 

Không gian trạng thái: Không gian các tập hợp trạng thái có thể (belief states) do tác nhân không có thông tin đầy đủ về trạng thái hiện tại. 

Mục tiêu: Tìm một chuỗi hành động đảm bảo đạt được mục tiêu bất kể trạng thái ban đầu thực tế là gì (trong tập hợp các trạng thái có thể). 

Ứng dụng: Phù hợp cho các môi trường mà tác nhân không thể quan sát trực tiếp trạng thái. 

Q-Learning: 

Thuật toán: Một thuật toán học tăng cường (Reinforcement Learning) off-policy. 

Bảng Q (Q-table): Lưu trữ giá trị Q(s, a) ước tính phần thưởng tích lũy kỳ vọng khi thực hiện hành động a trong trạng thái s. 

Nguyên tắc hoạt động: Tác nhân tương tác với môi trường, thực hiện các hành động và nhận phần thưởng. Bảng Q được cập nhật dựa trên kinh nghiệm này để học chính sách tối ưu. 

Ứng dụng: Phù hợp cho các môi trường có tính ngẫu nhiên và động, nơi tác nhân học hỏi thông qua thử và sai. 

Nondeterministic Search (Tìm kiếm không xác định): 

Đặc điểm: Các hành động có thể dẫn đến nhiều kết quả khác nhau. 

Mục tiêu: Tìm một kế hoạch (plan) bao gồm các hành động và các nhánh dự phòng cho các kết quả có thể xảy ra. 

Ứng dụng: Xử lý các tình huống có tính bất định. 

Partially Observable Search (Tìm kiếm quan sát một phần): 

Đặc điểm: Tác nhân không thể quan sát đầy đủ trạng thái của môi trường. 

Không gian trạng thái: Tương tự Sensorless Search, làm việc với các trạng thái tin tưởng (belief states). 

Mục tiêu: Tìm một chính sách (policy) ánh xạ các lịch sử quan sát đến các hành động. 

3. KẾT LUẬN 

Thông qua đồ án này, chúng tôi đã thực hiện nghiên cứu, triển khai và so sánh hiệu suất của một số thuật toán tìm kiếm tiêu biểu trong bối cảnh bài toán 8 ô chữ. Kết quả nghiên cứu cho thấy: 

Các thuật toán tìm kiếm có thông tin (A*, IDA*) thường hiệu quả hơn các thuật toán không có thông tin (BFS, IDDFS, DFS) về tốc độ tìm kiếm và số lượng trạng thái duyệt qua. 

Trong nhóm thuật toán không có thông tin, BFS và IDDFS đảm bảo tìm được lời giải tối ưu về số bước di chuyển, trong khi DFS có thể nhanh hơn nhưng không đảm bảo tính tối ưu. 

Các thuật toán tìm kiếm cục bộ có khả năng khám phá không gian trạng thái rộng lớn nhưng không đảm bảo tìm được lời giải tối ưu toàn cục. 

Thuật toán CSP phù hợp khi biểu diễn bài toán dưới dạng các ràng buộc, trong khi các thuật toán tìm kiếm trong môi trường không chắc chắn (Nondeterministic Search, Partially Observable Search) phù hợp cho các môi trường phức tạp hơn. 

Các thuật toán học tăng cường như Q-Learning có tiềm năng trong các bài toán mà tác nhân cần học hỏi thông qua tương tác với môi trường. 

Việc lựa chọn thuật toán phù hợp phụ thuộc vào yêu cầu cụ thể của bài toán, bao gồm yêu cầu về tính tối ưu, giới hạn về tài nguyên tính toán và đặc điểm của không gian trạng thái. 

Đồ án này đã cung cấp cái nhìn sâu sắc về ứng dụng thực tế của các thuật toán tìm kiếm trong một bài toán cụ thể, đồng thời làm nổi bật tầm quan trọng của việc lựa chọn thuật toán phù hợp để đạt được hiệu quả giải quyết vấn đề tối ưu. 

 