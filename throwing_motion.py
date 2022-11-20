import math
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

colors = list(mcolors.BASE_COLORS.keys())

MAX = 8
MIN = 1

gravity = 9.81  # g
c = 0.0  # c


class ThrowingObject:

    def __init__(self, name: str, m: float, v: float, theta: int, color: str, x0: int = 0, y0: int = 0,
                 maxx: int = math.inf):
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
        self.X = maxx
        self.vr =(m * gravity) / c

    def __str__(self):
        return f'{self.name}: v0 : {self.v0} - color:  {self.color} - theta: {self.theta}  - (y,t):  {[(self.y[i], self.t[i]) for i in range(0, self.t.__len__())]} - (x,t): {[(self.x[i], self.t[i]) for i in range(0, self.t.__len__())]}'

    def throw_object(self):
        tt = 0
        while (self.y.__len__() < 2 or self.y[-1] >= 0) and (
                self.x.__len__() < 1 or (self.X >= 0 and self.x[-1] < self.X) or (self.X < 0 and self.x[-1] > self.X)):
            self.y.append(((self.vr / gravity) * (self.vy + self.vr) * (1 - math.e ** (-gravity * tt / self.vr)) - (self.vr * tt)))
            self.x.append((((self.vr * self.vx) / gravity) * (1 - math.e ** (-gravity * tt / self.vr))))
            self.t.append(tt)
            tt += 0.001

        self.TT = tt


def plot(obj: [ThrowingObject]):
    fig, ax = plt.subplots(1, 2, figsize=(8, 5))

    for o in obj:
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

    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.4)
    matplotlib.pyplot.show()
    plt.show(block=True)


if __name__ == '__main__':
    print('WELLCOME To Throwing Mothion Simulator ')

    c = float(input('insert c : '))

    count = int(input(f'input count of object(between {MIN} - {MAX}) : '))
    while count < MIN or count > MAX:
        count = int(input(f'\n  wrong number  \n  please Enter valid number !!! between ({MIN} - {MAX}) : '))

    obstacle: int
    isObstacleAllowed: bool = False
    while True:
        askForObsObj = str(input('Do You wanna Place an Obstacle ? (Y/N) : '))
        match askForObsObj.split():
            case ['y' | 'Y']:
                obstacle = int(input(f'Place The Obstacle (Maximum x) : '))
                break
            case ['n' | 'N']:
                obstacle = math.inf
                break
            case default:
                print('\ninsert valid input !!! \n')

    tObjects: [ThrowingObject] = []

    for i in range(1, count + 1):
        print(f'insert M , v & theta for object #{i}')
        m = float(input(f'M_#{i} : '))
        v = int(input(f'v0_#{i} : '))
        theta = int(input(f'theta_#{i} : '))
        obj = ThrowingObject(f'Object#{i}', m, v, theta, colors[i - 1], maxx=obstacle)
        obj.throw_object()
        tObjects.append(obj)

    plot(tObjects)
