# example2.py

"""
http://ipywidgets-server.readthedocs.io/en/stable/tutorials.html
"""

import time

import matplotlib.pyplot as plt

import numpy as np

import ipywidgets as widgets
from IPython.display import display

SIZE = 50
XBASIS = np.linspace(0.0, 1.0, SIZE)

container = widgets.VBox()

def update():
    """ Generate a new random plot and embed it into the container """
    output = widgets.Output()
    with output:
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.plot(XBASIS, np.random.rand(SIZE))
        ax.set_ylim(0.0, 1.0)
        plt.show()
    container.children = [output]

display(container)

while True:
    # Update the plot in a busy loop
    time.sleep(1)
    update()