# 101Computing.net/projection-motion-formula
import math
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

colors = list(mcolors.BASE_COLORS.keys())

MAX = 8
MIN = 1

gravity = 9.81  # g
angle = 70  # theta
velocity = 80  # v0

t = 0


class Ball:

    def __init__(self, name: str, v: float, theta: int, color: str, x0: int = 0, y0: int = 0):
        self.name = name
        self.v0 = v
        self.theta = (theta % 360)
        self.x0 = x0
        self.y0 = y0
        self.vx = self.v0 * math.cos(math.radians(self.theta))
        self.vy = self.v0 * math.sin(math.radians(self.theta))
        self.TT = 0
        self.t = []
        self.y = []
        self.x = []
        self.color = color

    def __str__(self):
        return f'{self.name}: v0 : {self.v0} - color:  {self.color} - theta: {self.theta}  - (y,t):  {[(self.y[i], self.t[i]) for i in range(0, self.t.__len__())]} - (x,t): {[(self.x[i], self.t[i]) for i in range(0, self.t.__len__())]}'

    def throw_ball(self):
        tt = 0
        while self.y.__len__() < 2 or self.y[-1] >= 0:
            self.y.append(self.y0 + (self.vy * tt - 0.5 * gravity * tt ** 2))
            self.x.append(self.x0 + (self.vx * tt))
            self.t.append(tt)
            tt += 0.001

        self.TT = tt


def plot(obj: [Ball]):
    fig, ax = plt.subplots(1, 2, figsize=(8, 5))

    for o in tObjects:
        ax[0].plot(o.t, o.y, ls='-', color=o.color, lw=2, label=o.name)

        ax[1].plot(o.t, o.x, ls='-', color=o.color, lw=2, label=o.name)


    ax[0].set_xlabel('$t$', fontsize=14)
    ax[0].set_ylabel('$y(t)$', fontsize=14)
    ax[0].axvline(x=10, ls='', color='black')
    ax[0].legend(loc='best')

    ax[1].set_xlabel('$t$', fontsize=14)
    ax[1].set_ylabel('$x(t)$', fontsize=14)
    ax[1].axvline(x=10, ls='', color='black')
    ax[1].legend(loc='best')

    plt.show()


if __name__ == '__main__':
    print('WELLCOME To Throwing Mothion Simulator ')

    count = int(input(f'input count of object(between {MIN} - {MAX}) : '))
    tObjects: [Ball] = []
    while count < MIN or count > MAX:
        count = int(input(f'\n  wrong number  \n  please Enter valid number !!! between ({MIN} - {MAX}) : '))

    for i in range(1, count + 1):
        print(f'insert v & theta for object #{i}')
        v = int(input(f'v0_#{i} : '))
        theta = int(input(f'theta_#{i} : '))
        obj = Ball(f'Object#{i}', v, theta, colors[i - 1], )
        obj.throw_ball()
        tObjects.append(obj)

    plot(tObjects)
