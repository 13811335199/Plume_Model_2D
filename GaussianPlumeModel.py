import numpy as np
import matplotlib.pyplot as plt

# 大气稳定度D, Y水平方向扩散参数
def sigma_y(x):
    return 0.08 * x * (1 + 0.0001 * x) ** 0.5


# 大气稳定度D, Z垂直方向扩散参数
def sigma_z(x):
    return 0.06 * x * (1 + 0.0015 * x) ** 0.5


# 大气稳定度D, (x,y,z)的浓度值C, Q源项释放率, H有效排放高度, u平均风速
def Concentration_XYZ(Q, H, u, x, y, z):
    a = np.exp((-y * y) / (2 * sigma_y(x) * sigma_y(x)))
    b = np.exp((-(z - H) * (z - H)) / (2 * sigma_z(x) * sigma_z(x)))
    d = np.exp((-(z + H) * (z + H)) / (2 * sigma_z(x) * sigma_z(x)))
    e = 2 * np.pi * u * sigma_y(x) * sigma_z(x)
    C = Q * a * (b + d) / e
    return C


# input
# u = 2  # 平均风速，m/s
# Q = 100  # 源项释放率，Bq/s
# H = 50  # 有效排放高度，m

D = Concentration_XYZ(100, 50, 2, 100, 100, 1.5)
print(D)
