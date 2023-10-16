import math

# def calculate_angle(point1, point2, point3):
#     # Tính góc giữa ba điểm theo công thức arctan
#     x1, y1 = point1
#     x2, y2 = point2
#     x3, y3 = point3

#     angle1 = math.atan2(y1 - y2, x1 - x2)
#     angle2 = math.atan2(y2 - y3, x2 - x3)
#     angle3 = math.atan2(y3 - y1, x3 - x1)

#     # Trả về góc lớn nhất và điểm tương ứng
#     angles = [angle1, angle2, angle3]
#     max_angle = max(angles)
#     # tính góc lớn nhất theo độ
#     max_angle_decard = max_angle * 180 / math.pi
#     print("Góc lớn nhất:", max_angle_decard)

#     max_index = angles.index(max_angle)

#     if max_index == 0:
#         return point1
#     elif max_index == 1:
#         return point2
#     else:
#         return point3

# # Sử dụng hàm với ví dụ
# points = [[0, 0], [2, 2], [0, 2]]
# result = calculate_angle(points[0], points[1], points[2])
# print("Đỉnh có góc lớn nhất:", result)

def distance(point1, point2):
    # Tính khoảng cách giữa hai điểm
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def find_largest_angle(points):
    if len(points) != 3:
        return None

    # Tính độ dài các cạnh của tam giác
    side1 = distance(points[0], points[1])
    print(side1)
    side2 = distance(points[1], points[2])
    print(side2)
    side3 = distance(points[2], points[0])
    print(side3)


    # Sử dụng định lý Cosin để tính góc lớn nhất
    cos_a = (side1**2 + side3**2 - side2**2) / (2 * side1 * side3)
    print(cos_a)
    cos_b = (side1**2 + side2**2 - side3**2) / (2 * side1 * side2)
    print(cos_b)
    cos_c = (side2**2 + side3**2 - side1**2) / (2 * side2 * side3)
    print(cos_c)

    # Tìm góc lớn nhất => góc lớn nhất là góc có cos nhỏ nhất
    min_cos = min(cos_a, cos_b, cos_c)

    if min_cos == cos_a:
        return points[0], round(math.degrees(math.acos(min_cos)))
    elif min_cos == cos_b:
        return points[1], round(math.degrees(math.acos(min_cos)))
    else:
        return points[2], round(math.degrees(math.acos(min_cos)))

# Ví dụ sử dụng hàm
points = [[1, 1], [4, 1], [6, 4]]
result_point, angle_degrees = find_largest_angle(points)
print("Đỉnh có góc lớn nhất:", result_point)
print("Góc lớn nhất (đơn vị độ):", angle_degrees)
