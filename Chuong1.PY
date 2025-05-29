#1.2.1
danhsach1 = [1., 3.]
danhsach2 = [5., 7.]

danhsach = danhsach1 + danhsach2
print(danhsach)

danhsach_gapdoi = 2 * danhsach
print(danhsach_gapdoi)

danhsach_nhan2 = danhsach * 2
print(danhsach_nhan2)
mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]

anh_xa = zip(thu_tu, mon_hoc, diem_so)
print(list(anh_xa))

tap_hop = set(anh_xa)
print(tap_hop)

anh_xa_lai = zip(*zip(thu_tu, mon_hoc, diem_so))
lay_TT, lay_monhoc, lay_diem = anh_xa_lai
print(list(lay_monhoc))

import itertools
tap_sinh = list(itertools.chain(range(4), range(5, 10), range(15, 20)))
print(tap_sinh)

ket_hop_nhieu_tap = list(zip(range(4), range(7, 12), reversed(range(11))))
print(ket_hop_nhieu_tap)
#1.2.2
a = b = c = 0
mylist = []
with open('D:/thucthi1.py', 'r') as f:
    code = f.read()
local_namespace = {}
exec(code, globals(), local_namespace)
a_from_file = local_namespace.get('a')
b_from_file = local_namespace.get('b')
c_from_file = local_namespace.get('c')

print("Giá trị a, b, c sau khi chạy tệp:", a_from_file, b_from_file, c_from_file)
#2.1
from sympy import Symbol, symbols

x = Symbol('x')
f = x + x + x + 2
print(f)

a = Symbol('Noi')
b = Symbol('Chim')
expression = 3 * b + 7 * a
print(expression)

# Truy tên thật của symbol
print(a.name)
print(b.name)

# Định nghĩa nhiều symbols cùng lúc
y, z = symbols('y z')
a_sym, b_sym, c_sym = symbols('a b c')
print(a_sym)
print(b_sym)
print(c_sym)

# Thực hiện phép toán học với symbols
s = x * y + y * x
print(s)

# Thực hiện phép nhân
p = x * (x + 2 * x)
print(p)

from sympy import Symbol

x = Symbol('x')
y = Symbol('y')

# Biểu thức 1: Phép nhân không tự động khai triển
p = (x + 2) * (y + 3)
print(p)

# Biểu thức 2: Cộng hai biểu thức không tự động khai triển
p = (x + 2) * (y + 3) + (x + 2) * (x - 3)
print(p)

# Biểu thức 3: Biểu thức được tự động đơn giản hóa
p = x * (-x + 2 * x - x)
print(p)

# Khai triển biểu thức bằng expand()
p = (x + 2) * (y + 3)
expanded_p = p.expand()
print(expanded_p)
#2.2. Làm việc với biểu thức
#2.2.1 Đặt nhân tử chung và khai triển biểu thức
from sympy import Symbol, factor, expand

x = Symbol('x')
y = Symbol('y')

# Biểu thức cần phân tích thành thừa số
bieuthuc_factor = x**3 - y**3
factored_bieuthuc = factor(bieuthuc_factor)
print(f"Phân tích thành thừa số của {bieuthuc_factor}: {factored_bieuthuc}")

# Biểu thức cần khai triển
bieuthuc_expand = (x - y) * (x**2 + x * y + y**2)
expanded_bieuthuc = expand(bieuthuc_expand)
print(f"Khai triển của {bieuthuc_expand}: {expanded_bieuthuc}")

# Thử expand một biểu thức đã khai triển (sẽ không thay đổi)
bieuthuc_da_khai_trien = x**2 + 2*x + 1
expanded_bieuthuc_2 = expand(bieuthuc_da_khai_trien)
print(f"Khai triển của biểu thức đã khai triển {bieuthuc_da_khai_trien}: {expanded_bieuthuc_2}")
#2.2.2 Đọc thêm
#2.2.3
from sympy import Symbol, simplify

# Thay thế giá trị

# Định nghĩa symbols
x = Symbol('x')
y = Symbol('y')

# Định nghĩa biểu thức
bieuthuc = x**2 - x*y + y**2
print(bieuthuc)

# Thay thế x = 3 và y = 2
giatri = bieuthuc.subs({x: 3, y: 2})
print(giatri)

print(x)
print(y)

# Thực hành tình huống 1: Xác định theo thứ tự x=3 và y=x
giatri = bieuthuc.subs({x: 3, y: x})
print(giatri)
giatri = bieuthuc.subs({x: 3})
giatri = giatri.subs({y: x}) # Lúc này x đã là 3
print(giatri)

giatri = bieuthuc.subs({x: 3})
giatri = giatri.subs({y: 3})
print(giatri)

# Thực hành tình huống 2: Xác định theo thứ tự x=y và y=3
giatri = bieuthuc.subs({x: y, y: 3})
print(giatri)

giatri = bieuthuc.subs({y: 3})
giatri = giatri.subs({x: y}) # Lúc này y đã là 3
print(giatri)

# Thực hành tình huống 3: Xác định y=x và sau đó tính x=3
giatri = bieuthuc.subs({y: x}).subs({x: 3})
print(giatri)

giatri = bieuthuc.subs({y: x})
giatri = giatri.subs({x: 3})
print(giatri)

print("-" * 20)

# Sử dụng simplify

# Định nghĩa lại biểu thức
bieuthuc = x**2 - x*y + y**2
print(bieuthuc)

bieuthuc_moi = bieuthuc.subs({x: 1 - y})
print(bieuthuc_moi)

dongian = simplify(bieuthuc_moi)
print(dongian)

print("-" * 20)

# Hàm simplify với biểu thức lượng giác
from sympy import sin, cos

bt = sin(x)*cos(y) + cos(x)*sin(y)
bt_moi = simplify(bt)
print(bt_moi)
#3 Làm quen với thư viện Numpy
#3.1 Một số lệnh cơ bản numpy xử lý vector
import numpy as np

# Định nghĩa vector vec1
vec1 = np.array([1., 3., 5.])
print("vec1 =", vec1)

# Nhân vector với một số vô hướng
result_scalar_mult = vec1 * 2
print("vec1 * 2 =", result_scalar_mult)

# Nhân vector với chính nó (phép nhân từng phần tử)
result_elementwise_mult = vec1 * vec1
print("vec1 * vec1 =", result_elementwise_mult)
print("Đây là phép nhân từng phần tử (element-wise multiplication).")

# Chia vector cho một số vô hướng
result_scalar_div = vec1 / 2
print("vec1 / 2 =", result_scalar_div)

# Cộng vector với chính nó
result_vec_add_self = vec1 + vec1
print("vec1 + vec1 =", result_vec_add_self)

# Định nghĩa vector vec2
vec2 = np.array([2., 4.])
print("vec2 =", vec2)

# Cộng hai vector (yêu cầu cùng kích thước)
try:
    result_vec_add = vec1 + vec2
    print("vec1 + vec2 =", result_vec_add)
except ValueError as e:
    print(f"Lỗi khi cộng vec1 và vec2: {e}")
    print("Hai vector không cùng kích thước nên không thể cộng trực tiếp.")

# Định nghĩa vector vec3
vec3 = np.array([2., 4., 6.])
print("vec3 =", vec3)

# Cộng hai vector cùng kích thước
result_vec_add2 = vec1 + vec3
print("vec1 + vec3 =", result_vec_add2)

# Chia hai vector (chia từng phần tử)
result_vec_div = vec1 / vec3
print("vec1 / vec3 =", result_vec_div)

# Nhân hai vector (nhân từng phần tử)
result_vec_mult = vec1 * vec3
print("vec1 * vec3 =", result_vec_mult)

# Phép toán kết hợp vô hướng và vector
result_combined = 2 * vec1 + 5 * vec3
print("2 * vec1 + 5 * vec3 =", result_combined)
import numpy as np

# Truy xuất phần tử của vector
vec3 = np.array([2., 4., 6.])
print("vec3[2] =", vec3[2])

# Tạo vector thông qua linspace
vec4 = np.linspace(0, 20, 5)
print("vec4 =", vec4)

# Tạo vector toàn số 0
vec5 = np.zeros(5)
print("vec5 =", vec5)

# Tạo vector toàn số 1
vec6 = np.ones(5)
print("vec6 =", vec6)

# Tạo vector ảo (giá trị rỗng - thực tế là giá trị không xác định)
vec7 = np.empty(5)
print("vec7 =", vec7)

# Tạo vector các giá trị ngẫu nhiên từ 0 đến 1
vec_rand = np.random.rand(5)
print("np.random.rand(5) =", vec_rand)

print("-" * 20)

# Các lệnh xử lý vector v
v = np.array([1., 3., 5.])
print("v =", v)

# Lệnh lấy tổng các thành phần của vector
sum_v = np.sum(v)
print("np.sum(v) =", sum_v)

# Lệnh xem số chiều của một vector
shape_v = v.shape
print("v.shape =", shape_v)

# Thử nghiệm "chuyển vị" vector (cho vector 1D không thay đổi)
transpose_v = v.transpose()
print("v.transpose() =", transpose_v)

# Lấy một phần của vector
v1 = v[:2]
print("v1 = v[:2] =", v1)

v_at_0 = v[0]
print("v[0] =", v_at_0)
print("v =", v)

print("v1 =", v1)
v1_slice_assign = [1., 2., 3.] # Gán một list có kích thước khác sẽ gây lỗi
# v1[:2] = [1., 2., 3.] # Lỗi vì v1[:2] chỉ có 2 phần tử
v_copy = np.copy(v)
v1_copy = v_copy[:2]
v1_copy[:] = [1., 2.] # Gán đúng kích thước
print("v sau khi gán vào bản sao của v1:", v_copy)

v1_assign = [4, 6]
# v1 = [4, 6] # Thay đổi tham chiếu, không ảnh hưởng đến v ban đầu
v_copy_2 = np.copy(v)
v1_copy_2 = v_copy_2[:2]
v1_copy_2[:] = v1_assign
print("v sau khi gán giá trị mới cho bản sao v1:", v_copy_2)
print("v =", v)

v3_expr = 2 * v[:2] + v[:2] * 3
print("v[:2] =", v[:2])
print("v3 = 2 * v[:2] + v[:2] * 3 =", v3_expr)

v1_new = np.array([4, 6])
print("v1 =", v1_new)
print("v =", v)

print("-" * 20)

# Các phép toán trên vector: sin, cos, sqrt
sqrt_v = np.sqrt(v + 10.0)
print("np.sqrt(v + 10.0) =", sqrt_v)

cos_v = np.cos(v)
print("np.cos(v) =", cos_v)

sin_v = np.sin(v)
print("np.sin(v) =", sin_v)

print("-" * 20)

# Tích vô hướng của hai vector
v1_dot_v3_result = np.dot(v[:2], vec3[:2])
print("np.dot(v[:2], vec3[:2]) =", v1_dot_v3_result)

v3_dot_v1_result = np.dot(vec3[:2], v[:2])
print("np.dot(vec3[:2], v[:2]) =", v3_dot_v1_result)
