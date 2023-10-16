def find_fourth_point(p1, p2, p3):
    # p1, p2, và p3 lần lượt là các toạ độ của 3 trong 4 điểm của hình bình hành
    x4 = p2[0] + p3[0] - p1[0]
    y4 = p2[1] + p3[1] - p1[1]
    return (x4, y4)

# Ví dụ sử dụng hàm
point1 = (1, 1)
point2 = (4, 1)
point3 = (6, 4)

fourth_point = find_fourth_point(point1, point2, point3)
print("Toạ độ điểm thứ tư:", fourth_point)