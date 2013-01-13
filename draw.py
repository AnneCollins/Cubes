from matplotlib import pyplot as plt
import matplotlib
from main import Direction


def draw_configuration(pts, target):
    """
    Draw a configuration--a set of points, as well as a background rectangle
    for the target shape.  Will draw the target rectangle offset by 0.5 to make
    things look right.

    Arguments:
        pts: set of (x,y) tuples
        target: Shape object
    """
    xs, ys = zip(*list(pts))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    rect1 = matplotlib.patches.Rectangle((-0.5,-0.5), target.length, target.width, 
                                        color='#DDDDFF', alpha=0.5)
    ax.add_patch(rect1)
    ax.scatter(xs, ys, color='#0000FF')
    plt.show()