#Bài tập 1
from sympy import Symbol, solve

x = Symbol('x')
bieuthuc = x + 3 - 5
nghiem = solve(bieuthuc)
print(f"Nghiệm của phương trình {bieuthuc} = 0 là: {nghiem}")

bieuthuc_bac2 = x**2 + 3 - 5
nghiemx = solve(bieuthuc_bac2)
print(f"Các nghiệm của phương trình {bieuthuc_bac2} = 0 là: {nghiemx}")

if nghiemx:
    print(f"Nghiệm thứ nhất: {nghiemx[0]}")
    if len(nghiemx) > 1:
        print(f"Nghiệm thứ hai: {nghiemx[1]}")

#Bài tập 2
from sympy import Symbol, solve

x = Symbol('x')
ptb2_1 = x**2 + 9*x + 8
nghiem_1 = solve(ptb2_1, x, dict=True)
print(f"Nghiệm của phương trình {ptb2_1} = 0 (dạng dict): {nghiem_1}")

ptb2_2 = x**2 + 1*x + 10
nghiem_2 = solve(ptb2_2, x, dict=True)
print(f"Nghiệm của phương trình {ptb2_2} = 0 (dạng dict, có nghiệm phức): {nghiem_2}")
#Bài tập 3

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

ptb2_tongquat = a*x**2 + b*x + c
nghiem_tongquat = solve(ptb2_tongquat, x, dict=True)
print(f"Nghiệm của phương trình {ptb2_tongquat} = 0 theo x (dạng dict): {nghiem_tongquat}")

# Bài tập 4
x = Symbol('x')
y = Symbol('y')

# Định nghĩa hai phương trình
pt1 = 2*x + 3*y - 12
pt2 = 3*x - 2*y - 5

# Giải hệ phương trình
nghiem = solve((pt1, pt2), (x, y), dict=True)
print(f"Nghiệm của hệ phương trình (dạng dict): {nghiem}")

# Kiểm tra lại nghiệm (nếu tìm thấy nghiệm)
if nghiem:
    nghiem_dict = nghiem[0]
    x_nghiem = nghiem_dict[x]
    y_nghiem = nghiem_dict[y]

    # Thay nghiệm vào phương trình 1
    kiem_tra_pt1 = pt1.subs({x: x_nghiem, y: y_nghiem})
    print(f"Kiểm tra pt1 với nghiệm: {kiem_tra_pt1}")

    # Thay nghiệm vào phương trình 2
    kiem_tra_pt2 = pt2.subs({x: x_nghiem, y: y_nghiem})
    print(f"Kiểm tra pt2 với nghiệm: {kiem_tra_pt2}")
else:
    print("Không tìm thấy nghiệm.")

import numpy as np

# Bài tập 5

M1 = np.array([[9, 12], [23, 30]])
print("Ma trận M1:")
print(M1)

u = np.array([2, 1])
print("\nVector u:")
print(u)

# Tích giữa ma trận M1 và vector u (M1 * u)
tichM1u = np.dot(M1, u)
print("\nTích M1 * u:")
print(tichM1u)
# Giải thích:
# [9*2 + 12*1, 23*2 + 30*1] = [18 + 12, 46 + 30] = [30, 76]

# Tích giữa vector u và ma trận M1 (u * M1) - Phép nhân này không hợp lệ về kích thước
try:
    tichuM1 = np.dot(u, M1)
    print("\nTích u * M1:")
    print(tichuM1)
except ValueError as e:
    print("\nTích u * M1:")
    print("Phép nhân vector (1x2) với ma trận (2x2) không hợp lệ theo quy tắc nhân ma trận.")

# Thực hành phép toán np.dot(M1, u)
tich_np_dot_M1u = np.dot(M1, u)
print("\nnp.dot(M1, u):")
print(tich_np_dot_M1u)
# Giải thích: Tương tự như phép nhân M1 * u ở trên.

# Thực hành phép toán np.dot(u, M1)
try:
    tich_np_dot_uM1 = np.dot(u, M1)
    print("\nnp.dot(u, M1):")
    print(tich_np_dot_uM1)
except ValueError as e:
    print("\nnp.dot(u, M1):")
    print("Phép nhân vector (1x2) với ma trận (2x2) không hợp lệ theo quy tắc nhân ma trận.")
    print("Để thực hiện phép nhân này, bạn có thể cần chuyển vị vector u thành ma trận cột (2x1).")

# Thử nhân chuyển vị của u với M1
u_transposed = u.reshape(2, 1)
tich_uT_M1 = np.dot(M1, u_transposed)
print("\nTích M1 * u.T (u được chuyển vị thành cột):")
print(tich_uT_M1)

import numpy as np

# Lệnh 1:
mat1 = np.zeros((5, 5))
print("Câu hỏi: Cho biết mat1?")
print("mat1 =")
print(mat1)
print("-" * 20)

# Lệnh 2:
mat2 = np.ones((5, 5))
print("Câu hỏi: Cho biết mat2?")
print("mat2 =")
print(mat2)
print("-" * 20)

# Lệnh 3:
mat3 = mat1 + 2 * mat2
print("Câu hỏi: Cho biết mat3?")
print("mat3 =")
print(mat3)
print("-" * 20)

# Lệnh 4:
mat4 = mat3
print("Lệnh: mat4 = mat3")
mat3[3][2] = 10
print("Lệnh: mat3[3][2] = 10")
print("Câu hỏi: Cho biết mat3 và mat4? (mat3 thay đổi thì mat4 có thay đổi theo không?)")
print("mat3 =")
print(mat3)
print("mat4 =")
print(mat4)
print("Trả lời: Có, mat4 cũng thay đổi theo vì mat4 và mat3 cùng tham chiếu đến cùng một vùng nhớ.")
print("-" * 20)

# Lệnh 5:
mat5 = np.copy(mat3)
print("Lệnh: mat5 = np.copy(mat3)")
mat3[3][2] = 10  # Thay đổi lại mat3 để thấy sự khác biệt
print("Lệnh: mat3[3][2] = 10")
print("Câu hỏi: Cho biết mat3, mat4 và mat5? (mat3 thay đổi thì mat4 và mat5 có thay đổi theo không?)")
print("mat3 =")
print(mat3)
print("mat4 =")
print(mat4)
print("mat5 =")
print(mat5)
print("Trả lời: mat4 thay đổi theo mat3 (vì cùng tham chiếu). mat5 không thay đổi vì nó là một bản sao độc lập của mat3 tại thời điểm tạo.")
print("-" * 20)

# Lệnh 6:
mat6 = np.empty((4, 5))
print("Câu hỏi: hãy cho biết mat6?")
print("mat6 =")
print(mat6)
print("Trả lời: mat6 là một ma trận 4x5 với các giá trị không được khởi tạo (có thể là các giá trị ngẫu nhiên trong bộ nhớ).")
print("-" * 20)

# Lệnh 7:
mat7 = np.identity(4)
print("Câu hỏi: hãy cho biết mat7?")
print("mat7 =")
print(mat7)
print("Trả lời: mat7 là ma trận đơn vị 4x4.")
print("-" * 20)

# Lệnh 8:
mat8 = np.random.rand(4, 5)
print("Câu hỏi: hãy cho biết mat8?")
print("mat8 =")
print(mat8)
print("Trả lời: mat8 là một ma trận 4x5 với các giá trị ngẫu nhiên trong khoảng [0.0, 1.0).")

#Bài tập 6

# Ma trận thể hiện mức độ nguy cơ của các yếu tố
# Hàng: Cháy rừng, Lũ quét, Sạt lở núi, Bệnh dịch, Lộ bí mật
# Cột: Không có, Thấp, Trung bình, Cao, Rất cao
hazard_levels = np.array([
    [0, 1, 2, 3, 5],   # Cháy rừng
    [0, 1, 2, 4, 8],   # Lũ quét
    [0, 1, 3, 5, 9],   # Sạt lở núi
    [0, 1, 3, 5, 7],   # Bệnh dịch
    [0, 5, 10, 15, 20]  # Lộ bí mật
])

# Ma trận địa hình cho các khu vực
A = np.array([[1, 0, 0, 1],
              [3, 1, 0, 1],
              [5, 2, 0, 1],
              [2, 0, 1, 2]])

B = np.array([[1, 2, 2, 1],
              [2, 2, 0, 2],
              [0, 1, 2, 4],
              [1, 4, 1, 2]])

C = np.array([[0, 5, 1, 1],
              [0, 1, 1, 3],
              [1, 3, 1, 3],
              [0, 1, 3, 3]])

D = np.array([[3, 1, 1, 0],
              [5, 0, 0, 7],
              [7, 0, 0, 3],
              [5, 0, 3, 5]])

E = np.array([[0, 0, 10, 0],
              [0, 15, 0, 1],
              [0, 5, 15, 0],
              [0, 20, 5, 0]])

def calculate_total_hazard(terrain, consider_fire=True, consider_flood=True,
                           consider_landslide=True, consider_epidemic=True,
                           consider_exposure=True):
    """Tính tổng mức độ nguy cơ cho một bản đồ địa hình."""
    total_hazard = np.zeros_like(terrain, dtype=float)
    factors = [consider_fire, consider_flood, consider_landslide, consider_epidemic, consider_exposure]
    hazard_indices = np.array([0, 1, 2, 3, 4])

    for r in range(terrain.shape[0]):
        for c in range(terrain.shape[1]):
            cell_hazard = 0
            for i, factor_enabled in enumerate(factors):
                if factor_enabled:
                    hazard_level_index = terrain[r, c]
                    if 0 <= hazard_level_index < hazard_levels.shape[1]:
                        cell_hazard += hazard_levels[i, hazard_level_index]
            total_hazard[r, c] = cell_hazard
    return total_hazard

def is_safe(total_hazard_map, threshold=5):
    """Xác định các khu vực an toàn dựa trên tổng mức độ nguy cơ."""
    return total_hazard_map <= threshold

print("--- Phân tích mức độ an toàn cho từng kịch bản ---")

# a. An toàn trong chiến dịch ngắn hạn 1-2 ngày (có yếu tố tránh lộ bí mật; không quan tâm đến các yếu tố khác)
total_hazard_a = calculate_total_hazard(A, consider_fire=False, consider_flood=False,
                                         consider_landslide=False, consider_epidemic=False,
                                         consider_exposure=True)
safe_a = is_safe(total_hazard_a)
print("\na. An toàn trong chiến dịch ngắn hạn (chỉ xét lộ bí mật):")
print("Tổng mức độ nguy cơ:\n", total_hazard_a)
print("Khu vực an toàn (<= 5):\n", safe_a)

# b. An toàn trong tập luyện thời bình (không cần xét yếu tố tránh lộ bí mật và bệnh dịch)
total_hazard_b = calculate_total_hazard(B, consider_exposure=False, consider_epidemic=False)
safe_b = is_safe(total_hazard_b)
print("\nb. An toàn trong tập luyện thời bình (không xét lộ bí mật và bệnh dịch):")
print("Tổng mức độ nguy cơ:\n", total_hazard_b)
print("Khu vực an toàn (<= 5):\n", safe_b)

# c. An toàn theo mùa khô (không có lũ, không sạt núi nhưng có cháy rừng và bệnh dịch)
total_hazard_c = calculate_total_hazard(C, consider_flood=False, consider_landslide=False)
safe_c = is_safe(total_hazard_c)
print("\nc. An toàn theo mùa khô (chỉ xét cháy rừng và bệnh dịch):")
print("Tổng mức độ nguy cơ:\n", total_hazard_c)
print("Khu vực an toàn (<= 5):\n", safe_c)

# d. An toàn trong mùa mưa (có lũ, có sạt lở núi, có bệnh dịch mà không có cháy rừng)
total_hazard_d = calculate_total_hazard(D, consider_fire=False)
safe_d = is_safe(total_hazard_d)
print("\nd. An toàn trong mùa mưa (chỉ xét lũ, sạt lở núi và bệnh dịch):")
print("Tổng mức độ nguy cơ:\n", total_hazard_d)
print("Khu vực an toàn (<= 5):\n", safe_d)

# e. An toàn trong 8 tháng (có đủ các mùa và có yếu tố tránh lộ bí mật)
total_hazard_e = calculate_total_hazard(E, consider_exposure=True)
safe_e = is_safe(total_hazard_e)
print("\ne. An toàn trong 8 tháng (xét tất cả các yếu tố):")
print("Tổng mức độ nguy cơ:\n", total_hazard_e)
print("Khu vực an toàn (<= 5):\n", safe_e)