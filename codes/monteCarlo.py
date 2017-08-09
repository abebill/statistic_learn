# --*-- coding: utf-8 --*--
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def monteCarlo(n):
    o, r = (0., 0.), 1.0  #设置圆心及半径
    a, b = (o[0] - r , o[0] + r), (o[1] - r , o[1] + r)  #设置正方形边长范围

    #在正方形内投点
    x = np.random.uniform(a[0], a[1], n)
    y = np.random.uniform(b[0], b[1], n)

    #获取落入圆内点的数目
    dist = np.sqrt((x - o[0]) ** 2 + (y - o[1]) ** 2)
    goal_dots = len([i for i in dist if i < r])

    pi = 4 * float(goal_dots) / n
    print '值为：', pi

    #图示化
    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(x, y, 'o', markersize = 1)
    plt.axis('equal')
    circle = Circle(o, r, alpha = 0.5)
    axes.add_patch(circle)

    plt.show()


if __name__ == '__main__':
    monteCarlo(10000)