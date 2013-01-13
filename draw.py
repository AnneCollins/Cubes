from matplotlib import pyplot as plt
from main import Direction


def draw_configuration(pts):
    """
    Draw a configuration--a set of points
    """
    xs, ys = zip(*list(pts))
    plt.scatter(xs, ys)
    plt.show()