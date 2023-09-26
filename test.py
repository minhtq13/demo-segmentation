import cv2

# Đọc hình ảnh từ tệp
image = cv2.imread('n8.jpg')

# Hiển thị hình ảnh trong cửa sổ
cv2.imshow('Hình ảnh', image)

# Đợi cho đến khi người dùng nhấn một phím bất kỳ
cv2.waitKey(0)

# Đóng cửa sổ hiển thị
cv2.destroyAllWindows()