import os

import matplotlib.pyplot as plt


def paint(matrix):
    count = len(matrix)
    if count<30:
        x = [0, 30]
        y = x
    else:
        x=[0,2000]
        y = x
    plt.figure()
    plt.plot(x, y)
    if(count<30):
        for i in matrix:
            v1 = float(i[1])
            v2 = float(i[2])
            if ( int(v1) <= 30 and  int(v2) < 30 and int(v1)>0 and int(v2)>0 ):
                if (v1 < v2):
                    plt.scatter(v1, v2, c="#FF0000")
                else:
                    plt.scatter(v1, v2, c="#0000FF")
    else:
        for i in matrix:
            v1 = float(i[1])
            v2 = float(i[2])
            if (int(v1) <= 2000 and int(v2) < 2000 and int(v1) > 0 and int(v2) > 0 and ( 0.5 <(v2 / (v1)) < 1.5)):
                if (v1 < v2):
                    plt.scatter(v1, v2, c="#FF0000")
                else:
                    plt.scatter(v1, v2, c="#0000FF")
    plt.xlabel("ControlSample")
    plt.ylabel("KnockOutSample")
    # plt.show()
    os.remove("static/image/figure.png")
    plt.savefig("static/image/figure.png")