import matplotlib.pyplot as plt

def plot(xvals, yvals):
    plt.figure(figsize=(5,5))

    plt.scatter(xvals, yvals)

    plt.xlim([0, 480])
    plt.ylim([0, 640])
    plt.gca().invert_yaxis()
    return plt.show()
