import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#--------------------
# func definition

def draw_graph():

    f = open(data_file_full_path, mode="r")
    number_list = f.read().splitlines()

    figure(num=None, figsize=(30, 10), dpi=80, facecolor='w', edgecolor='k')

    i = 0
    x = list()
    y = list()
    for number in number_list:
        i = i + 1
        x.append(i)
        y.append(float(number))

    plt.scatter(x, y)
    plt.plot(x, y)    
    plt.savefig(image_file_full_path)
    plt.show()


if __name__ == "__main__":

    #--------------------
    # GLOBAL VARIABLES

    data_file_folder_path = "./data"
    data_file_name = "data.txt"
    data_file_full_path = data_file_path + data_file_name

    image_file_folder_path = "./images"
    image_file_name = "saved_image.png"
    image_file_full_path = image_file_folder_path + image_file_name

    #--------------------
    # function calling

    draw_graph()
