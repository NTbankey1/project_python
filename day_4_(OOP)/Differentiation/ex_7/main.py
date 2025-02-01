from abc import ABC, abstractmethod
import numpy as np

# Lớp trừu tượng cho ma trận
class Matrix(ABC):
    @abstractmethod
    def determinant(self):
        pass

# Ma trận vuông
class SquareMatrix(Matrix):
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        if self.matrix.shape[0] != self.matrix.shape[1]:
            raise ValueError("Ma trận phải là ma trận vuông")

    def determinant(self):
        return round(np.linalg.det(self.matrix), 2)

# Ma trận đơn vị
class IdentityMatrix(SquareMatrix):
    def __init__(self, size):
        super().__init__(np.eye(size))

# Sử dụng
m1 = SquareMatrix([[4, 3], [6, 3]])
m2 = IdentityMatrix(3)

print("Định thức của ma trận m1:", m1.determinant())  # ✅ -6.0
print("Định thức của ma trận đơn vị:", m2.determinant())  # ✅ 1.0
