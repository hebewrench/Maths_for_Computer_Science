import numpy as np
import math
def calc_angle(x, y):
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    return theta

a = np.array([1,1,0,2,0,0,2,0,2,0,1,0,0,0,0,2])
b = np.array([0,0,2,0,0,1,0,2,0,1,0,1,1,0,0,0])
c = np.array([0,0,2,0,1,0,0,0,3,0,0,0,0,2,1,0])

print(a)
print(b)
print(c)


print("A vs B:", calc_angle(a, b))
print("B vs C:", calc_angle(b, c))
print("A vs C:", calc_angle(a, c))

d=np.array([1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2])
e=np.array([0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0])
print("D vs E:", calc_angle(d, e))
