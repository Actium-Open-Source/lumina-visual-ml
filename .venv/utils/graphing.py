import matplotlib.pyplot as plt

def plot(xvals, yvals):
    plt.figure(figsize=(5,5)) # creating plot

    plt.scatter(xvals, yvals) # scatter hand points onto graph

    plt.xlim([0, 480]) # setting boundries for x-plane
    plt.ylim([0, 640]) # setting bounrdries for y-plan
    plt.gca().invert_yaxis() # inverting it so it is more visually understandable
    return plt.show() # show it!
