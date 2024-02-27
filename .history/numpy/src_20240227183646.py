import numpy as np
matrix = [
    [1,2,30],
    [1,2,30],
    [1,2,30],
    [1,2,30],
]

# Tạo một mảng từ danh sách
arr1 = np.array([1, 2, 3, 4, 5])

# Tạo một mảng 2D 3x3 chứa toàn số 0
arr2 = np.zeros((3, 3))

# Tạo một mảng 1D gồm 5 phần tử có giá trị là 1
arr3 = np.ones(5)

# Tạo một mảng 2D 2x2 với các giá trị ngẫu nhiên từ phân phối đều
arr4 = np.random.rand(2, 2)


# Thêm một phần tử vào cuối mảng
arr1 = np.append(arr1, 6)

# Chuyển đổi một mảng 1D thành mảng 2D 2x3
arr5 = arr1.reshape(2, 3)

# Ghép mảng
arr6 = np.concatenate((arr1, arr2))

# Chia mảng thành các mảng con
sub_arrays = np.split(arr6, 2)

# Nối mảng theo chiều dọc và chiều ngang
vertical_stack = np.vstack((arr1, arr2))
horizontal_stack = np.hstack((arr1, arr2))


# Tính tổng các phần tử trong mảng
total = np.sum(arr1)

# Tính trung bình của các phần tử trong mảng
avg = np.mean(arr1)

# Tìm giá trị lớn nhất và nhỏ nhất trong mảng
max_val = np.max(arr1)
min_val = np.min(arr1)

# Tính trung vị của mảng
median = np.median(arr1)

# Tính độ lệch chuẩn của mảng
std_deviation = np.std(arr1)

# Tính tổng các phần tử trên mỗi hàng hoặc cột
row_sum = np.sum(matrix, axis=1)  # Tổng theo hàng
column_sum = np.sum(matrix, axis=0)  # Tổng theo cột


# Tìm các phần tử trong mảng lớn hơn 3
greater_than_3 = arr1[arr1 > 3]

# Kiểm tra xem tất cả các phần tử có lớn hơn 0 không
all_positive = np.all(arr1 > 0)

# Kiểm tra xem có phần tử nào lớn hơn 3 không
any_greater_than_3 = np.any(arr1 > 3)

# Kiểm tra xem tất cả các phần tử có nhỏ hơn 10 không
all_less_than_10 = np.all(arr1 < 10)



# Tìm chỉ số của phần tử lớn nhất trong mảng
idx_max = np.argmax(arr1)

# Trích xuất các phần tử thỏa mãn điều kiện từ một mảng
extracted = np.extract(arr1 > 3, arr1)

# Sắp xếp mảng theo thứ tự tăng dần
sorted_arr = np.sort(arr1)

# Tìm chỉ số của các phần tử sau khi sắp xếp
sorted_indices = np.argsort(arr1)



# Chuyển vị của một ma trận
transpose_matrix = np.transpose(matrix)

# Tính ma trận nghịch đảo
inverse_matrix = np.linalg.inv(matrix)

# Tính định thức của một ma trận
determinant = np.linalg.det(matrix)
