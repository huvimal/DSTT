#Bài tập 1
import numpy as np

# a. Tự chọn một ma trận khả nghịch 3x3
A = np.array([[4, 2, 1],
              [0, 1, 3],
              [2, 1, 5]])

# Kiểm tra tính khả nghịch của ma trận
if np.linalg.det(A) != 0:
    print("Ma trận khả nghịch:", A)
else:
    print("Ma trận không khả nghịch.")

# b. Nhập họ tên và mã số sinh viên
name = input(" Lê Mai Vĩnh Hưng ")
student_id = input(" 2274802010347 ")

# c. Mã hóa họ tên và mã số sinh viên
encoded_name = ''.join(format(ord(char), '08b') for char in name)  # Mã hóa bằng nhị phân
encoded_id = ''.join(format(ord(char), '08b') for char in student_id)

print("Họ tên sinh viên đã mã hóa:", encoded_name)
print("Mã số sinh viên đã mã hóa:", encoded_id)

# d. Thực hiện giải ma trận với ma trận đảo
inverse_A = np.linalg.inv(A)
print("Ma trận đảo của A là:\n", inverse_A)

#Bài tập 2
from fractions import Fraction

def continued_fraction(numerator, denominator):
    """Tính phân số liên tiếp"""
    fractions = []
    
    while denominator != 0:
        integer_part = numerator // denominator
        fractions.append(integer_part)
        numerator, denominator = denominator, numerator - integer_part * denominator

    return fractions

# a. Tính phân số liên tiếp cho 8/3
numerator1 = 8
denominator1 = 3
cf1 = continued_fraction(numerator1, denominator1)
print(f"Phân số liên tiếp của {numerator1}/{denominator1}: {cf1}")

# b. Tính phân số liên tiếp cho 11/3
numerator2 = 11
denominator2 = 3
cf2 = continued_fraction(numerator2, denominator2)
print(f"Phân số liên tiếp của {numerator2}/{denominator2}: {cf2}")

# c. Tính giá trị của phân số liên tiếp
def compute_from_continued_fraction(cf):
    """Tính giá trị từ phân số liên tiếp"""
    result = Fraction(cf[-1])
    for coeff in reversed(cf[:-1]):
        result = coeff + 1/result
    return result

# Tính giá trị cho 8/3 và 11/3
value1 = compute_from_continued_fraction(cf1)
value2 = compute_from_continued_fraction(cf2)

print(f"Gía trị cho phân số liên tiếp của {numerator1}/{denominator1}: {value1}")
print(f"Gía trị cho phân số liên tiếp của {numerator2}/{denominator2}: {value2}")