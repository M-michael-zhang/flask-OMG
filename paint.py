
import matplotlib.pyplot as plt


def paint(matrix ):
    x = [0, 30]
    y = x
    plt.figure()
    plt.plot(x, y)
    for i in matrix:
        v1 = float(i[1])
        v2 = float(i[2])
        if (int(v1) <= 30 and int(v2) < 30):
            if (v2 != 0 and v1 / v2 < 1):
                plt.scatter(v1, v2, c="#FF0000")
            else:
                plt.scatter(v1, v2, c="#0000FF")
    plt.xlabel("ControlSample")
    plt.ylabel("KnockOutSample")
    # plt.show()
    plt.savefig("static/image/figure.png")